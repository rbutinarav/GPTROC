import json
import streamlit as st

def save_classified_dataset_df(dataset):
    # Save the results as a txt file
    with open("classified_dataset.txt", "w") as f:
        for idx, item in dataset.items():
            text = item["text"]
            classifications = item["classifications"]
            f.write(f"{text}\n")
            for classification in classifications:
                f.write(f"  - {classification}\n")
        st.write("The dataset has been saved in file classified_dataset.txt")

    # Save the results as a jsonl file
    with open("classified_dataset.jsonl", "w") as f:
        for idx, item in dataset.items():
            # Convert datetime objects to strings for each classification
            for classification in item["classifications"]:
                classification["timestamp"] = classification["timestamp"].strftime("%Y-%m-%dT%H:%M:%S")
            
            item["index"] = idx  # Add the index to the item dictionary
            json_string = json.dumps(item)
            f.write(json_string + '\n')

    # Save the results as a csv file
    with open("classified_dataset.csv", "w") as f:
        for idx, item in dataset.items():
            text = item["text"]
            classifications = item["classifications"]
            f.write(f"{text}|")
            for classification in classifications:
                class_str = f"{classification['class']} ({classification['model']} - {classification['run_name']})"
                f.write(class_str + '|')
            f.write('\n')
        st.write("The dataset has been saved in file classified_dataset.csv")

    st.session_state.save_dataset = False
