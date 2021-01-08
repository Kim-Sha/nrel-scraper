import json
import sys
from nrel_scraper.crawl import crawl

def scrape(event={}, context={}):
    print('====> Event:', event)
    print('====> Context:', context)
    crawl()

if __name__ == "__main__":
    try:
        event = json.loads(sys.argv[1])
    except IndexError:
        event = {}
    scrape(event)