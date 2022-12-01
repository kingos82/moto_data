import pandas as pd
import sys
import os
from pathlib import Path


def find_path():
    sys.path.append(os.path.abspath(os.path.join("..","./Data")))
    setpath=sys.path
    list_path=list(set([item for item in setpath if "Data" in item]))
    
    if len(list_path)==0:
        print("Data Folder Not Found")
        sys.exit()
    if len(list_path)>1:
        print("More than one data folder found")
        print(list_path)
        sys.exit()
    output_path=list_path[0]
    return output_path

output_path=find_path()
file_names = []
for name in os.listdir("../Data/"):
    if name.endswith(".csv"):
        file_names.append(name)

df_list=[]
for file in file_names:
    df=pd.read_csv(Path(output_path,file))
    df_list.append(df)

master_df=pd.concat(df_list)

print(master_df.info())