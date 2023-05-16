import streamlit as st

def gpt_statistics_df():

    def get_run_names(data):
        run_names = set()
        for item in data.values():
            for classification in item["classifications"]:
                run_names.add(classification["run_name"])
        return list(run_names)

    
    if st.session_state.text_items_list:
        st.write("The dataset contains ", len(st.session_state.text_items_list), " items")

    if st.session_state.results:
        results = st.session_state.results
        run_names = get_run_names(results)
        #calculate the number of runs in the dataset
        runs = len(run_names)
        
        st.write("The classified dataset contains ", runs, " classifications")

        #select the classification to use as benchmark
        benchmark = st.selectbox("Select the classification to use as benchmark", run_names)

        #select the classification(s) to compare with the benchmark
        compare = st.multiselect("Select the classification(s) to compare with the benchmark", run_names)

        #change format of compare into string
        compare_str = str(compare).replace("[", "").replace("]", "").replace("'", "")

        st.write ('Excellent!: I will compare: ', benchmark, ' with: ', compare_str)

        #crate a loop where for each item of the results, check if the benchmark is the same as the classification
        #if yes add 1 to the benchmark counter

        ##note importanti:
        # non esiste un concetto di training, il modello assegna la classe in base a quello che già sa
        # poiché in questi modelli non ho una misura della probabilità di assegnazione di una classe, non posso calcolare la precisione
        # ma solo l'accuratezza
        # l'accuratezza è il numero di classificazioni corrette diviso il numero totale di classificazioni

        #st.write ('Nota metodologica importante: poiché in questi modelli non ho una misura della probabilità di assegnazione di una classe, non posso calcolare la precisione ma solo l\'accuratezza. L\'accuratezza è il numero di classificazioni corrette diviso il numero totale di classificazioni')
        #translate the above in english
        st.write ('Important methodological note: since in these models do not provide a measure of the probability of assigning a class, it is not possible to calculate the precision but only the accuracy. The accuracy is the number of correct classifications divided by the total number of classifications')


