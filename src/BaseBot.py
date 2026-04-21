from abc import ABC, abstractmethod
from playwright.sync_api import Page
from logger import BotLogger

class BaseBot(ABC):
    def __init__(self, page: Page):
        self.page = page
        self.logger = BotLogger.get_logger(self.__class__.__name__)

    def get_url(self):
        current_url = self.page.url
        self.logger.debug(f"Aktuelle Position: {current_url}")
        return current_url

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def run(self):
        pass