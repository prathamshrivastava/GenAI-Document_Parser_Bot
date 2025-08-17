#imports 

import os
from dotenv import load_dotenv
import json
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.prompts import PromptTemplate

load_dotenv()
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", google_api_key = os.getenv("GOOGLE_API_KEY"))

PROMPT_TEMPLATE = '''
You are a Expert of resume parser, go through the file and return the following details:

Return first which languages does this person speaks.

{{
"Name: ": "..."
"Age: ": "..."
"Experience: ": "..."
"Education: ": "..."
"Projects: ": "..."
"Languages: ": "..."
}}

Rules:
- if a field is not known set it to No idea
- Return only valud Json(no extra commentry)
Result:
{Text}

'''
promt = PromptTemplate(template = PROMPT_TEMPLATE, input_variables=["Text"])

def load_resume_file(uploaded_file):
    temp_path = f"temp_{uploaded_file.name}"

    with open(temp_path,"wb") as f:
        f.write(uploaded_file.getbuffer())

    if uploaded_file.name.endswith('.pdf'):
        loader = PyPDFLoader(temp_path)
    
    elif uploaded_file.name.endswith('.docx'):
        loader = Docx2txtLoader(temp_path)
    
    elif uploaded_file.name.endswith('.txt'):
        loader = TextLoader(temp_path)
    
    else:
        return None
    
    return loader.load()

def main():
    st.set_page_config(page_title= "Resume Parser", page_icon= '', layout='centered')
    st.title("Resume Praser - Langchain")

    uploaded_file = st.file_uploader("Uploaded Resume", type = ["pdf","txt","docx"])

    if uploaded_file:
        with st.spinner("Loading Resume..."):
            docs = load_resume_file (uploaded_file)
            if not docs:
                st.error("Unsupported File type")
                return
            

        st.subheader("Extracted Text (preview)")
        preview_text = "\n\n".join([d.page_content for d in docs])[:40000]
        st.text_area("Preview", value = preview_text, height= 200)

        if st.button("Ask LLM"):
            with st.spinner("Sending to LLm..."):
                formated_promt = promt.format(Text = preview_text)
                response = llm.invoke(preview_text)
            
                st.write(response.content)

                try:
                    parsed_json = json.loads(response.content)
                    st.json(parsed_json)
                except json.JSONDecodeError:
                    st.write(response.content)


        

if __name__ == "__main__":
    main()