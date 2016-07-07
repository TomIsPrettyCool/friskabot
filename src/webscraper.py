from bs4 import BeautifulSoup
import requests
import threading
import time
import json
from models import Orders


class GetSoup:
    friskamenu = "http://www.friskafood.com/menu-ie?m=hotlunch"

    def __init__(self):
        http = requests.get(self.friskamenu, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'})

        self.soup = BeautifulSoup(http.text, 'html.parser')
        self.table = self.soup.find_all('table')[2]
        self.rows = self.table.find_all('td', 'menu_item')

    def extract_backround(self):
        thread = threading.Thread(target=self._soup_to_list())
        thread.daemon = True
        thread.start()
        return

    def _soup_to_list(self):
        """
        Returns an array of soup
        """
        while True:
            self.soups = []

            for row in self.rows:
                self.soups.append(row.get_text())
            print str(self.soups)
            self.cache_soup()
            time.sleep(3600)  # Run once an hour

    def cache_soup(self):

        with open('soups.json', 'wb') as soupcache:
            json.dump(self.soups, soupcache)

