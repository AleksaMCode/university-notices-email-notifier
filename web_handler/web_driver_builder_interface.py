from enum import Enum
from abc import ABCMeta, abstractmethod


class DriverType(Enum):
    CHROME = 1
    FIREFOX = 2
    EDGE = 3
    CHROMIUM = 4
    BRAVE = 5
    OPERA = 6
    INTERNET_EXPLORER = 7


class IWebDriverBuilder(metaclass=ABCMeta):
    """
    WebDriver Builder Interface
    """

    @property
    @abstractmethod
    def web_driver(self) -> None:
        pass

    @abstractmethod
    def set_driver_type(self, driver_type: DriverType) -> None:
        pass

    @abstractmethod
    def set_url(self, url: str) -> None:
        pass
