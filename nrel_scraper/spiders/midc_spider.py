import scrapy
from nrel_scraper.items import NrelScraperItem

class MidcSpider(scrapy.Spider):
    name = "midc"
    start_urls = [
        'https://midcdmz.nrel.gov/apps/plot.pl?site=BMS&start=20200101&live=1&zenloc=222&amsloc=224&time=1&inst=15&inst=22&inst=41&inst=43&inst=45&inst=46&inst=47&inst=48&inst=49&inst=50&inst=51&inst=52&inst=53&inst=55&inst=62&inst=63&inst=74&inst=75&type=data&wrlevel=6&preset=0&first=3&math=0&second=-1&value=0.0&global=-1&direct=-1&diffuse=-1&user=0&axis=1',
        'https://midcdmz.nrel.gov/apps/plot.pl?site=BMS&start=20200101&live=1&zenloc=222&amsloc=224&time=1&inst=130&inst=131&inst=132&inst=134&inst=135&inst=142&inst=143&inst=146&inst=147&inst=148&inst=149&inst=150&inst=151&inst=156&inst=157&inst=158&inst=159&inst=160&inst=161&inst=164&inst=172&inst=173&type=data&wrlevel=6&preset=0&first=3&math=0&second=-1&value=0.0&global=-1&direct=-1&diffuse=-1&user=0&axis=1'
        ]
    # Associate url with corresponding postgres table in RDS instance
    map_table = {k:v for k, v in zip(start_urls, ['irradiance', 'meteorological'])}

    def parse(self, response):
        """
        The parse() method will be called to handle each of the requests for those URLs, even though we haven’t
        explicitly told Scrapy to do so. This happens because parse() is Scrapy’s default callback method, which is
        called for requests without an explicitly assigned callback.
        """
        data_text = response.xpath('//body/p/text()').get()
        # Identify correct table to push parsed data to
        push_to_table = self.map_table.get(response.request.url, None)
        # Yield data
        yield NrelScraperItem(data_text = data_text, table = push_to_table)