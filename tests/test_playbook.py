"""Guards for the SkriptFlow playbook: language parity, step completeness, privacy and honesty rules."""
from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
LANGS = ["de", "en", "pt-br"]
FILES = ["00-prepare.md", "01-phase-1-current-state.md", "02-phase-2-solution.md", "03-phase-3-concept.md",
         "roles.md", "crm-draft.md", "benefit-argument.md", "checklist.md"]
STEP_WORD = {"de": "Schritt", "en": "Step", "pt-br": "Passo"}
PHASE_STEPS = {"01-phase-1-current-state.md": [1, 2, 3, 4], "02-phase-2-solution.md": [5, 6, 7, 8],
               "03-phase-3-concept.md": [9, 10, 11, 12]}
# Real third parties from the original project, money amounts and the author's real name must never appear.
FORBIDDEN = re.compile(r"(?i)stac+k?\s?valley|\bluca\b|\bsabine\b|\bigel\b|felipe|holanda|\d\s?€|€\s?\d|\bEUR\b")
DISCLAIMER = {"de": "Ich übernehme keine Verantwortung für jegliche Ergebnisse",
              "en": "I accept no responsibility for any results",
              "pt-br": "Não assumo nenhuma responsabilidade por quaisquer resultados"}


def all_text_files():
    return [p for p in ROOT.rglob("*") if p.is_file() and p.suffix in {".md", ".mmd", ".txt", ".csv", ".yml"}
            and ".git" not in p.parts and ".venv" not in p.parts]


@pytest.mark.parametrize("lang", LANGS)
def test_every_language_has_every_file(lang):
    missing = [f for f in FILES if not (ROOT / "playbook" / lang / f).exists()]
    assert not missing, f"{lang}: missing {missing}"


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("fname", list(PHASE_STEPS))
def test_phase_files_contain_their_steps_with_a_prompt(lang, fname):
    text = (ROOT / "playbook" / lang / fname).read_text(encoding="utf-8")
    word = STEP_WORD[lang]
    for n in PHASE_STEPS[fname]:
        assert re.search(rf"^## {word} {n}\b", text, re.M), f"{lang}/{fname}: heading '## {word} {n}' missing"
    sections = re.split(rf"^## {word} \d+", text, flags=re.M)[1:]
    for n, sec in zip(PHASE_STEPS[fname], sections):
        assert "```text" in sec, f"{lang}/{fname}: {word} {n} has no copy-paste prompt block"


@pytest.mark.parametrize("lang", LANGS)
def test_languages_have_same_number_of_prompts(lang):
    def count(l):
        return sum((ROOT / "playbook" / l / f).read_text(encoding="utf-8").count("```text") for f in FILES)
    assert count(lang) == count("de"), f"{lang} has {count(lang)} prompts, de has {count('de')}"


def test_no_third_parties_money_or_real_name():
    hits = []
    for p in all_text_files():
        if p.name == "test_playbook.py":
            continue
        for m in FORBIDDEN.finditer(p.read_text(encoding="utf-8")):
            hits.append(f"{p.relative_to(ROOT)}: {m.group(0)!r}")
    assert not hits, hits


def test_mermaid_blocks_start_with_a_diagram_type():
    bad = []
    for p in all_text_files():
        text = p.read_text(encoding="utf-8")
        blocks = re.findall(r"```mermaid\n(.*?)```", text, re.S)
        if p.suffix == ".mmd":
            blocks.append(text)
        for b in blocks:
            if not re.match(r"\s*(flowchart|graph|sequenceDiagram|gantt|mindmap|timeline)\b", b):
                bad.append(f"{p.relative_to(ROOT)}: {b[:40]!r}")
    assert not bad, bad


def test_relative_links_resolve():
    broken = []
    for p in all_text_files():
        if p.suffix != ".md":
            continue
        for target in re.findall(r"\]\((?!https?://|#|mailto:)([^)#\s]+)", p.read_text(encoding="utf-8")):
            if not (p.parent / target).exists():
                broken.append(f"{p.relative_to(ROOT)} -> {target}")
    assert not broken, broken


@pytest.mark.parametrize("lang", LANGS)
def test_disclaimer_in_readme_and_disclaimer_file(lang):
    readme = {"de": "README.md", "en": "README.en.md", "pt-br": "README.pt-br.md"}[lang]
    assert DISCLAIMER[lang] in (ROOT / readme).read_text(encoding="utf-8")
    assert DISCLAIMER[lang] in (ROOT / "DISCLAIMER.md").read_text(encoding="utf-8")


def test_example_is_marked_fictional():
    for p in (ROOT / "examples").rglob("*.md"):
        head = p.read_text(encoding="utf-8")[:600].lower()
        assert "fiktiv" in head or "fictional" in head, f"{p.relative_to(ROOT)} must say it is fictional at the top"
