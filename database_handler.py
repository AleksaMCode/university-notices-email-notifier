import os
from typing import List

from sqlalchemy import Column, Integer, String, Table, create_engine, UniqueConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from oglas import Oglas

Base = declarative_base()


class DatabaseHandler:
    def __init__(self, sqlite_filepath):
        new_table = os.path.exists(sqlite_filepath)
        self.engine = create_engine(f'sqlite:///{sqlite_filepath}', echo=True)
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()

        # Create new table if this is a first time database is created.
        if new_table:
            self.oglasi = Table(
                "oglasi",
                Base.metadata,
                Column("id", Integer, nullable=False, primary_key=True, autoincrement=True),
                Column("ime_predmeta", String),
                Column("date", String),
                Column("title", String),
                Column("content", String),
                Column("attachment_text", String),
                Column("attachment_link", String),
                UniqueConstraint('id')
            )

    def insert(self, oglasi: List[Oglas]):
        self.session.add_all(oglasi)
        self.session.commit()

    def select(self, count: int, year: int):
        return self.session.query(Oglas).filter_by(Oglas.year == year).order_by(Oglas.id.desc()).limit(count)
