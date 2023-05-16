import streamlit as st
from general_functions import get_env
from openai_functions import ai_complete

from create_dataset import create_dataset_df
from load_dataset import load_dataset_df
from save_dataset import save_dataset_df
from create_classes import create_classes_df
from classify_dataset import classify_dataset_df

import pandas as pd
import datetime

#inizialize session state variables
if "text_items_list" not in st.session_state:
    st.session_state.text_items_list = False
if "classes_list" not in st.session_state:
    st.session_state.classes_list = False
if "create_dataset" not in st.session_state:
    st.session_state.create_dataset = False
if "load_dataset" not in st.session_state:
    st.session_state.load_dataset = False
if "save_dataset" not in st.session_state:
    st.session_state.save_dataset = False
if "create_classes" not in st.session_state:
    st.session_state.create_classes = False
if "classify_dataset" not in st.session_state:
    st.session_state.classify_dataset = False
if "list_class" not in st.session_state:
    st.session_state.list_class = False
if "results" not in st.session_state:
    st.session_state.merged = False


#ask the user if wants to create a new dataset:
create_dataset = st.sidebar.button("Create dataset")
if create_dataset or st.session_state.create_dataset:
    st.session_state.create_dataset = True
    create_dataset_df()
    st.write("Dataset created")
    #st.session_state.create_dataset = False

#ask the user if wants to load a new dataset:
load_dataset = st.sidebar.button("Load dataset")
if load_dataset or st.session_state.load_dataset:
    st.session_state.load_dataset = True
    load_dataset_df()
    #st.session_state.load_dataset = False

if st.session_state.text_items_list:
    #ask user if wants to see the list of items
    show_list = st.sidebar.checkbox("Show list of items.")
    if show_list:
        st.write("This is the dataset:", st.session_state.text_items_list)

if st.session_state.text_items_list:
    save_dataset = st.sidebar.button("Save dataset")
    if save_dataset or st.session_state.save_dataset:
        st.session_state.save_dataset = True
        save_dataset_df(st.session_state.text_items_list)
        #st.session_state.save_dataset = False

if st.session_state.text_items_list:
    create_classes = st.sidebar.button("Create classes")
    if create_classes or st.session_state.create_classes:
        st.session_state.create_classes = True
        create_classes_df(st.session_state.text_items_list)
        #st.session_state.create_classes = False
    
if st.session_state.classes_list:
    #ask user if wants to see the list of classes
    show_list = st.sidebar.checkbox("Show list of classes")
    if show_list:
        st.write("This is the list of classes:", st.session_state.classes_list)

if st.session_state.classes_list and st.session_state.text_items_list:
    #ask user if wants to apply classification
    classify_dataset = st.sidebar.button("Classify dataset")
    if classify_dataset or st.session_state.classify_dataset:
        st.session_state.classify_dataset = True
        model, run_name, _ = classify_dataset_df(st.session_state.text_items_list, st.session_state.classes_list)
        
        if not hasattr(st.session_state, 'results'):
            st.session_state.results = {}
        
        for idx, item in enumerate(st.session_state.text_items_list):
            if idx not in st.session_state.results:
                st.session_state.results[idx] = {
                    "text": item,
                    "classifications": []
                }
            
            result = {
                "class": st.session_state.list_class[idx],
                "timestamp": datetime.datetime.now(),
                "run_name": run_name,
                "model": model
            }
            
            st.session_state.results[idx]["classifications"].append(result)

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

if st.session_state.classes_list:
    #ask user if wants to see classified items
    show_classes_list = st.sidebar.checkbox("Show classified items")
    if show_classes_list:
        #st.write("This is the list of classified items:", st.session_state.list_class)
        st.write("This is the list items and their classes:", st.session_state.results)

    
        



