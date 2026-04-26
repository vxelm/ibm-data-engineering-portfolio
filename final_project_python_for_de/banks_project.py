import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import numpy as np
from setting import LOGGING_DIR



def log_process(message: str) -> None:
    timestamp = datetime.timestamp()
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
                     table_attributes[1]: cols[2].text.strip()}
        df_list.append(data_dict)
    return pd.DataFrame(df_list)

    
    

def main():
    url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
    print(extract(url, ['Name', 'MC_USD_Billion']))

main()