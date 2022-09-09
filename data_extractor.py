from oglas import Oglas
from web_driver import WebDriver
from bs4 import BeautifulSoup
from datetime import datetime


class DataExtractor:
    web_driver: WebDriver
    soup: BeautifulSoup
    last_fetch: datetime

    def __init__(self, web_driver, last_fetch: str):
        self.web_driver = web_driver
        self.last_fetch = datetime.strptime(last_fetch, '%d/%m/%y %H:%M:%S')
        self.soup = BeautifulSoup(self.web_driver.page_source, "html.parser")

    def get_oglasi(self):
        oglasi_list = []
        oglas_info = []
        for year in range(1, 5):
            ulist = self.soup.find('ul', id=f'ul_id_{i}')

            for oglas in ulist.find_all('li'):
                h2_headings = oglas.find_all('h2')
                for i in range(2):
                    if h2_headings[i] is not "":
                        dt = datetime.strptime(h2_headings[i].text, '%d/%m/%y %H:%M:%S')
                        if self.latest_read_time > dt:
                            continue
                    oglas_info.insert(h2_headings[i].text)

                oglas_info.insert(oglas.h1.text)
                oglas_info.insert(oglas.p.text)
                if oglas.a is not None:
                    attachment = oglas.find('a', href=True)
                    oglas_info.insert(attachment.contents[0])
                    oglas_info.insert(attachment['href'])
                else:
                    oglas_info.insert("")
                    oglas_info.insert("")
            oglasi_list.insert(
                Oglas(ime_predmeta=oglas_info[2], year=year, date=oglas_info[0], title=oglas_info[1],
                      content=oglas_info[3], attachment_text=oglas_info[4], attachment_link=oglas_info[5]))

        return oglasi_list
