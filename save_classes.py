import streamlit as st
import json
def save_classes_df():

    #ask user to define the name of the file
    filename = st.text_input("Define the name of the file to save the classes", "classes.json")
    confirm_save = st.button("Save")

    if confirm_save:
        classes_list = st.session_state.classes_list
        #save the classes to a file
        with open(filename, 'w') as f:
            json.dump(classes_list, f)

        st.session_state.save_classes = False
