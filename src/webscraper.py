from bs4 import BeautifulSoup
import urllib2
from models import *


class GetSoup:
    friskamenu = "http://www.friskafood.com/menu-ie?m=hotlunch"

    def __init__(self):
        # http = requests.get(self.friskamenu, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'})
        request = urllib2.Request(self.friskamenu, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'})
        html = urllib2.urlopen(request).read()

        self.soup = BeautifulSoup(html, 'html.parser')
        self.table = self.soup.find_all('table')[2]
        self.rows = self.table.find_all('td', 'menu_item')

    def soup_to_list(self):
        soups = []

        for row in self.rows:
            soups.append(row.get_text())
        print str(soups)
        self.cache_soup(soups)
        #  Run once an hour

    def cache_soup(self, payload):
        soups = Soups(soup_array=payload, id='soup')
        soups.put()

