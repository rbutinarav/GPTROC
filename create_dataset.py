import streamlit as st
from openai_functions import ai_complete
import json
import pandas as pd


def create_dataset_df():
    #if "text_items_list" not in st.session_state:
    #    st.session_state.text_items_list = []
    if "suggested_classes_list" not in st.session_state:
        st.session_state.suggested_classes_list = []
    if "create_dataset" not in st.session_state:
        st.session_state.create_dataset = False


    general_topic = st.text_input("Please enter the general topic of the dataset", "tickets opened by clients of a large bank")
    num_text_items = st.number_input("Please enter the number of text items to generate", value=10)
    num_words = st.number_input("Please enter the number of words per review", value= 50)


    #set session state create_dataset to True
    st.session_state.create_dataset = True

    confirm_create = st.button("Start dataset creation")

    if confirm_create:
        context = "The following is 1 example of "+general_topic
        item_number = 1
        st.session_state.text_items_list = []
        # Add a progress bar
        progress_bar = st.progress(0)

        while item_number <= num_text_items :
            item = ai_complete(prompt=context, temperature=0.7, max_tokens=num_words*3, verbose=False, api_type="azure")
            st.session_state.text_items_list.append(item)

            # Update the progress bar
            progress_bar.progress(item_number / num_text_items)

            item_number += 1
    
        #set session state create_dataset to False
        st.session_state.create_dataset = False

    