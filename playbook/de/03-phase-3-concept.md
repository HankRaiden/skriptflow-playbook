# Phase 3 · Konzept

**Ziel der Phase:** Aus der gewählten Lösung wird ein Konzept, das man zeigen, besprechen und umsetzen kann.

Vorher: [Phase 2 · Lösung](02-phase-2-solution.md). Starte Phase 3 erst, wenn in Schritt 8 ein Mensch entschieden hat.

---

## Schritt 9 · KI: Strategiepapier und Konzept

**Wer:** KI · **Ergebnis:** Strategiepapier (2–4 Seiten)

```text
{{KONTEXT}}

Schreibe auf Basis der gewählten Lösung ein Strategiepapier für meinen Gesprächspartner.

Aufbau:
1. Ausgangslage – in seinen Worten (kurze Zitate aus dem Transkript).
2. Ziel – was nach der Umsetzung anders ist, beschrieben als Alltag, nicht als Technik.
3. Lösung – die gewählte Variante, in einfachen Worten.
4. Nutzenargumentation – je Baustein: Merkmal → Vorteil → Nutzen für genau diesen Gesprächspartner.
5. Umsetzung in Phasen – mit erstem schnellen Erfolg nach wenigen Wochen.
6. Was wir von dir brauchen – Entscheidungen, Zugänge, Ansprechpartner.
7. Risiken und wie wir ihnen begegnen.
8. Nächste Schritte.

Regeln:
- Du-Form oder Sie-Form wie im Kontext angegeben.
- KEINE erfundenen Zahlen, Kundenstimmen, Studien oder Garantien. Wo eine Zahl fehlt, schreibe „[zu klären]“.
- Kein Fachjargon ohne Erklärung.

Gewählte Lösung und Entscheidung:
{{ENTSCHEIDUNG}}

Ist-Analyse:
{{IST_ANALYSE}}
```

**Prüfen:** Suche gezielt nach erfundenen Belegen. KI-Texte neigen zu „Unsere Kunden berichten von 25 % mehr …“. Wenn du so einen Satz nicht beweisen kannst, streiche ihn. Vertrauen ist das Einzige, was du in einem Erstgespräch wirklich verkaufst.

Vertiefung: [Nutzenargumentation](benefit-argument.md)

---

## Schritt 10 · KI: Ablaufdiagramm für die Umsetzung

**Wer:** KI · **Ergebnis:** Diagramm der Umsetzung (Phasen, Pakete, Abhängigkeiten)

```text
{{KONTEXT}}

Erstelle aus dem Strategiepapier ein Ablaufdiagramm der UMSETZUNG als Mermaid-Code (flowchart LR).
- Eine Spalte (subgraph) je Phase.
- In jeder Phase die Pakete bzw. Arbeitsschritte als Kästen.
- Pfeile für Abhängigkeiten („B braucht A“).
- Kennzeichne Stellen, an denen der Kunde entscheiden oder liefern muss, mit ◆.
- Maximal 14 Kästen.
Gib danach eine Liste der Meilensteine aus, an denen man gemeinsam prüft, ob es wirkt.

Strategiepapier:
{{STRATEGIEPAPIER}}
```

---

## Schritt 11 · KI: Inhalte für die Präsentation

**Wer:** KI · **Ergebnis:** Folie-für-Folie-Inhalt

```text
{{KONTEXT}}

Erstelle den Inhalt für eine Präsentation mit höchstens 12 Folien für das Folgegespräch.
Für jede Folie: Titel (max. 8 Wörter), Kernaussage (ein Satz), 3 Stichpunkte, Vorschlag für ein Bild oder Diagramm.

Pflichtfolien:
- „Das habe ich verstanden“ – mit dem bestätigten Ist-Diagramm.
- „So könnte es aussehen“ – mit dem Soll-Diagramm.
- „Was es dir bringt“ – Nutzenargumentation.
- „So starten wir“ – erster Schritt, Zeitrahmen, was wir von dir brauchen.

Regeln: Sprich in der Sprache des Gesprächspartners. Keine erfundenen Zahlen. Keine Folie ohne klare Aussage.

Strategiepapier:
{{STRATEGIEPAPIER}}
Umsetzungsdiagramm:
{{UMSETZUNGSDIAGRAMM}}
```

---

## Schritt 12 · Mensch: Präsentation bauen und besprechen

**Wer:** Mensch · **Ergebnis:** fertige Präsentation und ein Gespräch auf Augenhöhe

Die KI hat Inhalte geliefert. Die Präsentation baust du selbst – in deiner Sprache, mit deinem Gefühl für dein Gegenüber. Dieser letzte Prompt bereitet dich auf das Gespräch vor:

```text
{{KONTEXT}}

Ich präsentiere morgen das Konzept. Bereite mich vor:
1. Die fünf wahrscheinlichsten Einwände meines Gesprächspartners – und je eine ehrliche, kurze Antwort.
2. Drei Fragen, mit denen ich das Gespräch öffne, statt mit Folien zu beginnen.
3. Woran ich merke, dass etwas nicht passt – und wie ich dann reagiere.

Material:
{{STRATEGIEPAPIER}}
{{IST_ANALYSE}}
```

**Prüfen:** Das Ziel ist nicht „verkaufen“, sondern ein gemeinsames Bild. Wenn dein Gesprächspartner im Ist-Diagramm sein Unternehmen wiedererkennt, ist der wichtigste Schritt bereits geschafft.

Zurück zur Übersicht: [Checkliste](checklist.md)
