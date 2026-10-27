import os
from apikey import apikey
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.globals import set_debug

os.environ["OPENAI_API_KEY"] = apikey
st.title("Enter your question")
topic = st.text_input("Input your topic of interest")
language = st.text_input("Provide language")
#topic = "what is the capitol of America?"
llm = ChatOpenAI(model="gpt-4o", temperature=0.9)

title_template = PromptTemplate(
    input_variables = ['topic', 'language'],
    template = 'Give me a short article topic on {topic} in language {language} in a single line'
)
chain = title_template | llm | StrOutputParser()
if topic:
    set_debug(True)
    response = chain.invoke({"topic": topic, "language": language})
    print(response)
    st.write(response)
