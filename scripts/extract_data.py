import requests
import json
import pandas as pd
from pathlib import Path
import sys
import os
import time

headers = {
	"X-RapidAPI-Key": "40b9d78839msh1124f7dc823b1e3p1ea943jsn7ece27de6cfa",
	"X-RapidAPI-Host": "motorcycle-specs-database.p.rapidapi.com"
}

def pquery(url: str, headers: str)->pd.DataFrame:
    '''
    querys data from an API through a URL and returns an object of type pandas dataframe
    '''
    try:

        response = requests.request("GET", url, headers=headers)
        json_response=json.loads(response.content)
        motodf=pd.json_normalize(json_response)

        return motodf

    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)

def save_queries(output_path: str, url, filename):
    '''
    make all the motorcycle makes and save to CSV file
    parameters: output_path whcih contains a full path to where the data will be stored
    '''
    make_df=pquery(url, headers)
    make_df.to_csv(Path(output_path, filename), sep=",")


def automate_data_extraction(output_path):
    '''
    reading content of URL file and storing into list
    '''
    with open("./moto_data/scripts/URL221130.txt", "r") as file:
        url_list=[line.replace("\n", "") for line in file]
    file.close()
    print(url_list)
    #performing and saving queries into csv file
    for item in url_list:
        motoID=item.split("/")[-1]
        save_queries(output_path, item, f"motoFILE_{motoID}.csv")
        time.sleep(10)
    

def main():
    #url = "https://motorcycle-specs-database.p.rapidapi.com/model/make-id/100/2015"
    

    sys.path.append(os.path.abspath(os.path.join(".","./moto_data/Data")))
    setpath=sys.path
    print(setpath)
    list_path=[item for item in setpath if "\\moto_data\\Data" in item]
    if len(list_path)==0:
        print("Data Folder Not Found")
        sys.exit()
    if len(list_path)>1:
        print("More than one data folder found")
        sys.exit()
    output_path=list_path[0]
    #execute once!
    #automate_data_extraction(output_path)
if __name__ == '__main__':
    main()
