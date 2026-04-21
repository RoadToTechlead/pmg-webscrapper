from enum import Enum

class ExcelTyp(Enum):
    COLUMN_CLEANUP = {
        "Gespraechshistorie": ['Teilnehmer', 'Anrufername', 'Nummer'],
        "Gespraechsuebersicht": ['Teilnehmer', 'Name', 'Nummer']
}