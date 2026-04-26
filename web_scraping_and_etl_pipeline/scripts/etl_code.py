import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "../logs/log_file.txt"
target_file = "../data/transformed_data.csv"

def extract_from_csv(file_path):
    dataframe = pd.read_csv(file_path)
    return dataframe

def extract_from_json(file_path):
    dataframe = pd.read_json(file_path, lines=True)
    return dataframe

def extract_from_xml(file_path):
    df_list = []
    tree = ET.parse(file_path)
    root = tree.getroot()

    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)

        single_row = {"name":name, "height":height, "weight":weight}
        df_list.append(single_row)
    
    return pd.DataFrame(df_list, columns=["name", "height", "weight"])

def extract():
    df_list = []

    for csvfile in glob.glob("../data/csv/*.csv"):
        new_data = extract_from_csv(csvfile)
        df_list.append(new_data) 

    for jsonfile in glob.glob("../data/json/*.json"):
        new_data = extract_from_json(jsonfile)
        df_list.append(new_data) 

    for xmlfile in glob.glob("../data/xml/*.xml"):
        new_data = extract_from_xml(xmlfile)
        df_list.append(new_data)

    data = pd.concat(df_list, ignore_index=True)
    data.columns = ['name', 'height', 'weight']

    return data

def transform(data):
    #Convertir pulgadas a metros redondeando a 2 decimales:
    data['height'] = round(data['height'] * 0.0254, 2)

    #Convertir libras a kg redondeando a 2 decimales:
    data['weight'] = round(data['weight'] * 0.45359237, 2)

    return data

def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a+") as f:
        f.write(timestamp + ',' + message + '\n')

# Log de inicializacion del ETL process 
log_progress("ETL Job Started") 

# Log de inicio del Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log del inicio del Extraction process 
log_progress("Extract phase Ended") 
 
# Log de inicio del proceso de Transformación
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log de finalización del proceso de Transformación
log_progress("Transform phase Ended") 
 
# Log de beginning of de Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log de inicio del proceso de carga
log_progress("Load phase Ended") 
 
# Log de finalización del proceso ETL
log_progress("ETL Job Ended") 