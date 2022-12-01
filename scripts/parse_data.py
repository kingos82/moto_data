import pandas as pd
import sys
import os
from pathlib import Path


def find_path():
    sys.path.append(os.path.abspath(os.path.join(".","./moto_data/Data")))
    setpath=sys.path
    list_path=list(set([item for item in setpath if "\\moto_data\\Data" in item]))
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
file_names=os.listdir(Path(output_path))
print(file_names)
df_list=[]
for file in file_names:
    df=pd.read_csv(Path(output_path,file))
    df_list.append(df)

master_df=pd.concat(df_list)

print(master_df.info())