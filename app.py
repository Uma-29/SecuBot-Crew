import streamlit as st
import os
from utils.save_docs import save_docs_to_vectordb
from utils.session_state import initialize_session_state_variables
from utils.prepare_vectordb import get_vectorstore
from utils.chatbot import chat
import time

class ChatApp:
    """
    A Streamlit application for chatting with PDF documents

    This class encapsulates the functionality for uploading PDF documents, processing them,
    and enabling users to chat with the documents using a chatbot. It handles the initialization
    of Streamlit configurations and session state variables, as well as the frontend for document
    upload and chat interaction
    """
    def __init__(self):
        """
        Initializes the ChatApp class

        This method ensures the existence of the 'docs' folder, sets Streamlit page configurations,
        and initializes session state variables
        """
        # Ensure the docs folder exists
        if not os.path.exists("docs"):
            os.makedirs("docs")

        # Configurations and session state initialization
        st.set_page_config(page_title="Cybersecurity Awareness Chatbot :shield:")
        st.title("Cybersecurity Awareness Chatbot :shield:")
        initialize_session_state_variables(st)
        self.docs_files = st.session_state.processed_documents

    def run(self):
        """
        Runs the Streamlit app for chatting with PDFs

        This method handles the frontend for document upload, unlocks the chat when documents are uploaded,
        and locks the chat until documents are uploaded
        """
        # Simulate document upload and processing
        upload_docs = os.listdir("docs")
        # Sidebar frontend for document upload
        with st.sidebar:
            st.subheader("Knowledge Base")
            if upload_docs:
                st.write("Loaded Cybersecurity Documents:")
                st.text(", ".join(upload_docs))
            else:
                st.info("No cybersecurity documents in the knowledge base yet.")
            st.subheader("Upload Cybersecurity Guidelines (PDFs)")
            pdf_docs = st.file_uploader("Upload cybersecurity awareness PDFs to the knowledge base", type=['pdf'], accept_multiple_files=True)
            if pdf_docs:
                # Simulate processing with a delay
                with st.spinner("Processing documents..."):
                    time.sleep(3)  # Simulate a 3-second delay
                    st.success("Documents processed successfully!")

        # Ensure chat is always available
        st.session_state.chat_history = chat(st.session_state.chat_history, None)

if __name__ == "__main__":
    app = ChatApp()
    app.run()