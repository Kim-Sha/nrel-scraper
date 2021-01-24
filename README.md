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

## 🚀 Quick start

### Fork & Install Dependencies
All the dependencies for this project (e.g. Scrapy, Pandas, Psycopg2-binary) are bundled using Pipenv. Leverage them using `pipenv install` or `pipenv sync` (if you already have an activated virtual environment). If your developing for a different use-case, you can also set up your own pipenv with Scrapy as a starting dependency:
```
pipenv --three

pipenv shell

pipenv install scrapy
```
### Install Serverless
This Scrapy Crawler operates on Lambda and RDS using the Serverless framework, so you'll require an AWS account and credentials as prerequisites. You can configure Serverless access to your cloud provider by following [documentation](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/).
```
npm install -g serverless

serverless plugin install -n serverless-python-requirements
```

### Configure and Deploy
Make sure to configure the `serverless.yml` according to your [requirements and dependencies](https://www.serverless.com/blog/serverless-python-packaging). E.g.
```
custom:
  pythonRequirements:
    slim: true # Omits tests, __pycache__, *.pyc etc from dependencies
    usePipenv: true
    dockerizePip: non-linux
```
Deploy to your cloud provider. On AWS, you should see your application stored in an S3 bucket and a corresponding function on the Lambda console. Scheduled runs can be found on the CloudWatch dashboard.
```
serverless deploy --verbose
```

### Invoke (optional)

You can schedule job events using cron syntax in `serverless.yml`, but the function can also be invoked manually:
```
serverless invoke -f nrelScrape -l
```

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
