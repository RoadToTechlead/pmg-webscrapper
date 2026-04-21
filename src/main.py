from playwright.sync_api import sync_playwright
from HistorieBot import HistorieBot
from ÜbersichtBot import Übersicht

def main():
    with sync_playwright() as p:
        slow_mo_value = 500
        browser = p.chromium.launch(headless=True, slow_mo=slow_mo_value)
        context = browser.new_context()
        page = context.new_page()
        print(f"Bot läuft im Headless Modus")

        historieBot = HistorieBot(page)
        übersichtBot = Übersicht(page)

        try:
            historieBot.run()
            übersichtBot.run()
        finally:
            browser.close()

if __name__ == "__main__":
    main()