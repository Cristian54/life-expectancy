import sqlite3, csv
from sqlite3 import Error

def main():
    database = r"Data/CountriesData.sqlite"
    conn = sqlite3.connect(database)
    
    cur = conn.cursor()

    country = 'Angola'
    year = '1961'
    
    sql = """
        SELECT Population
        FROM Population
        WHERE CountryNamePop = ? AND Year = ?
    """
    
    cur.execute(sql, (country,year,))
    test = cur.fetchone()
    print(test)
    
    cur.close()
    

if __name__ == '__main__':
    main()