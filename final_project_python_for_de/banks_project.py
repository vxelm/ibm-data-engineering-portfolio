import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import numpy as np
from setting import LOGGING_DIR, DATA_DIR
import sqlite3



def log_process(message: str) -> None:
    timestamp = datetime.now().timestamp()
    with open(LOGGING_DIR / "code_log.txt", 'a') as f:
        f.write(f"{timestamp} : {message}")
    return None

def extract(url: str, table_attributes: list) -> pd.DataFrame:
    
    raw_page = requests.get(url).text
    soup = BeautifulSoup(raw_page, 'html.parser')
    df_list = []
    
    table = soup.find_all('table')[0]
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all('td')
        data_dict = {table_attributes[0]: cols[1].contents[2].text, 
                     table_attributes[1]: float(cols[2].text.strip())}
        df_list.append(data_dict)
    return pd.DataFrame(df_list)


def transform(df: pd.DataFrame, csv_path: str) -> pd.DataFrame:
    df_csv = pd.read_csv(csv_path)
    rates = df_csv.set_index("Currency")["Rate"]

    df["MC_GBP_Billion"] = (df["MC_USD_Billion"] * rates["GBP"]).round(2)
    df["MC_EUR_Billion"] = (df["MC_USD_Billion"] * rates["EUR"]).round(2)
    df["MC_INR_Billion"] = (df["MC_USD_Billion"] * rates["INR"]).round(2)
    return df
    

def load_to_csv(df: pd.DataFrame, path) -> None:
    filename = "Largest_banks_data.csv"
    csv_path = path / filename
    df.to_csv(csv_path, index=False)
    return None

def get_conn():
    return sqlite3.connect("Banks.db")

def load_to_db(df: pd.DataFrame, conn: sqlite3.Connection) -> None:
    table_name = "Largest_banks"
    df.to_sql(name=table_name, con=conn)
    return None

def run_queries(sttmt: str, conn: sqlite3.Connection) -> None:
    cursor = sqlite3.Cursor(conn)
    cursor.execute(sttmt)
    print(cursor.fetchall())
    return None


def main():
    url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
    
    
    df = extract(url, ['Name', 'MC_USD_Billion'])
    log_process("Data extraction complete. Initiating Transformation process")

    
    csv_name = "exchange_rate.csv"
    df = transform(df, DATA_DIR / csv_name )
    log_process("Data transformation complete. Initiating Loading process")
    
    load_to_csv(df, DATA_DIR)
    log_process("Data saved to CSV file")

    conn = get_conn()
    log_process("SQL Connection initiated")


    load_to_db(df, conn)
    log_process("Data loaded to Database as a table, Executing queries")

    run_queries("SELECT * FROM Largest_banks", conn)
    run_queries("SELECT AVG(MC_GBP_Billion) FROM Largest_banks", conn)
    run_queries("SELECT Name from Largest_banks LIMIT 5", conn)
    log_process("Process Complete")

    conn.close()
    log_process("Server Connection closed")

    

main()