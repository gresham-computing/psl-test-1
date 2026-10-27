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
#topic = "what is the capitol of America?"
llm1 = ChatOpenAI(model="gpt-4o", temperature=0.9)
llm2 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

title_template = PromptTemplate(
    input_variables = ['topic', 'language'],
    template = 'Give me a short article topic on {topic} in a single line'
)
article_template= PromptTemplate(
    input_variables = ['title'],
    template = 'Give me a small article contents with {title} in 4-5 lines'
)

title_chain = title_template | llm1 | StrOutputParser()
article_chain = article_template | llm2 | StrOutputParser()
overall_chain = title_chain | article_chain
if topic:
    set_debug(True)
    #response = overall_chain.invoke({"topic": topic})
    #st.write(response)
    title_response = title_chain.invoke({"topic": topic})
    article_response = article_chain.invoke({"title": title_response})
    st.write("Title:", title_response)
    st.write("Article:", article_response)
