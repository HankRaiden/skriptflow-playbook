# 00 · Vorbereitung: Einwilligung, Anonymisierung, Kontext

Bevor ein einziges Wort an eine KI geht, kommen drei Dinge. Sie dauern zusammen zehn Minuten und schützen dich, deinen Gesprächspartner und das Ergebnis.

## 1. Einwilligung vor der Aufnahme

In Deutschland ist das heimliche Aufzeichnen eines nicht öffentlich gesprochenen Wortes strafbar (§ 201 StGB). Außerdem sind Gesprächsinhalte fast immer personenbezogene Daten im Sinne der DSGVO. Deshalb:

- **Vorher fragen, nicht nachher.** Am besten schon in der Termineinladung, und zu Beginn des Gesprächs noch einmal mündlich.
- **Zweck nennen.** „Ich zeichne auf, damit ich nichts vergesse und dir danach eine Zusammenfassung und ein Ablaufdiagramm schicken kann.“
- **Nein heißt nein.** Dann schreibst du mit und nutzt deine Notizen als „Transkript“. Das Verfahren funktioniert trotzdem, nur gröber.
- **Werkzeug prüfen.** Wo speichert das Aufnahme-Tool die Daten? Gibt es einen Auftragsverarbeitungsvertrag (AVV)? Das ist eine Frage für deinen Datenschutzbeauftragten, nicht für dieses Playbook.

Muster für die Einladung:

```text
Kurzer Hinweis zum Termin: Ich würde unser Gespräch gerne aufzeichnen und transkribieren lassen,
damit ich mich voll auf dich konzentrieren kann und nichts verloren geht. Danach bekommst du von mir
eine Zusammenfassung und ein Bild deines aktuellen Ablaufs zur Bestätigung. Die Aufnahme nutze ich nur
für diesen Zweck und lösche sie, wenn wir fertig sind. Wenn dir das nicht recht ist, sag einfach
Bescheid – dann schreibe ich klassisch mit.
```

> Keine Rechtsberatung. Prüfe die Regeln deines Landes, deines Unternehmens und deines Werkzeugs selbst.

## 2. Anonymisieren, bevor die KI es sieht

Ersetze Namen, Firmen, Orte, Telefonnummern, E-Mail-Adressen, Preise und alles, was eine Person erkennbar macht, durch Rollen und Platzhalter. Die KI braucht für die Analyse keine echten Namen. Du kannst die Zuordnung für dich behalten.

```text
Du bist ein sorgfältiger Datenschutz-Assistent.

Aufgabe: Anonymisiere das folgende Transkript, bevor es weiterverarbeitet wird.
- Ersetze Personennamen durch Rollen in eckigen Klammern, z. B. [Geschäftsführer], [Vertriebsleiterin], [Ich].
- Ersetze Firmennamen durch [Unternehmen A], [Kunde B], [Lieferant C] usw. Gleiche Namen bekommen immer denselben Platzhalter.
- Ersetze Orte, Telefonnummern, E-Mail-Adressen, Webseiten, Kunden- und Auftragsnummern durch [Ort], [Telefon], [E-Mail] usw.
- Ersetze konkrete Geldbeträge durch [Betrag].
- Ändere sonst NICHTS: keine Kürzung, keine Umformulierung, keine Korrektur.
- Gib am Ende eine Tabelle „Original → Platzhalter“ aus, die ich lokal behalte und NICHT weitergebe.

Transkript:
{{TRANSKRIPT}}
```

> Wichtig: Wenn du schon diesen Schritt einer Cloud-KI gibst, hat die Cloud-KI die Originaldaten gesehen. Für sensible Gespräche anonymisiere von Hand (Suchen & Ersetzen) oder mit einem lokal laufenden Modell.

## 3. Der Kontext-Block

Jeder Prompt in diesem Playbook beginnt mit demselben Kontext-Block. Fülle ihn einmal aus und kopiere ihn immer mit. So weiß die KI in jedem Schritt, worum es geht.

```text
KONTEXT
- Wer bin ich: {{deine Rolle, z. B. „Berater für Prozessautomatisierung“, „Vertriebsleiter“, „Salesforce-Admin“}}
- Mit wem war das Gespräch: {{Rolle des Gesprächspartners, Branche, Größe – ohne Namen}}
- Art des Gesprächs: {{Erstgespräch / Strategiegespräch / Schulung / internes Meeting}}
- Ziel des Gesprächspartners: {{in einem Satz, so wie er es gesagt hat}}
- Mein Ziel: {{z. B. „sein Problem verstehen und drei Lösungswege vorschlagen“}}
- Sprache und Ton der Ergebnisse: {{z. B. Deutsch, Du-Form, einfache Worte, keine Fachbegriffe ohne Erklärung}}
```

## Arbeitsweise

- **Ein Gespräch = ein Chat** (oder ein Projekt in deiner KI). So bleiben die Ergebnisse früherer Schritte im Kontext und du musst sie nicht jedes Mal neu einfügen.
- **Jeden Schritt prüfen**, bevor du den nächsten startest. Die KI baut auf ihren eigenen Fehlern weiter, wenn du sie nicht stoppst.
- **Ergebnisse speichern** – als Markdown-Datei pro Schritt. Am Ende hast du eine nachvollziehbare Akte.

Weiter: [Phase 1 · Ist-Analyse](01-phase-1-current-state.md)
