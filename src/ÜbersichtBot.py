from BaseBot import BaseBot
import os
from dotenv import load_dotenv
from Util import Util
from DokumentenManager import DokumentenManager
from datetime import datetime, timedelta

load_dotenv()

class Übersicht(BaseBot):
    def login(self):
        self.logger.info("Starte Login-Prozess auf portal.pmg.ag")
        user = os.getenv("PMG_USER")
        pw = os.getenv("PMG_PASSWORD")

        if not user or not pw:
            self.logger.error("Zugangsdaten in .env fehlen!")
            raise ValueError("Credentials missing")
        
        self.page.goto("https://portal.pmg.ag/")
        self.page.fill("#usernameField", user)
        self.page.fill('input[name="password"]', pw)
        self.page.get_by_role("button", name="Login").click()

        self.page.wait_for_load_state("networkidle")
        self.logger.info("Login erfolgreich.")

    def aktiviere_alle_filter(self):
        self.filter_ausgehend_aktivieren()
        self.filter_verpasst_aktivieren()
        self.filter_queue_aktivieren()
        self.logger.info("Alle Filter wurden aktiviert.")
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    def filter_ausgehend_aktivieren(self):
        self.logger.info("Prüfe Zustand des Filters 'Ausgehend'")
        self.page.get_by_role("button", name="Ausgehend").click()    
        self.logger.info("Filter 'Ausgehend' gefunden und angeklickt")
    
    def filter_verpasst_aktivieren(self):
        self.logger.info("Prüfe Zustand des Filters 'Verpasst'")
        self.page.get_by_role("button", name="Verpasst").click()
        self.logger.info("Filter 'Ausgehend' gefunden und angeklickt")

    def filter_queue_aktivieren(self):
        self.logger.info("Prüfe Zustand des Filters 'Queue'")
        self.page.get_by_role("button", name="Queue").click()
        self.logger.info("Filter 'Ausgehend' gefunden und angeklickt")

    def run(self):
        try:
            # Anmeldung
            if "login" in self.get_url():
                self.login()

            # Navigiere zur richtigen Stelle
            self.page.get_by_text("Verwaltung (inTime Express Logistik GmbH)").click()
            übersicht_nav = self.page.locator('span.x-tree-node-text', has_text="Gesprächsübersicht")
            übersicht_nav.wait_for(state="visible")
            übersicht_nav.click()
 
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(1000)
            self.logger.info("Auf Reiter Gespraechsübersicht geklickt")

            # Filter setzen
            self.aktiviere_alle_filter()
            
            # nach Gestern filtern
            util = Util(self.page, self.logger)
            util.set_time_yesterday()

            gestern_datum = datetime.now() - timedelta(days=1)
            datum_string = gestern_datum.strftime("%Y-%m-%d")

            dokument_name = f"data/parquet/Gesprächsübersicht/Gesprächsübersicht_{datum_string}.parquet"
            dokument = DokumentenManager(self.page, dokument_name, is_sensitive=True)
            dokument.save_excel() 
        
        except Exception as e:
            self.logger.error(f"Kritischer Fehler im Bot-Ablauf: {e}")
            raise


