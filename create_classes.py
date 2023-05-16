import streamlit as st
from openai_functions import ai_complete

def create_classes_df(list, num_words=50, num_text_items=100):

    if st.session_state.create_classes:
        #initialize session state variables
        if "generate_classes" not in st.session_state:
            st.session_state.generate_classes = False

        text_items_list=list
        num_classes = st.number_input("Please enter the number of classes to generate", 2)

        context_classifier = "Analyze the following items and identify "+str(num_classes)+" classes that will be used to categorize those and future items of the same kind. Provide the result as a plain text separated by commas."
        max_num_items_classifier = int (2048 / num_words)
        num_items_classifier = min (num_text_items, max_num_items_classifier)
        st.write ('I will be able to analyze in one round ', num_items_classifier, ' items, trying to derive ', num_classes, ' classes')
        
        #ask user to generated classes
        generate_classes = st.button("Generate classes")

        if generate_classes or st.session_state.generate_classes:
            st.session_state.generate_classes = True
            text_items_list_classifier = text_items_list[:num_items_classifier]
            #convert the list of items to a string where each item is marked by [ at the beginning and ] at the end
            text_items_list_classifier = str(text_items_list_classifier)

            classifier_prompt = context_classifier + text_items_list_classifier

            suggested_classes = ai_complete(classifier_prompt, temperature=0.7, max_tokens=num_words*3, verbose=False, api_type="azure")

            suggested_classes_list = suggested_classes.split(",")
            #remove spaces from the new classes
            suggested_classes_list = [x.strip(' ') for x in suggested_classes_list]
            st.session_state.classes_list = suggested_classes_list

            st.write("The new classes are: ", suggested_classes_list)

            #ask user to confirm the new generated classes
            #st.session_state.create_classes = False
            st.session_state.generate_classes = False
            #classes_list_confirmed = st.button("Confirm classes")

                

        if st.session_state.classes_list != []:
            suggested_classes = str(st.session_state.classes_list)
            st.write("If you want to modify the suggested classes, please enter the new classes separated by commas")
                
            new_classes = st.text_input("Please enter the new classes separated by commas", suggested_classes)
            new_classes_list = new_classes.split(",")
            #remove spaces from the new classes
            new_classes_list = [x.strip(' ') for x in new_classes_list]
            st.write("The new classes are: ", new_classes_list)

            #ask user to confirm the new generated classes
            classes_list_confirmed = st.button("Confirm classes")
            
            if classes_list_confirmed:
                st.session_state.classes_list = new_classes_list
                st.session_state.create_classes = False
                st.session_state.generate_classes = False
                generate_classes = False


