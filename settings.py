from typing_extensions import TypedDict


class Settings(TypedDict):
    website: str = "https://efee.etf.unibl.org/oglasi/"
    database_name: str = "etfbl_oglasi.db"
    last_fetch: str = ""
    web_driver: str = "edge"
    fetch_interval: str = "60"
    db_interval: str = "30"
    preview_count: str = "10"
