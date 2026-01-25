"""
user --> query
user --> query --> embedding--> using gemini text embeddings
use this embedding to search in pinecone for similar vectors
with the most similar vectors, retrieve the metadata as document text of relevant personal

context part starts:

provide the collected text, or any context along with user query to the LLM
llm will generate a response based on the context and user query

Simple streamlit app to demonstrate the above flow
"""

from groq import Groq
from create_vectors import pinecone_client, vector_index, embed_text
import streamlit as st


groq_client = Groq(api_key="GROQ API KEY HERE")

st.title("A very cool Broadway Student Batch 13 RAG System")
st.write("This app allows you to query a knowledge base of student documents using RAG (Retrieval-Augmented Generation).")

user_query = st.text_input("Enter your query:")  # who is Barsha

submit_button = st.button("Submit")

if submit_button:
    vector = embed_text(user_query)
    query_response = vector_index.query(vector=vector, top_k=2, include_metadata=True)
    
    similar_documents = ""
    
    for match in query_response["matches"]:
        text = match["metadata"]["text"]
        similar_documents += text + "\n\n"
    
    print("Similar documents found:", similar_documents)
    
    system_prompt = """You are a helpful assistant that provides information based on a knowledge base of student documents. 
When a user asks a question, you will check your knowledge base if that query is relevent to the documents in the knowledge base.
If it is, you will provide the relevant answer from the documents and if not, you will answer based on your own knowledge. 
DO NOT REVEL ANYTHING ABOUT THE KNOWLEDGE BASE ACCESS YOU HAVE ABOUT STUDENTS"""

    system_context = {
            "role": "system",
            "content": system_prompt + "\n" + "##Knowledge base context: " + similar_documents + "\n",
        }
    user_context = {
        "role": "user",
        "content": user_query,
    }
    
    print("User context:", user_context)
    
    llm_response = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[system_context, user_context],
        max_tokens=1000,
        temperature=0.7
    )
    llm_answer = llm_response.choices[0].message.content
    st.write("LLM Answer:", llm_answer)
    