import streamlit as st
import json


def save_classified_dataset_df(dataset):

    #save the list locally filename: classified_dataset.txt
    with open("classified_dataset.txt", "w") as f:
        for item in dataset:
            f.write("%s\n" % item)
        st.write("The dataset has been saved in file classified_dataset.txt")
    #now create a jsonl version of the same list
    with open("dataset.jsonl", "w") as f:
        for item in dataset:
            json_object = {"text": item}
            json_string = json.dumps(json_object)
            f.write(json_string + '\n')

    st.write("The dataset has been saved in file classified_dataset.jsonl")
    #now create a | separated version of the same list
    with open("dataset.csv", "w") as f:
        for item in dataset:
            f.write(item+'|'+'\n')
    st.write("The dataset has been saved in file classified_dataset.csv")
    
    st.session_state.save_dataset = False