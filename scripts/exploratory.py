import requests
import json
import pandas as pd
from pathlib import Path


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

def get_makes(output_path: str):
    '''
    make all the motorcycle makes and save to CSV file
    parameters: output_path whcih contains a full path to where the data will be stored
    '''
    make_url = "https://motorcycle-specs-database.p.rapidapi.com/make"
    make_df=pquery(make_url, headers)
    make_df.to_csv(Path(output_path, "Moto_makes.csv"), sep=",")
    

def main():
    output_path="C:/Users/kingo/Dropbox/pyProject/moto_data/moto_data"
    #url = "https://motorcycle-specs-database.p.rapidapi.com/model/make-id/100/2015"
    
    url = "https://motorcycle-specs-database.p.rapidapi.com/model/make-name/Kawasaki"
    with open("URLs.txt", "r") as file:
        url_list=[line for line in file]
    file.close()
if __name__ == '__main__':
    main()
