
# csv from https://www.stats.govt.nz/large-datasets/csv-files-for-download/

from urllib import request

url = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2017-financial-year-provisional/Download-data/annual-enterprise-survey-2017-financial-year-provisional-size-bands-csv.csv'

def fileDownloader(csv_url):
    response = request.urlopen(csv_url)

    csv = response.read()
    csv_str = str(csv)

    lines = csv_str.split("\\n")

    # lines now looks like ["bla bla", "bla", "bla bla bla"]

    dest_url = r'D:\School\data.csv'
    fx=open(dest_url,'w')

    for line in lines:
        fx.write(line+'\n')
    fx.close()

fileDownloader(url)

'''
#Tried method similar to image download. Does not fetch entire file.
import random
import urllib.request #module defines functions and classes which help in opening URLs

def download_csv(url):
    name = random.randrange(1,1000)
    file_name = str(name)+".csv"
    urllib.request.urlretrieve(url,file_name)


download_csv('https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2017-financial-year-provisional/Download-data/annual-enterprise-survey-2017-financial-year-provisional-size-bands-csv.csv')

'''