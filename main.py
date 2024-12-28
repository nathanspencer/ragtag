import streamlit as st
import sqlite3
import pandas as pd
import chromadb

#vectordb
client = chromadb.PersistentClient(path=r"C:\Users\nls08\VirtualEnvironments\ragtag") 
collection_name = "brotherhood_of_steel"
collection = client.get_or_create_collection(collection_name)

st.set_page_config(
    page_title="Lore Explore",
    page_icon="☣️",
)

# Page layout
st.title("☣️ Lore Explore")

# Initialize session state to store query results
if 'results' not in st.session_state:
    st.session_state['results'] = None

# Input form
with st.form("query_form"):
    user_input = st.text_input("Enter question:")
    n_results = st.number_input("Number of results", min_value=1, step=1, value=5)
    submit_button = st.form_submit_button("Search")

# Process form submission
if submit_button:
    # Simulate querying a database (replace this with actual ChromaDB query logic)
    response = collection.query(
        query_texts=[user_input], # Chroma will embed this for you
        n_results=n_results # how many results to return
        )

    # Convert distances to similarity percentages
    def cosine_distance_to_similarity_percentage(distance):
        cosine_similarity = 1 - distance
        return ((cosine_similarity + 1) / 2) * 100

    distances = response['distances'][0]
    similarities = [cosine_distance_to_similarity_percentage(d) for d in distances]

    # Store results in session state
    results = zip(response['ids'][0], response['documents'][0], similarities)
    st.session_state['results'] = list(results)

if st.session_state['results']:
    for doc_id, doc, similarity in st.session_state['results']:
        st.write(f"**ID**: {doc_id} | **Similarity**: {similarity:.2f}%")
        st.write(f"Document: {doc}")