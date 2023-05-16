import streamlit as st
from general_functions import get_env
from openai_functions import ai_complete

from create_dataset import create_dataset_df
from load_dataset import load_dataset_df
from save_dataset import save_dataset_df
from create_classes import create_classes_df
from classify_dataset import classify_dataset_df
from load_classes import load_classes_df
from save_classes import save_classes_df
from load_classified_dataset import load_classified_dataset_df
from save_classified_dataset import save_classified_dataset_df
from gpt_statistics import gpt_statistics_df

import pandas as pd
import datetime

#inizialize session state variables
session_state_variables = [
    ("text_items_list", False),
    ("classes_list", False),
    ("create_dataset", False),
    ("load_dataset", False),
    ("save_dataset", False),
    ("create_classes", False),
    ("classify_dataset", False),
    ("list_class", []),
    ("results", {}),
    ('load_classes', False),
    ('save_classes', False),
    ('load_classified_dataset', False),
    ('save_classified_dataset', False),

]

for key, default_value in session_state_variables:
    if key not in st.session_state:
        st.session_state[key] = default_value

##MAIN INFORMATION

st.subheader("GPT ROC")
st.write("An integrated tool for Text Generation, Classification and Measurement")



##MANAGE DATESET

#ask the user if wants to create a new dataset:
create_dataset = st.sidebar.button("Create dataset")
if create_dataset or st.session_state.create_dataset:
    st.session_state.create_dataset = True
    create_dataset_df()
    st.write("Dataset created")

#ask the user if wants to load a new dataset:
load_dataset = st.sidebar.button("Load dataset")
if load_dataset or st.session_state.load_dataset:
    st.session_state.load_dataset = True
    load_dataset_df()

if st.session_state.text_items_list:
    #ask user if wants to see the list of items
    show_list = st.sidebar.checkbox("Show dataset")
    if show_list:
        st.write("This is the dataset:", st.session_state.text_items_list)

#if st.session_state.text_items_list:
    save_dataset = st.sidebar.button("Save dataset")
    if save_dataset or st.session_state.save_dataset:
        st.session_state.save_dataset = True
        save_dataset_df(st.session_state.text_items_list)


##MANAGE CLASSES

#if st.session_state.text_items_list:
    create_classes = st.sidebar.button("Create classes")
    if create_classes or st.session_state.create_classes:
        st.session_state.create_classes = True
        create_classes_df(st.session_state.text_items_list)

#ask the user if wants to load a new class list:
load_dataset = st.sidebar.button("Load classes")
if load_dataset or st.session_state.load_classes:
    st.session_state.load_classes = True
    load_classes_df()

#ask the user if wants to save a class list:
save_dataset = st.sidebar.button("Save classes")
if save_dataset or st.session_state.save_classes:
    st.session_state.save_classes = True
    save_classes_df()
    
if st.session_state.classes_list:
    #ask user if wants to see the list of classes
    show_list = st.sidebar.checkbox("Show list of classes")
    if show_list:
        st.write("This is the list of classes:", st.session_state.classes_list)


##MANAGE CLASSIFICATION

def update_results(text_items_list, list_class, model, run_name):
    if "results" not in st.session_state:
        st.session_state.results = {}
    
    for idx, item in enumerate(text_items_list):
        if idx not in st.session_state.results:
            st.session_state.results[idx] = {
                "text": item,
                "classifications": []
            }
        
        # Check if the current index is within the length of list_class
        if idx < len(list_class):
            result = {
                "class": list_class[idx],
                "timestamp": datetime.datetime.now(),
                "run_name": run_name,
                "model": model
            }
        else:
            # If the index is out of range, you can either skip it or assign a default value
            result = {
                "class": "Unknown",
                "timestamp": datetime.datetime.now(),
                "run_name": run_name,
                "model": model
            }
        
        st.session_state.results[idx]["classifications"].append(result)
    
    return st.session_state.results

if st.session_state.classes_list and st.session_state.text_items_list:
    classify_dataset = st.sidebar.button("Classify dataset")
    if classify_dataset or st.session_state.classify_dataset:
        st.session_state.classify_dataset = True
        results = classify_dataset_df(st.session_state.text_items_list, st.session_state.classes_list)
        if results:
            #st.write("Results:", results)
            model = results[0]
            run_name = results[1]
            list_class = results[2]
            st.session_state.list_class = list_class  # Assign list_class to st.session_state object
            #st.write('Model:', model, 'Run name:', run_name, "List class:", list_class)
        
            # Call the update_results function
            st.session_state.results = update_results(st.session_state.text_items_list, list_class, model, run_name)

save_classified_dataset = st.sidebar.button("Save classified dataset")
if save_classified_dataset or st.session_state.save_classified_dataset:
    st.session_state.save_classified_dataset = True
    save_classified_dataset_df(st.session_state.results)
    st.write("Classified_dataset_saved")

load_classified_dataset = st.sidebar.button("Load classified dataset")
if load_classified_dataset or st.session_state.load_classified_dataset:
    st.session_state.load_classified_dataset = True
    load_classified_dataset_df()
    st.write("Classified_dataset_loaded")

if st.session_state.results:
    #ask user if wants to see classified items
    show_classes_list = st.sidebar.checkbox("Show classified items")
    if show_classes_list:
        #st.write("This is the list of classified items:", st.session_state.list_class)
        st.write("This is the list items and their classes:", st.session_state.results)


##STATISTICS

#ask user if want to see statistics
show_statistics = st.sidebar.checkbox("Show statistics", value=True)

if show_statistics:
    if st.session_state.text_items_list:
        st.write("The dataset contains ", len(st.session_state.text_items_list), " items")

    if st.session_state.results:
        #calculate the number of classifications in the dataset
        classifications = len(st.session_state.results[0]["classifications"])
        st.write("The classified dataset contains ", classifications, " classifications")

show_advanced_statistics = st.sidebar.checkbox("Show advanced statistics")

if show_advanced_statistics:
    gpt_statistics_df()


##MANAGE ENVIRONMENT

#ask user if wants the results to be cleared
clear_results = st.sidebar.button("Clear results")
if clear_results:
    st.session_state.results = {}
    st.write("Results cleared")

#ask user if wants the window to be cleared
clear_results = st.sidebar.button("Clear window")
if clear_results:
    st.session_state.classify_dataset = False
    st.session_state.create_dataset = False
    st.session_state.load_dataset = False
    st.session_state.create_classes = False



    
        



