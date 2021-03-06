# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from io import StringIO
import pandas as pd
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
        print(f'====> SQLAlchemy engine created for database: {database} at hostname: {hostname}')

    def close_spider(self, spider):
        self.engine.dispose()
        print('====> SQLAlchemy engine disposed')

    def process_item(self, item, spider):

        # Read ASCII text data into pandas dataframe and process
        df = pd.read_csv(StringIO(item['data_text']), sep=",")
        print('====> ASCII text data read into Pandas dataframe')

        df['measurement_ts'] = pd.to_datetime(df['DATE (MM/DD/YYYY)'] + ' ' + df['MST']).dt.tz_localize('MST')
        df.drop(['DATE (MM/DD/YYYY)', 'MST'], axis=1, inplace=True)
        df['station_id'] = 1
        df.columns = df.columns.str.lower()\
                               .str.replace("\(.*\)|\[.*\]", '', regex=True)\
                               .str.replace('li-200', 'li200')\
                               .str.strip().str.replace('-|\W+', '_', regex=True)
        print('====> Dataframe cleaned')

        # Write to associated table in Postgres
        df.to_sql(item['table'], self.engine, if_exists='append', index=False)

        return f"====> Data processed to: {item['table']} table in {self.engine.url.database}"