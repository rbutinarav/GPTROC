import streamlit as st
from openai_functions import ai_complete

def create_dataset():
    if "text_items_list" not in st.session_state:
        st.session_state.text_items_list = []
    if "suggested_classes_list" not in st.session_state:
        st.session_state.suggested_classes_list = []

    general_topic = st.text_input("Please enter the general topic of the dataset", "tickets opened by clients of a large bank")
    num_text_items = st.number_input("Please enter the number of text items to generate", value=10)
    num_words = st.number_input("Please enter the number of words per review", value= 50)
    num_classes = st.number_input("Please enter the number of classes to generate", 2)

    create_dataset = st.sidebar.button("Create dataset")
    if create_dataset:
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
    
    if st.session_state.text_items_list != []:
        #ask the user if he wants to see the list of items
        show_list = st.sidebar.checkbox("Show list of items")
        if show_list:
            st.write("The following is the list of "+general_topic)
            st.write(st.session_state.text_items_list)

        #ask the user if he wants to delete the list of items
        delete_list = st.sidebar.button("Delete list of items")
        if delete_list:
            st.session_state.text_items_list = []
            st.write("The list of items has been deleted")

    create_classes = st.sidebar.button("Create classes")
    if create_classes:
        context_classifier = "Analyze the following items and identify "+str(num_classes)+" classes that will be used to categorize those and future items of the same kind. Provide the result as a plain text separated by commas."
        max_num_items_classifier = int (2048 / num_words)
        num_items_classifier = min (num_text_items, max_num_items_classifier)
        st.write ('I will be able to analyze in one round ', num_items_classifier, ' items, trying to derive ', num_classes, ' classes')
       
        text_items_list_classifier = st.session_state.text_items_list[:num_items_classifier]
        #convert the list of items to a string where each item is marked by [ at the beginning and ] at the end
        text_items_list_classifier = str(text_items_list_classifier)
    
        classifier_prompt = context_classifier + text_items_list_classifier
        
        suggested_classes = ai_complete(classifier_prompt, temperature=0.7, max_tokens=num_words*3, verbose=False, api_type="azure")

        #parse the suggested classes that are separated by commas and create a list
        suggested_classes_list = suggested_classes.split(",")

        #add suggested classes to session state variable
        st.session_state.suggested_classes_list = suggested_classes_list

    if st.session_state.suggested_classes_list != []:
        st.write("The suggested classes are: ", st.session_state.suggested_classes_list)
        #ask the user if he want to modify the suggested classes, if so ask him to enter the new classes separated by commas, defult is the suggested classes
        modify_classes = st.sidebar.checkbox("Modify classes")
            
        if modify_classes:
                new_classes = st.sidebar.text_input("Please enter the new classes separated by commas", suggested_classes)
                new_classes_list = new_classes.split(",")
                st.write("The new classes are: ", new_classes_list)
                suggested_classes_list = new_classes_list


  



        

