# PMG-Webscrapper

Dieses Open-Source-Projekt bietet einen Webscraper zur Extraktion von Anrufer-Logs aus dem PMG-Portal. Der Scraper automatisiert die Anmeldung, Navigation und den Download von Gesprächshistorie und Gesprächsübersicht als Parquet-Dateien.

## Funktionen

- **Automatische Anmeldung**: Sichere Anmeldung am PMG-Portal mit Umgebungsvariablen.
- **Gesprächshistorie extrahieren**: Lädt Gesprächsdaten vom Vortag aus dem Call Center Bereich.
- **Gesprächsübersicht extrahieren**: Sammelt Übersichtsdaten mit Filtern (Ausgehend, Verpasst, Queue).
- **Parquet-Export**: Speichert Daten in effizientem Parquet-Format für weitere Analyse.
- **Headless-Browser**: Läuft im Hintergrund ohne GUI.
- **Logging**: Detaillierte Logs für Debugging und Überwachung.

## Voraussetzungen

- Python 3.8 oder höher
- Windows (aufgrund der .bat-Scripts; für andere OS anpassen)
- Zugang zum PMG-Portal mit gültigen Anmeldedaten

## Installation

1. **Repository klonen**:
   ```bash
   git clone <repository-url>
   cd pmg-webscrapper
   ```

2. **Abhängigkeiten installieren**:
   Führen Sie das bereitgestellte Script aus:
   ```bash
   install_dependencies.bat
   ```
   Dies erstellt eine virtuelle Umgebung und installiert alle erforderlichen Pakete.

3. **Umgebungsvariablen konfigurieren**:
   Erstellen Sie eine `.env`-Datei im Projektroot mit Ihren PMG-Portal-Zugangsdaten:
   ```
   PMG_PORTAL_USERNAME=IhrBenutzername
   PMG_PORTAL_PASSWORD=IhrPasswort
   PMG_USER=IhrBenutzername
   PMG_PASSWORD=IhrPasswort
   ```
   Alternativ können Sie Dateipfade zu den Credentials angeben (siehe HistorieBot.py).

## Verwendung

### Lokale Ausführung

1. **Script ausführen**:
   ```bash
   run.bat
   ```
   Dies aktiviert die virtuelle Umgebung und startet den Scraper.

2. **Manueller Start**:
   ```bash
   .venv\Scripts\activate
   python src\main.py
   ```

### Docker

1. **Image bauen**:
   ```bash
   docker build -t pmg-scraper .
   ```

2. **Container ausführen**:
   ```bash
   docker run --env-file .env -v /mnt/data:/mnt/data pmg-scraper
   ```
   Stellen Sie sicher, dass das Datenverzeichnis gemountet ist.

## Projektstruktur

```
pmg-webscrapper/
├── src/
│   ├── main.py                 # Haupteinstiegspunkt
│   ├── BaseBot.py              # Abstrakte Basisklasse für Bots
│   ├── HistorieBot.py          # Bot für Gesprächshistorie
│   ├── ÜbersichtBot.py         # Bot für Gesprächsübersicht
│   ├── DokumentenManager.py    # Verwaltet Downloads und Speicherung
│   ├── Util.py                 # Hilfsfunktionen
│   ├── logger.py               # Logging-Konfiguration
│   └── ...                     # Weitere Hilfsdateien
├── requirements.txt            # Python-Abhängigkeiten
├── dockerfile                  # Docker-Konfiguration
├── install_dependencies.bat    # Installationsscript
├── run.bat                     # Ausführungsscript
├── README.md                   # Diese Datei
└── .env                        # Umgebungsvariablen (nicht im Repo)
```

## Ausgaben

Die extrahierten Daten werden in `data/parquet/` gespeichert:
- `Gesprächshistorie/Gesprächshistorie_{YYYY-MM-DD}.parquet`
- `Gesprächsübersicht/Gesprächsübersicht_{YYYY-MM-DD}.parquet`

## Sicherheit

- Verwenden Sie starke Passwörter und speichern Sie Credentials sicher.
- Die `.env`-Datei ist in `.gitignore` ausgenommen – laden Sie sie nicht ins Repository.
- Der Scraper läuft im Headless-Modus für Sicherheit.

## Beitragen

Beiträge sind willkommen! Erstellen Sie Issues für Bugs oder Feature-Requests und Pull-Requests für Verbesserungen.

## Lizenz

Dieses Projekt ist Open-Source. Bitte überprüfen Sie die Lizenzdatei für Details. 
