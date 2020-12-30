# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

class NrelScraperPipeline(object):

    def open_spider(self, spider):

        # Retrieve environment variables and keys
        hostname = os.getenv('HOSTNAME')
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        database = os.getenv('DATABASE')

        self.engine = create_engine(f'postgresql://{username}:{password}@{hostname}:5432/{database}')

    def close_spider(self, spider):
        self.engine.dispose()

    def process_item(self, item, spider):
        item['content'].to_sql('irradiance', self.engine, if_exists='append', index=False)
        return item