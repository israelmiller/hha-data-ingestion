import pandas as pd #import pandas for general files
import json #import json for json files
import requests #import requests for web requests
import xlrd #import xlrd for excel files

#importing the data from sheet 1 and 2 in the excel file and converting it to a dataframe.

tab1 = pd.read_excel('SNAP-FY20.xls', sheet_name='NERO') #read SNAP FY 2020 excel file and import tab 1
tab1

tab2 = pd.read_excel('SNAP-FY20.xls', sheet_name='MARO') #read SNAP FY 2020 excel file and import tab 2
tab2

#importing data from an open source JSON api using requests Package.

apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data') #import data from the open source JSON api
apiDataset = apiDataset.json() #convert the data to a json file
apiDataset




