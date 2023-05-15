import streamlit as st
from general_functions import get_env
from openai_functions import ai_complete
from create_dataset import create_dataset

st.write("Welcome to GPTROC")

##launch dataset creation
create_dataset()

