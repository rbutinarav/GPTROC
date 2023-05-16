import streamlit as st
import json


def save_dataset_df(list):

    #save the list locally filename: dataset.txt
    with open("dataset.txt", "w") as f:
        for item in list:
            f.write("%s\n" % item)
        st.write("The list of items has been saved in file dataset.txt")
    #now create a jsonl version of the same list
    with open("dataset.jsonl", "w") as f:
        for item in list:
            json_object = {"text": item}
            json_string = json.dumps(json_object)
            f.write(json_string + '\n')

    st.write("The list of items has been saved in file dataset.jsonl")
    #now create a | separated version of the same list
    with open("dataset.csv", "w") as f:
        for item in list:
            f.write(item+'|'+'\n')
    st.write("The list of items has been saved in file dataset.csv")
    
    st.session_state.save_dataset = False