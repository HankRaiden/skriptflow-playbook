# Phase 2 · Lösung

**Ziel der Phase:** Aus einem bestätigten Ist-Bild werden mehrere Lösungswege – geprüft von einem kritischen Gegenspieler und ausgewählt von einem Menschen.

Vorher: [Phase 1 · Ist-Analyse](01-phase-1-current-state.md). Starte Phase 2 erst, wenn dein Gesprächspartner das Ist-Diagramm bestätigt hat.

---

## Schritt 5 · KI: 30 Ideen für Automatisierung und Verbesserung

**Wer:** KI · **Ergebnis:** Ideenliste mit grober Bewertung

Warum 30? Weil die ersten zehn Ideen die offensichtlichen sind. Die interessanten kommen danach.

```text
{{KONTEXT}}

Du bist Berater für Prozessautomatisierung und KI im Mittelstand.
Entwickle auf Basis der Ist-Analyse und des bestätigten Ist-Diagramms 30 konkrete Ideen, wie der Ablauf
verbessert oder automatisiert werden kann.

Gib eine Tabelle aus mit den Spalten:
Nr. | Idee (ein Satz) | Löst Schmerzpunkt | Aufwand (klein/mittel/groß) | Wirkung (klein/mittel/groß) | Risiko / Voraussetzung

Regeln:
- Mische: schnelle Erfolge ohne neue Software, Automatisierungen mit vorhandenen Werkzeugen, KI-Einsatz, organisatorische Änderungen.
- Jede Idee muss einen Schmerzpunkt aus der Ist-Analyse adressieren.
- Keine Werbung für bestimmte Anbieter; Werkzeuge nur als Beispiel nennen.
- Markiere am Ende die 5 Ideen mit dem besten Verhältnis aus Wirkung zu Aufwand.

Ist-Analyse:
{{IST_ANALYSE}}

Bestätigtes Ist-Diagramm:
{{IST_DIAGRAMM}}
```

**Prüfen:** Streiche, was für dieses Unternehmen offensichtlich nicht passt. Du kennst Kultur, Budget und Menschen – die KI nicht.

---

## Schritt 6 · KI: Lösung als Ablaufdiagramm – die KI als Berater

**Wer:** KI in einer Experten-Rolle · **Ergebnis:** drei Lösungsvorschläge, jeder als Soll-Diagramm

Hier gibst du der KI eine Rolle, die zur Anfrage passt. Sucht dein Gesprächspartner z. B. jemanden für KI-Automatisierung, lautet die Rolle „AI-Consultant mit Expertise in AI Automation“. Sucht er einen Vertriebsprozess, ist es „Vertriebsberater für B2B im Mittelstand“.

```text
{{KONTEXT}}

Agiere als {{ROLLE, z. B. „AI-Consultant mit Expertise in AI Automation“}} mit 15 Jahren Praxiserfahrung.

Nenne mir DREI unterschiedliche Lösungsvorschläge, wie wir die Anforderungen meines Gesprächspartners erfüllen
können. Die drei sollen sich wirklich unterscheiden, z. B.:
- A: schnell und schlank (mit vorhandenen Werkzeugen, in Wochen umsetzbar),
- B: ausgewogen (einige neue Bausteine, deutlich mehr Wirkung),
- C: weitreichend (größerer Umbau, größter Hebel).

Für jeden Vorschlag:
1. Kernidee in zwei Sätzen.
2. Welche Ideen aus der 30er-Liste er bündelt (Nummern).
3. Soll-Ablauf als Mermaid-Code (flowchart TD), gleiche Schreibweise wie das Ist-Diagramm; markiere neue oder automatisierte Schritte mit ✦.
4. Was der Gesprächspartner dafür tun oder entscheiden muss.
5. Größtes Risiko.

Anforderungen und Ist-Analyse:
{{IST_ANALYSE}}

30 Ideen:
{{IDEEN}}
```

**Prüfen:** Lege Ist- und Soll-Diagramm nebeneinander. Ist der Unterschied in einem Satz erklärbar? Wenn nicht, ist der Vorschlag zu kompliziert.

---

## Schritt 7 · KI: Challenger – bewerten und optimieren

**Wer:** KI als Gegenspieler · **Ergebnis:** bewertete und verbesserte Vorschläge

Jeder Entwurf bekommt einen Gegenspieler. Am besten in einem **neuen Chat**, damit die KI ihre eigenen Vorschläge nicht verteidigt.

```text
{{KONTEXT}}

Du bist ein kritischer Challenger. Deine Aufgabe ist NICHT, die Vorschläge gut zu finden, sondern ihre
Schwächen zu finden, bevor es der Kunde tut.

Für jeden der drei Vorschläge:
1. Inversion: Wie würde dieses Vorhaben in sechs Monaten gescheitert sein? Nenne die drei wahrscheinlichsten Gründe.
2. Welche Annahme ist am wenigsten belegt?
3. Was hat der Berater übersehen (Datenschutz, Akzeptanz im Team, Wartung, Abhängigkeit von einem Anbieter, Kosten nach dem Start)?
4. Bewertung von 1–10 für: Nutzen für den Kunden, Umsetzbarkeit, Risiko (10 = geringstes Risiko).
5. Konkrete Verbesserung, die die größte Schwäche behebt.

Zum Schluss: Welchen Vorschlag würdest du – nach Verbesserung – dem Kunden zuerst zeigen, und warum?

Vorschläge:
{{LOESUNGSVORSCHLAEGE}}

Ist-Analyse zum Abgleich:
{{IST_ANALYSE}}
```

**Prüfen:** Übernimm Verbesserungen bewusst, nicht automatisch. Ein Challenger, der alles schlecht findet, ist genauso wenig hilfreich wie einer, der alles gut findet.

---

## Schritt 8 · Mensch: entscheiden, was weiterverfolgt wird

**Wer:** Mensch – du und/oder der Entscheider auf der anderen Seite · **Ergebnis:** gewählte Lösung bzw. Leistungspakete

Hier entscheidet keine KI. Die KI hat Material geliefert; jetzt wählt ein Mensch, der die Folgen trägt. Dieser Prompt hilft nur, die Entscheidung vorzubereiten:

```text
{{KONTEXT}}

Bereite eine Entscheidungsvorlage auf EINER Seite vor:
- Tabelle der drei (verbesserten) Vorschläge: Nutzen, Umsetzbarkeit, Risiko, was der Kunde beitragen muss.
- Je Vorschlag ein Satz: „Wähle diesen, wenn …“.
- Drei Fragen, die der Entscheider vor der Wahl beantworten sollte.
Triff selbst KEINE Entscheidung.

Material:
{{LOESUNGSVORSCHLAEGE}}
{{CHALLENGER_ERGEBNIS}}
```

**Prüfen:** Halte die Entscheidung schriftlich fest – mit Datum und Begründung in einem Satz. Das ist der Ausgangspunkt für Phase 3.

Weiter: [Phase 3 · Konzept](03-phase-3-concept.md)
