import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = '../databases/Movies.db'
table_name = 'Top_50'
csv_path = '../data/csv/top_50_films.csv'

def html_extraction(url):
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    return data

def tr_extraction_from_tbody(data):
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    return rows

def get_tr_data(rows, limit):
    df_list = []
    data_dict = {}

    for row in rows:
        if len(df_list)>=limit:
            break
        
        col = row.find_all('td')

        if len(col) == 0:
            continue
        
        data_dict = {
                "Average Rank": col[0].text.strip(),
                "Film": col[1].text.strip(),
                "Year": col[2].text.strip()
            }
        df_list.append(data_dict)

    return pd.DataFrame(df_list, columns=["Average Rank","Film","Year"])

def save_to_csv(df, csv_path):
    df.to_csv(csv_path, index=False)
    print(f"Datos guardados en: {csv_path}")

def save_to_db(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Datos guardados en la DB: {db_name} en la tabla: {table_name}")

def main():
    
    data = html_extraction(url)
    rows = tr_extraction_from_tbody(data)
    df = get_tr_data(rows, limit=50)
    
    print(df)

    save_to_csv(df, csv_path)
    save_to_db(df, db_name, table_name)

if __name__ == "__main__":
    main()