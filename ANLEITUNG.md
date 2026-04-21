# Anleitung für PMG-Webscrapper

Diese Anleitung führt Sie Schritt für Schritt durch die Installation und Ausführung des PMG-Webscrappers.

## Schritt 1: Vorbereitung

### 1.1 Repository herunterladen
- Klonen Sie das Repository oder laden Sie den Code herunter.
- Navigieren Sie in den Projektordner: `cd pmg-webscrapper`

### 1.2 Python installieren
- Stellen Sie sicher, dass Python 3.8+ installiert ist.
- Überprüfen Sie mit: `python --version`

### 1.3 PMG-Portal Zugang
- Sie benötigen gültige Anmeldedaten für das PMG-Portal (portal.pmg.ag).
- Notieren Sie Ihren Benutzernamen und Passwort.

## Schritt 2: Installation

### 2.1 Abhängigkeiten installieren
- Doppelklicken Sie auf `install_dependencies.bat` oder führen Sie es in der Kommandozeile aus:
  ```
  install_dependencies.bat
  ```
- Dies erstellt eine virtuelle Umgebung (`.venv`) und installiert alle Pakete aus `requirements.txt`.

### 2.2 Umgebungsvariablen einrichten
- Erstellen Sie eine neue Datei namens `.env` im Projektroot.
- Fügen Sie Ihre Zugangsdaten hinzu:
  ```
  PMG_PORTAL_USERNAME=IhrBenutzername
  PMG_PORTAL_PASSWORD=IhrPasswort
  PMG_USER=IhrBenutzername
  PMG_PASSWORD=IhrPasswort
  ```
- **Wichtig**: Diese Datei nicht ins Git-Repository hochladen!

## Schritt 3: Ausführung

### 3.1 Lokaler Start
- Doppelklicken Sie auf `run.bat` oder führen Sie es aus:
  ```
  run.bat
  ```
- Alternativ manuell:
  1. Virtuelle Umgebung aktivieren: `.venv\Scripts\activate`
  2. Script starten: `python src\main.py`

### 3.2 Docker (optional)
- Image bauen: `docker build -t pmg-scraper .`
- Container starten: `docker run --env-file .env -v C:\Pfad\zu\data:/mnt/data pmg-scraper`
- Passen Sie den Pfad zum Datenverzeichnis an.

## Schritt 4: Überprüfung

### 4.1 Logs prüfen
- Während der Ausführung werden Logs in der Konsole angezeigt.
- Erfolgreiche Ausführung zeigt: "Bot-Durchlauf erfolgreich beendet."

### 4.2 Daten prüfen
- Nach der Ausführung finden Sie die Parquet-Dateien in `data/parquet/`.
- Verwenden Sie Tools wie Python Pandas oder Excel zum Öffnen.

## Schritt 5: Fehlerbehebung

### Häufige Probleme:
- **Login fehlgeschlagen**: Überprüfen Sie die `.env`-Datei auf korrekte Credentials.
- **Module nicht gefunden**: Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist.
- **Browser-Fehler**: Playwright könnte Chromium neu installieren müssen: `playwright install chromium`

### Logs analysieren:
- Detaillierte Fehler in den Konsolen-Logs.
- Bei anhaltenden Problemen: Issues im Repository erstellen.

## Schritt 6: Anpassungen (fortgeschrittene Nutzer)

### Zeitraum ändern:
- In `Util.py` die `set_time_yesterday()` Methode anpassen für andere Daten.

### Neue Bots hinzufügen:
- Erben Sie von `BaseBot` und implementieren Sie `login()` und `run()`.

### Filter anpassen:
- In `ÜbersichtBot.py` die Filter-Methoden modifizieren.

Bei Fragen oder Problemen konsultieren Sie die README.md oder erstellen Sie ein Issue.