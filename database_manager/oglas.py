from sqlalchemy import Column, String, Integer
from database_handler import Base


class Oglas(Base):
    __tablename__ = "oglasi"

    subject = Column(String)
    year = Column(Integer)
    date = Column(String)
    title = Column(String)
    content = Column(String)
    attachment_text = Column(String)
    attachment_link = Column(String)
