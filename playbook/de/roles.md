# Rollen · Ein Gespräch, viele Perspektiven

Ein CTO hört in einem Gespräch etwas anderes als eine Marketingleiterin oder jemand aus dem Kundenservice. Das kannst du nutzen: Gib der KI eine Rolle, und sie liest dasselbe Transkript durch eine andere Brille.

**So verwendest du die Vorlagen:** Kontext-Block + Rollen-Prompt + bereinigtes Transkript. Eine Rolle pro Durchlauf. Vergleiche danach die Ergebnisse – die Unterschiede sind oft die wertvollsten Erkenntnisse.

## Die Grundform

Alle Rollen folgen derselben Form. Du kannst damit jede weitere Rolle selbst bauen (Einkauf, Personal, Finanzen, Qualität …).

```text
{{KONTEXT}}

Agiere als {{ROLLE}} mit langjähriger Erfahrung in {{BRANCHE}}.
Lies das Transkript ausschließlich aus deiner Perspektive und beantworte:
1. Was ist aus deiner Sicht das eigentliche Thema dieses Gesprächs?
2. Welche drei Aussagen sind für deinen Bereich am wichtigsten? (wörtliches Zitat + warum)
3. Welche Risiken oder Chancen siehst du, die andere übersehen würden?
4. Welche Fragen würdest du im nächsten Gespräch stellen?
5. Was sollte aus deiner Sicht als Erstes passieren?
Bleib in deiner Rolle. Keine allgemeinen Ratschläge außerhalb deines Fachgebiets.

Transkript:
{{TRANSKRIPT_BEREINIGT}}
```

## Fertige Rollen

### Geschäftsführung

```text
{{KONTEXT}}

Agiere als Geschäftsführer eines mittelständischen Unternehmens. Lies das Transkript mit Blick auf:
Wachstumsgrenzen, Abhängigkeit von einzelnen Personen, Entscheidungen, die anstehen, und was das Thema
für Ertrag und Zukunftsfähigkeit bedeutet. Beantworte die fünf Fragen der Grundform (Thema, drei
wichtigste Aussagen mit Zitat, übersehene Risiken/Chancen, nächste Fragen, erster Schritt).

Transkript:
{{TRANSKRIPT_BEREINIGT}}
```

### CTO / IT

```text
{{KONTEXT}}

Agiere als CTO. Lies das Transkript mit Blick auf: eingesetzte Systeme, Medienbrüche (Papier, E-Mail,
Excel, Word), doppelte Datenhaltung, Schnittstellen, Datenschutz und IT-Sicherheit, Wartbarkeit.
Beantworte die fünf Fragen der Grundform und skizziere zusätzlich die heutige Systemlandschaft als Liste.

Transkript:
{{TRANSKRIPT_BEREINIGT}}
```

### Marketing (CMO)

```text
{{KONTEXT}}

Agiere als Marketingleiter. Lies das Transkript mit Blick auf: Wie finden Kunden das Unternehmen? Welche
Sprache benutzt der Gesprächspartner für sein Angebot und seine Kunden? Welche Botschaften, Positionierung
und Kanäle stecken darin? Beantworte die fünf Fragen der Grundform und sammle zusätzlich wörtliche
Formulierungen, die sich für Texte eignen.

Transkript:
{{TRANSKRIPT_BEREINIGT}}
```

### Vertrieb

```text
{{KONTEXT}}

Agiere als Vertriebsleiter im B2B. Lies das Transkript mit Blick auf: Kaufsignale, Bedarf, Dringlichkeit,
Entscheider und Beeinflusser, Budget-Signale (ohne Beträge), Einwände, nächster Schritt. Beantworte die
fünf Fragen der Grundform und schließe mit einer Einschätzung: Wie warm ist diese Gelegenheit (kalt/lau/heiß) und warum?

Transkript:
{{TRANSKRIPT_BEREINIGT}}
```

### Kundenservice

```text
{{KONTEXT}}

Agiere als Leiterin Kundenservice. Lies das Transkript mit Blick auf: wiederkehrende Fragen und Probleme
von Kunden, Wartezeiten, Übergaben zwischen Personen, an denen Informationen verloren gehen, und was
Kunden frustriert. Beantworte die fünf Fragen der Grundform.

Transkript:
{{TRANSKRIPT_BEREINIGT}}
```

### Schulung / Wissensvermittlung

Für interne Schulungen (z. B. eine CRM-Schulung): Aus dem Transkript wird ein Lernbild für Kolleginnen und Kollegen.

```text
{{KONTEXT}}

Agiere als Trainer für Erwachsenenbildung. Das Transkript stammt aus einer Schulung.
1. Fasse die wichtigsten Prinzipien in höchstens 7 Sätzen zusammen – so, dass ein neuer Kollege sie versteht.
2. Erstelle den gezeigten Arbeitsablauf als Mermaid-Diagramm (flowchart TD), Schritt für Schritt, mit den Stellen, an denen Anwender typischerweise Fehler machen (⚠).
3. Formuliere 5 Verständnisfragen mit Lösung.
4. Liste Fragen aus der Schulung auf, die unbeantwortet blieben.

Transkript:
{{TRANSKRIPT_BEREINIGT}}
```

### KI-Berater

Die stärkste Rolle für Erstgespräche – siehe auch [Schritt 6](02-phase-2-solution.md#schritt-6--ki-lösung-als-ablaufdiagramm--die-ki-als-berater).

```text
{{KONTEXT}}

Agiere als {{z. B. „AI-Consultant mit Expertise in AI Automation“}}. Nenne mir drei Vorschläge, drei Ideen,
wie wir die Anfrage meines Gesprächspartners erfüllen können. Je Vorschlag: Kernidee, erster Schritt,
größtes Risiko. Unterscheide klar zwischen schnell/schlank, ausgewogen und weitreichend.

Transkript:
{{TRANSKRIPT_BEREINIGT}}
```

### Challenger

Für jedes Ergebnis, das du jemandem zeigen willst – siehe [Schritt 7](02-phase-2-solution.md#schritt-7--ki-challenger--bewerten-und-optimieren).

```text
Du bist ein kritischer Challenger. Finde die drei größten Schwächen des folgenden Ergebnisses, bevor es
mein Gesprächspartner tut: unbelegte Behauptungen, Widersprüche zum Transkript, übersehene Risiken.
Schlage je Schwäche eine konkrete Verbesserung vor. Sei streng, aber fair.

Ergebnis:
{{ERGEBNIS}}

Transkript zum Abgleich:
{{TRANSKRIPT_BEREINIGT}}
```

## Perspektiven zusammenführen

```text
Hier sind die Auswertungen desselben Gesprächs aus mehreren Rollen. Erstelle eine Tabelle:
Thema | Geschäftsführung | IT | Marketing | Vertrieb | Service – und markiere, wo sich die Rollen
widersprechen. Leite daraus die drei Themen ab, die im nächsten Gespräch geklärt werden müssen.

{{ROLLEN_ERGEBNISSE}}
```
