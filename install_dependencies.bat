@echo off
echo [1/5] Erstelle virtuelle Umgebung...
if not exist .venv (
    python -m venv .venv
) else (
    echo Virtuelle Umgebung bereits vorhanden. Überspringe Erstellung.
)

echo [2/5] Aktiviere Umgebung und aktualisiere Pip...
call .venv\Scripts\activate
python -m pip install --upgrade pip

echo [3/5] Installiere Anforderungen aus requirements.txt...
pip install -r requirements.txt

echo [4/5] Installiere Playwright Browser (Chromium)...
playwright install chromium

echo[5/5] Erstelle .env Datei aus Vorlage...
if not exist ".env" (
    if exist ".env.example" (
        copy .env.example .env
        echo .env wurde erfolgreich aus .env.example erstelle.
        echo BITTE VERGISS NICHT, DEINE ZUGANGSDATEN IN DER .env EINZUTRAGEN!
    ) ELSE (
        echo Warnung: .env.example wurde nicht gefunden. Erstelle leere .env
        echo PMG_USER >> .env
        echo PMG_PASSWORD >> .env
    )
) else (
    echo .env Datei existiert bereits. Bestehende Werte wurden nicht überschrieben.
)

echo.
echo Fertig! Alle Abhaengigkeiten wurden installiert.
pause