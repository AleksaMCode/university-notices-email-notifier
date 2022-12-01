from typing_extensions import TypedDict


class Settings(TypedDict):
    website: str = "https://efee.etf.unibl.org/oglasi/"
    latest_fetch: str = ""
    web_driver: str = "CHROME"
