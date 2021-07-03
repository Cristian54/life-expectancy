import sqlite3, csv
from sqlite3 import Error

def main():
    database = r"Data/CountriesData.sqlite"
    conn = sqlite3.connect(database)
    
    cur = conn.cursor()

    cur.execute('SELECT CountryNamePop FROM Populations WHERE Year = 1960')
    test = cur.fetchall()
    for t in test: print(t)
    cur.close()
    

if __name__ == '__main__':
    main()