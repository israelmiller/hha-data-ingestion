import pandas as pd #import pandas for general files
import json #import json for json files
import requests #import requests for web requests
import xlrd #import xlrd for excel files
from google.cloud import bigquery #import bigquery for bigquery
import db_dtypes #import db_dtypes for database types

##Import Excel File
#importing the data from sheet 1 and 2 in the excel file and converting it to a dataframe.

tab1 = pd.read_excel('SNAP-FY20.xls', sheet_name='NERO') #read SNAP FY 2020 excel file and import tab 1
tab1

tab2 = pd.read_excel('SNAP-FY20.xls', sheet_name='MARO') #read SNAP FY 2020 excel file and import tab 2
tab2

##Requests Package
#importing data from an open source JSON api using requests Package.

apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data') #import data from the open source JSON api
apiDataset = apiDataset.json() #convert the data to a json file
apiDataset

## BIGQUERY
# connect to bigquery
client = bigquery.Client.from_service_account_json('israel-507-354c0da1587f.json') ## create bigquery client


## Big Query 1
bigquery1_query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100") ## query chicago crime public dataset
bigquery1_results = bigquery1_query_job.result() ## get results
bigquery1 = pd.DataFrame(bigquery1_results.to_dataframe()) ## put results into dataframe 
bigquery1

## Big Query 2
bigquery2_query_job = client.query("SELECT * FROM `bigquery-public-data.stackoverflow.posts_questions` LIMIT 100") ## query COVID 19 public dataset
bigquery2_results = bigquery2_query_job.result() ## get results
bigquery2 = pd.DataFrame(bigquery2_results.to_dataframe()) ## put results into dataframe 
bigquery2

