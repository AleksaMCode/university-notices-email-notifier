from sqlalchemy import Column, String


class Oglas:
    __tablename__ = "oglasi"

    ime_predmeta = Column(String)
    date = Column(String)
    title = Column(String)
    content = Column(String)
    attachment_text = Column(String)
    attachment_link = Column(String)
