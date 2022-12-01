from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as BraveService
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.core.utils import ChromeType

from web_handler.web_driver_builder_interface import IWebDriverBuilder, DriverType


class WebDriverBuilder(IWebDriverBuilder):
    _driver_type: DriverType
    _url: str
    _options: Options

    def __init__(self) -> None:
        self._reset()

    def _reset(self) -> None:
        self._driver_type = None
        self._url = None

    @property
    def web_driver(self) -> None:
        self._set_options()
        web_driver = self._set_driver()
        web_driver.get(self._url)
        self._reset()
        return web_driver

    def set_driver_type(self, driver_type: DriverType) -> None:
        self._driver_type = driver_type

    def set_url(self, url: str) -> None:
        self._url = url

    def _set_options(self):
        self._options = Options()
        self._options.headless = True
        self._options.add_argument("--window-size=1920,1200")  # TODO: Maybe remove this?

    def _set_driver(self):
        match self._driver_type:
            case DriverType.CHROME:
                return webdriver.Chrome(options=self._options, service=ChromeService(ChromeDriverManager().install()))
            case DriverType.FIREFOX:
                return webdriver.Firefox(options=self._options, service=FirefoxService(GeckoDriverManager().install()))
            case DriverType.EDGE:
                return webdriver.Edge(options=self._options, service=EdgeService(EdgeChromiumDriverManager().install()))
            case DriverType.CHROMIUM:
                return webdriver.Chrome(options=self._options, service=ChromiumService(
                    ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
            case DriverType.BRAVE:
                return webdriver.webdriver.Chrome(options=self._options, service=BraveService(
                    ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
            case DriverType.OPERA:
                return webdriver.Opera(options=self._options, executable_path=OperaDriverManager().install())
            case DriverType.INTERNET_EXPLORER:
                return webdriver.Ie(options=self._options, service=IEService(IEDriverManager().install()))
