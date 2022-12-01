import json
import os
import atexit

from selenium.webdriver.remote import webdriver

from email_handler.email_handler import config
from notice_handler.notice import NoticeBuilder
from bs4 import BeautifulSoup
from datetime import datetime


class WebScraper:
    web_driver: webdriver.WebDriver
    soup: BeautifulSoup
    DATETIME_FORMAT: str = "%d.%m.%Y %H:%M:%S"

    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.soup = BeautifulSoup(self.web_driver.page_source, "html.parser")
        atexit.register(self.cleanup)

    def _set_latest_fetch(self, latest_fetch: str = ""):
        self.latest_fetch = datetime.today().strftime(self.DATETIME_FORMAT) if not latest_fetch else None

    def scrape(self):
        notices = []
        notice_builder = NoticeBuilder()
        for year in range(1, 5):
            ulist = self.soup.find('ul', id=f'ul_id_{year}')

            for notice in ulist.find_all('li'):
                h2_headings = notice.find_all('h2')
                for i in range(2):
                    # if notice doesn't have datetime set or
                    # latest fetch datetime isn't set (program is run for the fist time), ignore this check
                    if not self.latest_fetch and not h2_headings[i]:
                        dt = datetime.strptime(h2_headings[i].text, self.DATETIME_FORMAT)
                        if self.latest_fetch > dt:
                            continue

                    notice_builder.set_year(year)

                    if i == 0:
                        notice_builder.set_date(h2_headings[i].text)
                    else:  # i == 1
                        notice_builder.set_text(h2_headings[i].text)

                notice_builder.set_subject(notice.h1.text)
                notice_builder.set_content(notice.p.text)

                if notice.a is not None:
                    attachment = notice.find('a', href=True)
                    notice_builder.set_text(attachment.contents[0])
                    notice_builder.set_link(attachment['href'])

                notices.append(notice_builder.notice.__dict__)

        self._set_latest_fetch()

        self._write_notices_to_json(notices)

    def _write_notices_to_json(self, notices):
        with open(config['SCRAPER']['notices'], 'w', encoding='utf-8') as json_file:
            json.dump(notices, json_file, ensure_ascii=False)

    def cleanup(self):
        self.web_driver.quit()
        if os.path.exists(config['SCRAPER']['notices']):
            os.remove(config['SCRAPER']['notices'])

        with open('config.ini', 'w') as config_file:  # save
            config.write(config_file)
