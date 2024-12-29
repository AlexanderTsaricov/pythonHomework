# Task 1
import csv
import json
import os
import pickle
from pprint import pprint
from pathlib import Path

def getDirectoryInfo (catalog, parent='No'):
    result = {}
    catalogObj = Path(catalog)
    result['name'] = catalogObj.name
    result['files'] = []
    result['subdirectory'] = []
    result['parent'] = parent
    result['size'] = catalogObj.stat().st_size
    for file in catalogObj.iterdir():
        if file.is_dir():
            result['subdirectory'].append(getDirectoryInfo(file, catalogObj.resolve().name))
        elif file.is_file():
            result['files'].append({'name': file.name, 'size': file.stat().st_size})
    return result

def saveToJson(nameJson, data):
    with open(f'{nameJson}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def saveToCSV(nameCSV, data):
    with open(f'{nameCSV}.csv', 'w',newline='', encoding='utf-8') as file:
        csv_writer = csv.DictWriter(file, fieldnames=list(data.keys()), restval='file')
        csv_writer.writeheader()
        csv_writer.writerow(data)

def saveToPickle(namePickle, data):
    with open(f'{namePickle}.pkl', 'wb') as file:
        pickle.dump(data, file)

# Task 2

def saveInOneFile (catalog, nameFile):
    catalogObj = Path(catalog)
    allList = []
    for file in catalogObj.iterdir():
        with open(f'{catalog}/{file.name}', 'r', encoding='utf-8') as fileJson:
            listFromJson = json.load(fileJson)
            for item in listFromJson:
                allList.append(item)
    saveToJson(nameFile, allList)

# Task 3

def convertJsonToCSV (jsonFile, nameCSVFile):
    headers = []
    data = []
    with open(jsonFile, 'r', encoding='utf-8') as file:
        listFromJson = json.load(file)
        headers = list(listFromJson[0].keys())
        for item in listFromJson:
            peopleData = {}
            for key, value in item.items():
                peopleData[key] = value
            data.append(peopleData)
    with open(f'{nameCSVFile}.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.DictWriter(file, fieldnames=headers, restval='people')
        csv_writer.writeheader()
        csv_writer.writerows(data)

# Task 4

def getTotalpryses(file, csvName):
    with (
        open(file, 'r', newline='', encoding='utf-8') as f_read,
        open(f'{csvName}.csv', 'w', newline='', encoding='utf-8') as f_write
    ):
        csv_file_read = csv.DictReader(f_read)
        csv_file_write = csv.DictWriter(f_write, fieldnames=['product','price'], quoting=csv.QUOTE_NONNUMERIC)
        result = []
        for item in csv_file_read:
            result.append({'product': item['product'], 'price': round(float(item['quantity']) * float(item['price']), 2)})
        csv_file_write.writeheader()
        csv_file_write.writerows(result)


# Task 5
# В задании написано одно, а в CSV файле другое, ну... сделаю что нибудь. Сгруппирую по возрасту



