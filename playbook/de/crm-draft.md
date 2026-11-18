# CRM-Entwurf · Vom Gespräch in den Arbeitsfluss

Ein Transkript wird erst dann produktiv, wenn daraus Arbeit entsteht: eine Aufgabe, ein Lead, eine Verkaufschance (Opportunity). Dieser Prompt erzeugt einen **Entwurf**, den ein Mensch prüft und dann ins CRM überträgt – per Hand, per Import (CSV) oder über eine Automatisierung.

> **Grundsatz: Entwurf statt Autopilot.** Die KI legt nichts selbst an. Sie bereitet vor, du gibst frei. Erst wenn ein Entwurf über Wochen zuverlässig ist, lohnt es sich, den Übertrag zu automatisieren – und auch dann mit einer Freigabe-Stelle.

## Der Prompt

```text
{{KONTEXT}}

Du bist CRM-Assistent. Lies das Transkript und erstelle einen ENTWURF für das CRM.

1. Aufgaben (Tasks)
   Tabelle: Titel | Beschreibung (1 Satz) | Verantwortlich (Rolle) | Fällig (Datum oder „[zu klären]“) | Beleg (Zitat)
   Nur Aufgaben, die im Gespräch zugesagt oder klar vereinbart wurden.

2. Lead / Kontakt
   Felder: Unternehmen (Platzhalter) | Rolle des Ansprechpartners | Branche | Größe | Quelle | Bedarf in einem Satz.

3. Verkaufschance (Opportunity)
   Felder: Name | Phase (z. B. Qualifizierung / Bedarfsanalyse / Angebot) | Bedarf | Entscheider | nächste Aktivität |
   Einschätzung kalt/lau/heiß mit Begründung. KEINE Beträge, KEINE Abschlusswahrscheinlichkeit als Prozentzahl erfinden.

4. Gesprächsnotiz
   5–8 Sätze für die Aktivitäten-Historie des Kontakts.

5. CSV
   Gib die Aufgaben zusätzlich als CSV mit Kopfzeile aus: Subject,Description,Owner,DueDate

Regeln:
- Nichts erfinden. Was im Gespräch nicht vorkam, ist „[zu klären]“.
- Platzhalter aus der Anonymisierung beibehalten; ich ersetze sie erst im CRM.

Transkript:
{{TRANSKRIPT_BEREINIGT}}
```

## Prüfen vor dem Übertrag

- Ist jede Aufgabe wirklich zugesagt worden – oder hat die KI eine gute Idee zur Aufgabe gemacht?
- Stimmen Verantwortliche und Fälligkeiten?
- Platzhalter durch echte Datensätze ersetzen – erst im CRM, nicht im KI-Chat.

## Der Weg zur Automatisierung (für Fortgeschrittene)

Wenn der Entwurf zuverlässig ist, kann eine Automatisierung (z. B. mit n8n, Make, Zapier oder den Bordmitteln deines CRM) die Schritte verbinden: Transkript kommt an → KI erzeugt den Entwurf im Format oben → **ein Mensch gibt frei** → Aufgaben, Lead und Opportunity werden angelegt. Die Freigabe-Stelle ist kein Misstrauen gegen die Technik, sondern Qualitätssicherung: Ein falscher Eintrag im CRM kostet später mehr Zeit als zehn Sekunden Prüfen jetzt.
