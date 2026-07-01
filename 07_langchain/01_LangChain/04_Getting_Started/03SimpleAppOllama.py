# Simple GENAI App Using Ollama (GenAIAppWithOllama)
# - Run the Ollama model from the local machine and use it with the stremlit to call with the user's question

import os
from dotenv import load_dotenv # type: ignore
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)

## For LangSmith Tracking
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY") or os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT") or os.getenv("LANGCHAIN_PROJECT")
 
# Usually optional for hosted LangSmith, but safe to set
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")

## Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the questions asked."),
    ("user", "Question: {question}")
])

## Streamlit Framework
st.title("Langchain Demo With gemma2:2b Model")
input_text = st.text_input("What question you have in mind?")

## Ollama
llm = Ollama(model="gemma2:2b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))