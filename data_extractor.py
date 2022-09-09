from oglas import Oglas
from web_driver import WebDriver
from bs4 import BeautifulSoup
from datetime import datetime


class DataExtractor:
    web_driver: WebDriver
    soup: BeautifulSoup
    latest_read_time: datetime

    def __init__(self, web_driver, latest_read_time: str):
        self.web_driver = web_driver
        self.latest_read_time = datetime.strptime(latest_read_time, '%d/%m/%y %H:%M:%S')
        self.soup = BeautifulSoup(self.web_driver.page_source, "html.parser")
        ulist = self.soup.find('ul', id='ul_id_1')
        self.oglasi = ulist.find_all('li')

    def get_oglasi(self):
        oglasi_list = []
        oglas_info = []
        for oglas in self.oglasi:
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
        oglasi_list.insert(Oglas(oglas_info))

        return oglasi_list
