import os
from datetime import datetime, timedelta
from typing import List

from sqlalchemy import Column, Integer, String, Table, create_engine, UniqueConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from oglas import Oglas

Base = declarative_base()


class DatabaseHandler:
    DATETIME_FORMAT: str = "%d/%m/%y %H:%M:%S"

    def __init__(self, sqlite_filepath: str, db_interval: str):
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
                Column("subject", String),
                Column("year", Integer),
                Column("date", String),
                Column("title", String),
                Column("content", String),
                Column("attachment_text", String),
                Column("attachment_link", String),
                UniqueConstraint('id')
            )

        self.clean(db_interval)

    def clean(self, db_interval):
        rows = self.select_all()
        for row in rows:
            dt = datetime.strptime(row.date, self.DATETIME_FORMAT)
            now = datetime.datetime.now()
            diff = now - dt
            if diff > datetime.timedelta(hours=int(db_interval) * 24):
                self.session.delete(row)

    def insert(self, oglasi: List[Oglas]):
        self.session.add_all(oglasi)
        self.session.commit()

    def select_all(self):
        return self.session.query(Oglas).all()

    def select(self, count: int, year: int):
        return self.session.query(Oglas).filter_by(Oglas.year == year).order_by(Oglas.id.desc()).limit(count)

    def select(self, count: int, subject: str):
        return self.session.query(Oglas).filter_by(Oglas.subject == subject).order_by(Oglas.id.desc()).limit(count)

    def select(self, count: int, subject: str, year: int):
        return self.session.query(Oglas).filter(Oglas.subject.like(subject), Oglas.year.like(year)) \
            .order_by(Oglas.id.desc()).limit(count)
