import streamlit as st
from openai_functions import ai_complete
import json
import pandas as pd


def load_dataset_df():
    # Load dataset from file
    # Ask the user to enter the name of the file
    filename = st.text_input("Please enter the name of the jsonl file containing the dataset", "dataset.jsonl")
    confirm_load = st.button("Load")
    
    if confirm_load:
        # Open the filename, which has a jsonl format and then parse it into a dictionary
        with open(filename) as f:
            dataset_dict = [json.loads(line) for line in f]
        
        # Extract the text from the dictionary and create a list of text items
        text_items_list = [item['text'] for item in dataset_dict]
        
        # Add the list of text items to the session state variable
        st.session_state.text_items_list = text_items_list
        st.write("The dataset has been loaded from file ", filename)

        st.session_state.load_dataset = False
