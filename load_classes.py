import streamlit as st
import json

def load_classes_df():

    #ask user to define the name of the file
    filename = st.text_input("Define the name of the file to load the classes", "classes.json")

    #ask user to confirm the load
    confirm_load = st.button("Load")
    if confirm_load:
        with open(filename, 'r') as f:
            classes_list = json.load(f)

        st.session_state.classes_list = classes_list
                 
        st.session_state.load_classes = False