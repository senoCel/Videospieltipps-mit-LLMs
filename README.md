# OpenLLM-Project
Erstellt mit Python 3.14

## Beschreibung
Repository für ein OpenLLM Projekt, welches sich mit der Generierung von Tipps zu verschiedenen Videospielen beschäftigt.

Arbeitsschritte: 
- Prompts ausdenken/aussuchen und optimieren (Beide)
- Persönlicher Goldstandard (Senem) 
- System laufen lassen (Niklas)
- Ergebnisse evaluieren (Beide)

## Modelle
- [mistral:7b](https://ollama.com/library/mistral:7b) 
- [falcon3:7b](https://ollama.com/library/falcon3) -> Stand 28.11 1. im Open LLM Leaderboard bei Modellen bis zu 7 Milliarden Parametern 
- [llama3.1:8b](https://ollama.com/library/llama3.1:8b)
- [qwen2.5:7b](https://ollama.com/library/qwen2.5:7b)
- [deepseek-r1:8b](https://ollama.com/library/deepseek-r1:8b)

## Games
- Assassins Creed Shadows
- Assassins Creed Origins
- Minecraft
- EA Sports FC / Fifa
- Need for Speed
- GTA V
- Mario Bros
- Rocket League
- CSGO
- Die Sims

## Erwartungen
- passender Output relativ zum Spiel -> sinnvoll
- unterschiedlicher aber hilfreicher Output -> unterschiedliche Schwerpunkte
- LLM passt sich an Spielsituationen an -> unterschiedlicher Spielerfortschritt
- LLM erkennt Erfahrungsgrad

## Prompts
### Spielübergreifende Prompts 
### Zielgruppenspezifische Prompts 
### Situationsbedingte Prompts 

### Situationen
- von Spiel abhängig
- brenzlige Situationen -> unbedingte Hilfe nötig

### Zielgruppen
- Anfänger:in
- Erfahrene:r Spieler:innen
- verschiedene Konsolen
- Altersgruppen
  -> zB. Test, ob Kleinkind Tipps für GTA bekommt -> FSK unterschreitet

## Chats

## Ergebnisse

### Bewertungskriterien

1. Korrektheit der Informationen

- Stimmen die Tipps nachweislich mit dem Spielinhalt überein?

2. Relevanz zum Spiel und zur Frage

- Passt der Tipp konkret zum genannten Spiel, Modus, Level oder Problem?

3. Praktischer Nutzen

- Hilft der Tipp tatsächlich beim Weiterkommen?
- Ist er spielerisch umsetzbar und nicht nur theoretisch?

4. Klarheit und Verständlichkeit

- Ist der Tipp klar formuliert?
- Wird erklärt, wie man etwas machen soll?

5. Fundierte Analyse

- Geht der Tipp auf Spielmechaniken oder Gegnerverhalten ein?

6. Anpassungsfähigkeit

- Bezieht der Tipp mögliche Variationen ein (z. B. unterschiedliche Spielstile)?
- Wird der Kontext des Nutzers (z. B. Anfänger vs. Fortgeschrittener) berücksichtigt?
- Wird die Situation der Spieler:innen berücksichtigt?
