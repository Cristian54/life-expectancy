import requests
from bs4 import BeautifulSoup
import csv
import os


def getCountries():
    URL = 'https://www.worldometers.info/geography/alphabetical-list-of-countries/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')

    div = soup.find_all('div', attrs={'class':'container'})
    content = div[1].find('div', attrs={'class':'content-inner'})
    table = content.find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    countries = []
    for row in rows:
        country = row.find_all('td')[1]
        countries.append(country.text.strip())
        country = ''

    return countries


def clean(input, countries):
    tmpFile = "tmp.csv"
    with open(input, "r") as file, open(tmpFile, "w") as outFile:
        reader = csv.reader(file, delimiter=',')
        writer = csv.writer(outFile, delimiter=',')
        header = next(reader)
        writer.writerow(header)
        for row in reader:
            colValues = []
            if row[0] in countries: 
                for col in row:
                    colValues.append(col)
                writer.writerow(colValues)
    os.rename(tmpFile, input)

""" countries = getCountries()
countries.append('Puerto Rico')
countries.append('Venezuela, RB')
clean('Data/country_population.csv', countries) """

def reorgCSV(input):
    tempFile = "temp.csv"
    with open(input) as file, open(tempFile, "w") as temp:
        reader = csv.reader(file, delimiter=',')
        writer = csv.writer(temp, delimiter=',')
        
        colNames = next(reader)
        colNames.pop(0)
        
        for row in reader:
            colvals = []
            colvals.append(row[0])
            country = row[0]
            row.pop(0)
            for col, year in zip(row, colNames):
                colvals.append(year)
                colvals.append(col)
                writer.writerow(colvals)
                colvals = [country]
    os.rename(tempFile, input)

#reorgCSV('Data/country_population.csv')

def addIDCol(input):
    tempFile = "temp.csv"
    with open(input) as file, open(tempFile, "w") as temp:
        reader = csv.reader(file, delimiter=',')
        writer = csv.writer(temp, delimiter=',')
        
        headers = ['dummyID']
        csvHeaders = next(reader)
        for h in csvHeaders: headers.append(h)
        writer.writerow(headers)
        
        id = 0
        for row in reader: 
            colVals = [id]
            for ele in row: colVals.append(ele)
            writer.writerow(colVals)
            id += 1
        os.rename(tempFile, input)

addIDCol('Data/country_population.csv')