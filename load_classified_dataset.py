import json
import datetime
import streamlit as st

def load_classified_dataset_df():
    results = {}

    filename = st.text_input("Please enter the name of the jsonl file containing the classified dataset", "classified_dataset.jsonl")
    confirm_load = st.button("Load")
    
    if confirm_load:
    
        with open(filename, "r") as f:
            for line in f:
                json_object = json.loads(line)
                index = json_object["index"]
                
                # Convert timestamp strings back to datetime objects for each classification
                for classification in json_object["classifications"]:
                    classification["timestamp"] = datetime.datetime.strptime(classification["timestamp"], "%Y-%m-%dT%H:%M:%S")
                
                results[index] = {
                    "text": json_object["text"],
                    "classifications": json_object["classifications"]
                }
        
        st.session_state.load_classified_dataset = False
        st.session_state.results = results

        #calculate the number of items in the dataset
        length = len(st.session_state.results)
        st.write("The dataset has been loaded from file ", filename)
        st.write("The dataset contains ", length, " items")

        #st.write ("This is the dataset: ", results)

        #derive st.session_state.text_items_list
        st.session_state.text_items_list = [item['text'] for item in results.values()]

        #st.write("This is the text_items_list: ", st.session_state.text_items_list)

        return results
