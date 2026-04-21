from BaseBot import BaseBot
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from Util import Util
from DokumentenManager import DokumentenManager

load_dotenv()

class HistorieBot(BaseBot):

    def load_secret_from_path_var(self, env_var_name):
        file_path = os.getenv(env_var_name)

        if file_path and os.path.exists(file_path):
            with open(file_path, 'r') as secret_file:
                return secret_file.read().strip()
        else:
            return os.getenv(env_var_name)
            
    def login(self):
        self.logger.info("Starte Login-Prozess auf portal.pmg.ag")
        user = self.load_secret_from_path_var("PMG_PORTAL_USERNAME")
        pw = self.load_secret_from_path_var("PMG_PORTAL_PASSWORD")
        
        if not user or not pw:
            self.logger.error("Zugangsdaten in .env fehlen!")
            raise ValueError("Credentials missing")

        self.page.goto("https://portal.pmg.ag/")
        self.page.fill("#usernameField", user)
        self.page.fill('input[name="password"]', pw)
        self.page.get_by_role("button", name="Login").click()
        
        self.page.wait_for_load_state("networkidle")
        self.logger.info("Login erfolgreich.")

    def run(self):
        try:
            self.login()
            self.logger.info("Navigiere zum Call Center Bereich...")
            self.page.get_by_text("Call Center (inTime Express Logistik GmbH)").click()
            
            historie_nav = self.page.locator('span.x-tree-node-text', has_text="Gesprächshistorie")
            
            historie_nav.wait_for(state="visible")
            historie_nav.click()
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(1000)
            self.logger.info("Auf Reiter Gespraechshistorie geklickt")

            helper = Util(self.page, self.logger)
            helper.set_time_yesterday()

            print("Warte 5 Sekunden, damit die Tabelle geladen wird...")
            self.page.wait_for_timeout(5000)

            self.logger.info("Filtere Zeitraum: Gestern...") #Datum des gestrigen Tages berechnen und Excel-File danach benennen
            self.zeitstempel = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.logger.info("Starte Excel-Download...")

            gestern_datum = datetime.now() - timedelta(days=1)
            datum_string = gestern_datum.strftime("%Y-%m-%d")

            try:
                dokument_name = f"data/parquet/Gesprächshistorie/Gesprächshistorie_{datum_string}.parquet"
                dokument = DokumentenManager(self.page, dokument_name, is_sensitive=True)
                dokument.save_excel()
            
                self.logger.info("Bot-Durchlauf erfolgreich beendet.")
            except Exception as e:
                self.logger.error(f"Fehler im Bot-Ablauf: {e}")
                raise
            
            """
            In der Regel sollte der Bot damit weiter machen, dass er die Excel-Liste aus der Gesprächsübersicht im Bereich "Verwaltung (InTime Express Logistik) 
            extrahiert. Wenn der Bot bereits registriert ist, ist kein login()-Aufruf nötig. Geprüft wird dies mit einer if-Abfrage über den derzeitigen Link.
            """
            
        except Exception as e:
            self.logger.error(f"Kritischer Fehler im Bot-Ablauf: {e}")
            raise