from email_handler.email_handler import send_email, config
from web_handler.web_scraper import WebScraper
from web_handler.web_driver import WebDriverBuilder, DriverType

if __name__ == '__main__':
    driver_builder = WebDriverBuilder()
    driver_builder.set_driver_type(DriverType[config['SCRAPER']['web_driver'].upper()])
    driver_builder.set_url(config['SCRAPER']['website'])
    WebScraper(driver_builder.web_driver).scrape()
    send_email()
