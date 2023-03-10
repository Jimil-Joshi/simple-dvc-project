import yaml
import os
import shutil
import logging
import json

def read_params(cofig_path: str) -> dict:
    with open(cofig_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def clean_prev_dir_if_exist(dir_path):
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)


def create_dir(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)

    

def save_local_df(df, df_path, header=False):
    if header:
        new_cols = [col.replace(" ","_") for col in df.columns]
        df.to_csv(df_path, index = False, header=new_cols)

    else:
        df.to_csv(df_path, index = False)

def save_reports(filepath:str, report:dict):
    with open(filepath,"w") as f:
        json.dump(report,f, indent=4)

      
