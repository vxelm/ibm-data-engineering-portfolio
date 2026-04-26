import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

from settings import RAW_DATA_DIR, PROCESSED_DATA_DIR, LOGS_DIR, target_file, log_file

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe

"""Coursera solution:
def extract_from_xml(file_to_process): 
    dataframe = pd.DataFrame(columns=["name", "height", "weight"]) 
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True) 
    return dataframe 
"""

# My solution:
def extract_from_xml(file_to_process):
    datalist = []
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        datalist.append({"name":name, "height":height, "weight":weight})
    dataframe = pd.DataFrame(datalist)
    return dataframe

def extract():
    extracted_data = pd.DataFrame()
    csv_df_list = [extract_from_csv(csvfile) for csvfile in glob.glob(f"{RAW_DATA_DIR}/*.csv") if csvfile != target_file]
    if csv_df_list:
        csv_extracted_data = pd.concat(csv_df_list, ignore_index=True)

    json_df_list = [extract_from_json(jsonfile) for jsonfile in glob.glob(f"{RAW_DATA_DIR}/*.json")]
    if json_df_list:
        json_extracted_data = pd.concat(json_df_list, ignore_index=True)

    xml_df_list = [extract_from_xml(xmlfile) for xmlfile in glob.glob(f"{RAW_DATA_DIR}/*.xml")]
    if xml_df_list:
        xml_extracted_data = pd.concat(xml_df_list, ignore_index=True)

    extracted_data = pd.concat([csv_extracted_data, json_extracted_data, xml_extracted_data], ignore_index=True)
    return extracted_data

def transform(data):
    '''Convert inches to meters and round off to two decimals
    1 inch = 0.0254 meters '''
    data['height'] = round(data.height * 0.0254, 2)

    '''Convert pounds to kilograms and round off to two decimal
    1 pound = 0.45359237 meters'''
    data['weight'] = round(data.weight * 0.45359237, 2)

    return data


def load_data(target_file: str, transformed_data: pd.DataFrame) -> None:
    transformed_data.to_csv(f"{PROCESSED_DATA_DIR}/{target_file}")

def log_progress(mesagge):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(f"{LOGS_DIR}/{log_file}", "a") as f:
        f.write(timestamp + ',' + mesagge + '\n')


def main() -> None:
    # Log the initialization of the ETL process 
    log_progress("ETL Job Started") 
    
    # Log the beginning of the Extraction process 
    log_progress("Extract phase Started") 
    extracted_data = extract() 
    
    # Log the completion of the Extraction process 
    log_progress("Extract phase Ended") 
    
    # Log the beginning of the Transformation process 
    log_progress("Transform phase Started") 
    transformed_data = transform(extracted_data) 
    print("Transformed Data") 
    print(transformed_data) 
    
    # Log the completion of the Transformation process 
    log_progress("Transform phase Ended") 
    
    # Log the beginning of the Loading process 
    log_progress("Load phase Started") 
    load_data(target_file,transformed_data) 
    
    # Log the completion of the Loading process 
    log_progress("Load phase Ended") 
    
    # Log the completion of the ETL process 
    log_progress("ETL Job Ended") 


if __name__ == '__main__':
    main()