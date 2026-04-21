from enum import Enum
import re

class InternalExcelName(Enum):
    GESPRAECHSHISTORIE = (r"historie", "Gespraechshistorie", r"QueueCallHistorieGrid")
    GESPRAECHSUEBERSICHT = (r".bersicht", "Gespraechsuebersicht", r"CallsOverviewGrid")

    @classmethod
    def find_by_filename(cls, filename):
        for member_ in cls:
            pattern = member_.value[0]
            if re.search(pattern, filename, re.IGNORECASE):
                return member_
        return None
    
    @classmethod
    def find_by_url(cls, url):
        """
        Sucht den internen Namen basierend auf der Download_Url.
        """
        for member in cls:
            url_pattern = member.value[2]
            if re.search(url_pattern, url, re.IGNORECASE):
                return member

    @property
    def interner_name(self):
        return self.value[1]
    