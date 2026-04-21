import pandas as pd
import io

class Util:

    def __init__(self, page, logger):
        self.page = page
        self.logger = logger

    def _set_time_filter(self, label):
        try:
            self.logger.info(f"Filtere Zeitraum: {label}...")
            dropdown = self.page.locator('select[name="selDate"]')
            dropdown.select_option(label=label)
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(1000)
        except Exception as e:
            return
        
    def set_time_today(self):
        self._set_time_filter("heute")
    
    def set_time_yesterday(self):
        self._set_time_filter("gestern")
    
    def set_time_current_week(self):
        self._set_time_filter("aktuelle Woche")
    
    def set_time_last_week(self):
        self._set_time_filter("letzte Woche")
        
    def set_time_current_month(self):
        self._set_time_filter("aktueller Monat")
    
    def set_time_last_month(self):
        self._set_time_filter("letzter Monat")

    # Wenn eine neuer Filter von PMG hinzugefügt wird, dann einfach analog der oberen Funktionen erstellen...
    
    # Hilfsfunktion zum Downloaden von von allgemeinen-Files
    def _download_document(self, dateityp, is_sensitive):
        if is_sensitive == True:
            if dateityp == "excel":
                try:
                    with self.page.expect_download() as download_info:
                        self.page.click('img[src="images/icons/xls.gif"]')
                    
                    download = download_info.value
                    
                    # Excel Liste in den Arbeitsspeicher laden und direkt verarbeiten anstatt persistenz zu speichern 
                    with open(download.path(), "rb") as f:
                        file_content = f.read()
                    
                    df = pd.read_excel(io.BytesIO(file_content))
                    df = df.drop(columns=['Teilnehmer', 'Nummer', 'Name'])
                    print(df.head())

                    dateiname = f"../data/processed/anrufübersicht_.parquet"

                    df.to_parquet(dateiname, engine='pyarrow', index=False)
                    self.logger.info("Excel erfolgreich heruntergeladen und verarbeitet")

                except Exception as e:
                    self.logger.info("Download oder Verarbeitung mit Pandas fehlgeschlagen")
                    return
            
            elif dateityp == "pdf":
                self.logger.info("Keine Implementierung für PDFs vorhanden")
                return 
    # Funktion zum Downloaden von Excel-Files
    def download_excel(self):
        self._download_document(dateityp= "excel", is_sensitive=True)

    # Funktion zum Erstellen von PDF-Files
        # nicht vorhanden, da zumindest jetzt noch nicht benötigt
    
    