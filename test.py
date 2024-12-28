import streamlit as st

# Inject custom CSS
st.markdown(
    """
    <style>
    /* Background styling */
    body {
        background-color: #002b36; /* Dark Pip-Boy background color */
        color: #00ff00; /* Neon green text color */
        font-family: 'Courier New', monospace; /* Monospaced font */
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-thumb {
        background: #00ff00;
        border-radius: 10px;
    }
    
    /* Input box styling */
    .stTextInput, .stNumberInput {
        border: 1px solid #00ff00 !important;
        background-color: #001f27 !important;
        color: #00ff00 !important;
    }
    
    /* Button styling */
    button {
        background-color: #001f27;
        border: 1px solid #00ff00;
        color: #00ff00;
    }
    button:hover {
        background-color: #003540;
        border-color: #00ff00;
        color: #00ff00;
    }
    
    /* Section dividers */
    .stDivider {
        border-top: 2px solid #00ff00 !important;
    }

    /* Result boxes */
    .stMarkdown {
        border: 1px solid #00ff00;
        padding: 10px;
        background-color: #001f27;
        box-shadow: 0 0 10px #00ff00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app content
st.title("Pip-Boy Style App")
st.write("Welcome to the Pip-Boy inspired interface. Enter your query below.")

# Example form
with st.form("query_form"):
    query = st.text_input("Enter your query:")
    n_results = st.number_input("Number of results", min_value=1, step=1, value=5)
    submit_button = st.form_submit_button("Search")

if submit_button:
    st.success("Query submitted!")  # Example feedback
    # Example result
    st.write("**Example Result**: This is an example document styled like the Pip-Boy.")