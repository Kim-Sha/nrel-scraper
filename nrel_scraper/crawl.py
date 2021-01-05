import sys
import scrapy
from scrapy.spiderloader import SpiderLoader
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Start sqlite3 fix
# https://stackoverflow.com/questions/52291998/unable-to-get-results-from-scrapy-on-aws-lambda
import imp
import sys
sys.modules["sqlite"] = imp.new_module("sqlite")
sys.modules["sqlite3.dbapi2"] = imp.new_module("sqlite.dbapi2")
# End sqlite3 fix

def crawl(spider_name="midc", spider_kwargs={}):

    project_settings = get_project_settings()
    print("====> Project settings retrieved")
    spider_loader = SpiderLoader(project_settings)
    spider_cls = spider_loader.load(spider_name)

    process = CrawlerProcess(project_settings)
    print(f"====> Crawler instantiated for spider: {spider_name}")

    process.crawl(spider_cls, **spider_kwargs)
    process.start()
    print(f"====> Spider {spider_name} has finished crawling")