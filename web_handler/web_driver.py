from enum import Enum
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


class DriverType(Enum):
    CHROME = 1
    FIREFOX = 2
    EDGE = 3
    CHROMIUM = 4
    BRAVE = 5
    OPERA = 6
    INTERNET_EXPLORER = 7


class WebDriver:
    driver: webdriver.WebDriver
    driver_type: DriverType
    website_path: str

    def __init__(self, driver_type, website_path):
        self.driver_type = driver_type
        self.website_path = website_path
        self._initialize()

    def _initialize(self):
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        self._set_chrome_driver(options)

    def _set_chrome_driver(self, options):
        if self.driver_type is DriverType.CHROME:
            self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        elif self.driver_type is DriverType.FIREFOX:
            self.driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
        elif self.driver_type is DriverType.EDGE:
            self.driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        elif self.driver_type is DriverType.CHROMIUM:
            self.driver = webdriver.Chrome(options=options, service=ChromiumService(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        elif self.driver_type is DriverType.BRAVE:
            self.driver = webdriver.webdriver.Chrome(options=options, service=BraveService(
                ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
        elif self.driver_type is DriverType.OPERA:
            self.driver = webdriver.Opera(options=options, executable_path=OperaDriverManager().install())
        elif self.driver_type is DriverType.INTERNET_EXPLORER:
            self.driver = webdriver.Ie(options=options, service=IEService(IEDriverManager().install()))

        self.driver.get(self.website_path)
