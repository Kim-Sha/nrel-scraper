<p align="center">
  <a href="https://midcdmz.nrel.gov/">
    <img alt="MIDC" src="https://midcdmz.nrel.gov/srrl_bms/pictures/bms.jpg" width="300" />
  </a>
</p>
<h1 align="center">
  NREL MIDC Scraper
</h1>

This is a project to scrape solar irradiance and meteorological data from NREL's Measurement and Instrumentation Data Center (MIDC) records. The specific station being crawled is their baseline measurement system located in Denver, Colorado.

A Scrapy crawler parses the requested response, before a SQLAlchemy connection is leveraged to push data to a PostgreSQL instance hosted on Amazon RDS. Using the Serverless framework, this function is deployed to AWS Lambda and scheduled for daily scraping at 11:59PM MST (UTC-7:00). The project backlog is tracked on this [Kanban board](https://github.com/Kim-Sha/nrel-scraper/projects/1).

## 🧐 What's inside?

A quick look at the top-level files and directories you'll likely find in this repository:

    .
    ├── nrel_scraper
    ├── query_history
    ├── .gitignore
    ├── Pipfile
    ├── Pipfile.lock
    ├── handler.py
    ├── LICENSE
    ├── package-lock.json
    ├── package.json
    ├── scrapy.cfg
    ├── serverless.yml
    └── README.md

1. **`/nrel_scraper`**: This directory contains all of the data that will be queried by GraphQL and ultimately displayed on the website. 

2.  **`/query_history`**: This directory contains all of the modules of code that your project depends on (npm packages) are automatically installed.

3.  **`.gitignore`**: This file tells git which files it should not track / not maintain a version history for.

4. **`package-lock.json`** (See `package.json` below, first). This is an automatically generated file based on the exact versions of your npm dependencies that were installed for your project. **(You won’t change this file directly).**

5. **`package.json`**: A manifest file for Node.js projects, which includes things like metadata (the project’s name, author, etc). This manifest is how npm knows which packages to install for your project.

6. **`README.md`**: A text file containing useful reference information about your project.


## 🚀 Quick start

Scrapy Crawler on AWS Lambda
```
pipenv --three

pipenv shell

pipenv install scrapy
```
Install Serverless
```
npm install -g serverless

serverless plugin install -n serverless-python-requirements
```
Deploy
```
severless deploy --verbose
```
Invoke
```
serverless invoke -f nrelScrape -l
```
