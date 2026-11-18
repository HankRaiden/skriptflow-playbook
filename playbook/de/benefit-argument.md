# Nutzenargumentation · Merkmal → Vorteil → Nutzen

Menschen kaufen keine Merkmale. Sie kaufen, was ein Merkmal in ihrem Alltag verändert. Die Nutzenargumentation übersetzt in drei Stufen:

| Stufe | Frage | Beispiel |
|---|---|---|
| **Merkmal** | Was ist es? | Das Erstgespräch wird als Ablaufdiagramm dargestellt. |
| **Vorteil** | Was kann es? | Beide Seiten sehen denselben Ablauf auf einem Bild. |
| **Nutzen** | Was hast **du** davon? | Missverständnisse fallen auf, bevor ein Angebot geschrieben wird – nicht erst mitten im Projekt. |

Der Nutzen ist immer **persönlich** und **im Alltag des Gegenübers** formuliert. Ein guter Test: Kann man an den Nutzen-Satz „… und deshalb …“ anhängen, ohne dass es albern klingt? Dann ist es noch ein Vorteil.

## Der Prompt

```text
{{KONTEXT}}

Formuliere für jeden Baustein der gewählten Lösung eine Nutzenargumentation in drei Stufen:
Merkmal (was es ist) → Vorteil (was es kann) → Nutzen (was mein Gesprächspartner in SEINEM Alltag davon hat).

Regeln:
- Der Nutzen bezieht sich auf einen konkreten Schmerzpunkt aus der Ist-Analyse; nenne das Zitat als Beleg.
- Nutze die Sprache des Gesprächspartners, nicht unsere Fachsprache.
- KEINE erfundenen Zahlen, Prozentwerte, Studien oder Kundenstimmen. Wenn ein Nutzen nur mit einer Zahl
  überzeugt, die wir nicht haben, schreibe stattdessen, wie man sie gemeinsam messen könnte.
- Am Ende: der eine Nutzen, der für diesen Gesprächspartner am schwersten wiegt – in einem Satz.

Gewählte Lösung:
{{ENTSCHEIDUNG}}
Ist-Analyse:
{{IST_ANALYSE}}
```

## Nutzen je Rolle

Derselbe Baustein hat für verschiedene Menschen verschiedenen Nutzen. Kombiniere die Nutzenargumentation mit den [Rollen](roles.md):

```text
Formuliere die Nutzenargumentation für denselben Baustein dreimal: für die Geschäftsführung, für die
Mitarbeiter, die damit täglich arbeiten, und für die Kunden des Unternehmens. Je ein Satz Nutzen.

Baustein:
{{BAUSTEIN}}
```

## Häufige Fehler

- **Nutzen ohne Bezug:** „Spart Zeit“ – wessen Zeit, wobei, wofür wird sie frei?
- **Erfundene Beweise:** Ein ausgedachter Prozentwert zerstört mehr Vertrauen, als er schafft.
- **Merkmal-Listen:** Zehn Funktionen überzeugen weniger als ein Nutzen, der genau den Schmerz trifft, den der Gesprächspartner selbst genannt hat.
