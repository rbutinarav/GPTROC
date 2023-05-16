import streamlit as st
import os
import dotenv
import pandas as pd

def get_env(env_name):
    dotenv.load_dotenv()
    env_value = os.getenv(env_name)
    if env_value is None:
        env_value = st.secrets[env_name]    
    return env_value

def json_to_df (file_name):
    # Opening JSON file
    json_file = open(file_name)
    json_dict = json.load(json_file)
    json_df=pd.DataFrame(json_dict)
    json_file.close()
    return json_df