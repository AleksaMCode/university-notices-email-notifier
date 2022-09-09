from datetime import datetime
from typing import Tuple


class Oglas:
    ime_predmeta: str
    date: str
    title: str
    content: str
    attachment_text: str
    attachment_link : str

    def __init__(self, oglas: Tuple[str, str, str, str, str, str]):
        self.ime_predmeta = oglas[0]
        self.date = oglas[1]
        self.title = oglas[2]
        self.content = oglas[3]
        self.attachment_text = oglas[5]
        self.attachment_link = oglas[6]
