import pandas as pd
from DokumentTyp import DokumentTyp
from InternalExcelName import InternalExcelName
from ExcelTyp import ExcelTyp
from pathlib import Path
from logger import BotLogger

ROOT_DIR = Path(__file__).resolve().parent.parent

class DokumentenManager:

    def __init__(self, page, dokument_name, is_sensitive=False):
        self.page = page
        self.logger = BotLogger.get_logger()
        self.dokument_name = dokument_name
        self.is_sensitive = is_sensitive

    def _perform_download(self, dateityp):
        """
        Hilfsmethode: erledigt den Download
        """
        try:    
            with self.page.expect_download() as download_info:
                self.page.click(dateityp.value)
            return download_info.value
        except:
            self.logger.error("Download fehlgeschlagen")
            return None
    
    def _save_document(self, doc_type: DokumentTyp):
        download = self._perform_download(doc_type)

        if not download:
            return
        if self.is_sensitive == True:
            if doc_type == DokumentTyp.EXCEL:
                self._process_senstive_excel(download)
            
            elif doc_type == "pdf":
                self.logger.error("Keine Implementierung für PDFs vorhanden")
                return         

    def _process_senstive_excel(self,download):
        try:
            url_ = self._get_download_url(download)
            self.logger.info(f"{url_}.")
            if url_ is None:
                self.logger.error("Name konnte nicht gefunden werden.")

            config = InternalExcelName.find_by_url(url_)

            if config is None: 
                self.logger.error(f"Keine Konfiguration für {url_} gefunden. Verarbeitung wird abgebrochen.")
                return
            
            self.logger.info(f"Regex-Match: '{url_} erkannt als '{config.interner_name}'.")
            
            df = pd.read_excel(download.path())

            cols_to_drop = ExcelTyp.COLUMN_CLEANUP.value.get(config.interner_name, [])

            existing_cols_to_drop = [c for c in cols_to_drop if c in df.columns]

            if existing_cols_to_drop:
                df.drop(columns=existing_cols_to_drop, inplace=True)
                self.logger.info(f"Folgende sensible Spalten wurden entfernt: {existing_cols_to_drop}")

            full_path = ROOT_DIR / self.dokument_name
            full_path.parent.mkdir(parents=True, exist_ok=True)

            df.to_parquet(str(full_path), engine='pyarrow', index=False)
            self.logger.info("Excel erfolgreich heruntergeladen und verarbeitet")

        except Exception as e:
            self.logger.error(f"Fehler bei der Parquet-Verarbeitung: {e}")

    def save_excel(self):
        self._save_document(doc_type=DokumentTyp.EXCEL)

    def _get_suggested_name(self, download):
        """
        Extrahiert den Namen des gedownloadeten Objektes.
        """        
        return download.suggested_filename 
    
    def _get_download_url(self, download):
        return download.url
    
    def mapping_documents_name_to_excel_typ(self):
        return
