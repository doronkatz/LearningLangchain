import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI

load_dotenv()

os.environ['OPENAI_API_KEY'] =  os.getenv('API_KEY')

st.title("Medium Article Generator")
topic = st.text_input("Enter the topic of the article")

llm = OpenAI(temperature=0.9)

if (topic):
    response = llm(topic)
    st.write(response)
