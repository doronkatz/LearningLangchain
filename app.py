import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


load_dotenv()

os.environ['OPENAI_API_KEY'] =  os.getenv('API_KEY')

st.title("Medium Article Generator")
topic = st.text_input("Enter the topic of the article")
title_template = PromptTemplate(
    input_variables=['topic', 'language'],
    template='Give me medium article title on {topic} in {language}'
)

llm = OpenAI(temperature=0.9)

if (topic):
    response = llm(title_template.format(topic=topic, language='english'))
    st.write(response)
