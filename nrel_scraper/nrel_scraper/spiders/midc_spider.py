import scrapy


class MidcSpider(scrapy.Spider):
    name = "midc"
    start_urls = [
        'https://midcdmz.nrel.gov/apps/plot.pl?site=BMS&start=20200101&live=1&zenloc=222&amsloc=224&time=1&inst=45&inst=46&inst=47&inst=48&inst=49&inst=50&inst=51&inst=52&type=hour&wrlevel=6&preset=0&first=3&math=0&second=-1&value=0.0&global=-1&direct=-1&diffuse=-1&user=0&axis=1'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

            # response.xpath('//body/p/text()').getall()     