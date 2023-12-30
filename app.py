import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

st.title("Medium Article Generator")
topic = st.text_input("Enter the topic of the article")