##att a class to each item in the list
import streamlit as st
from openai_functions import ai_complete

#create a cicle so that for each item in the dictionary openai will apply a class from the class list
def classify_dataset_df(list, classes):

    
    #define context
    context = "Apply one of the following classes: " + str(classes) + "to this text item: "
    max_items = st.slider("Please enter the number of items to classify", min_value=1, max_value=len(list), value=10)

    list_class = []

    #ask the model to use to perform the classification
    model = st.selectbox("Please select the model to use", ["text-davinci-003", "gpt-35-turbo"])
    run_name = st.text_input("Please enter the run name", "classify_dataset")

    #ask user to confirm and start the classification
    start = st.button("Start")

    if start:

        progress_bar = st.progress(0)

        for item in list[:max_items]:
            #ask openai to complete the sentence
            prompt = context + item
            completion = ai_complete(prompt, item, engine=model)
            #print the result
            #st.write("The item: ", item, "has been classified as: ", completion)
            #add the result to the list as separate new field callded "class"
            list_class.append(completion)

            #update the progress bar
            progress_bar.progress(list.index(item)/(max_items-1))
            st.session_state.list_class = list_class    
        
        #st.write(list)
        #st.write(list_class)
        st.write("Classification completed")
        st.session_state.classify_dataset = False

        return model, run_name, list_class
