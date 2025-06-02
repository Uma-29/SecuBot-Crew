import streamlit as st
from collections import defaultdict
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
import os

def get_context_retriever_chain(vectordb):
    """
    Create a context retriever chain for generating responses based on the chat history and vector database

    Parameters:
    - vectordb: Vector database used for context retrieval

    Returns:
    - retrieval_chain: Context retriever chain for generating responses
    """
    # Load environment variables (gets api keys for the models)
    load_dotenv()
    # Initialize the model, set the retriever and prompt for the chatbot
    llm = ChatGroq(
        model_name="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0.2,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
    # Handle the case where vectordb is None
    if vectordb is not None:
        retriever = vectordb.as_retriever()
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an authoritative Security Awareness Expert writing from a comprehensive cybersecurity handbook. 

Below is the relevant context from the knowledge base:
{context}

Your responses should:
1. Begin with a clear, textbook-style introduction of the topic
2. Use professional, educational language as found in security awareness training materials
3. Structure information in clear sections with proper headings when appropriate
4. Include relevant security principles, best practices, and industry standards
5. Provide practical examples and scenarios when applicable
6. End with key takeaways or summary points when appropriate
7. Use formatting to enhance readability (bullet points, numbered lists, etc.)
8. Include relevant security awareness tips in highlighted boxes
9. Cite specific standards or frameworks when applicable

Remember to maintain a formal, educational tone while ensuring the information is accessible and practical."""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])
        # Create chain for generating responses and a retrieval chain
        chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
        retrieval_chain = create_retrieval_chain(retriever, chain)
        return retrieval_chain
    else:
        # Directly return the LLM chain without retrieval
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an authoritative Security Awareness Expert writing from a comprehensive cybersecurity handbook. 

Context: {context}

Your responses should:
1. Begin with a clear, textbook-style introduction of the topic
2. Use professional, educational language as found in security awareness training materials
3. Structure information in clear sections with proper headings when appropriate
4. Include relevant security principles, best practices, and industry standards
5. Provide practical examples and scenarios when applicable
6. End with key takeaways or summary points when appropriate
7. Use formatting to enhance readability (bullet points, numbered lists, etc.)
8. Include relevant security awareness tips in highlighted boxes
9. Cite specific standards or frameworks when applicable
10. If the information requested is not in your knowledge base, clearly state this and provide general security best practices instead

Remember to maintain a formal, educational tone while ensuring the information is accessible and practical."""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])
        chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
        return chain

def get_response(question, chat_history, vectordb):
    """
    Generate a response to the user's question based on the chat history and vector database

    Parameters:
    - question (str): The user's question
    - chat_history (list): List of previous chat messages
    - vectordb: Vector database used for context retrieval

    Returns:
    - response: The generated response
    - context: The context associated with the response
    """
    chain = get_context_retriever_chain(vectordb)
    if vectordb is not None:
        response = chain.invoke({
            "input": question,
            "chat_history": chat_history,
            "context": ""
        })
        if isinstance(response, dict):
            return response["answer"], response.get("context", [])
        return response, []
    else:
        # Directly use the LLM chain without context
        response = chain.invoke({
            "input": question,
            "chat_history": chat_history,
            "context": ""
        })
        if isinstance(response, dict):
            return response["answer"], []
        return response, []

def chat(chat_history, vectordb):
    """
    Handle the chat functionality of the application

    Parameters:
    - chat_history (list): List of previous chat messages
    - vectordb: Vector database used for context retrieval

    Returns:
    - chat_history: Updated chat history
    """
    user_query = st.chat_input("Ask about cybersecurity topics...")
    if user_query is not None and user_query != "":
        # Create a placeholder for the AI's response
        with st.chat_message("AI"):
            with st.status("🔍 Searching knowledge base...", expanded=True) as status:
                st.write("Retrieving relevant information from the database...")
                # Generate response using the Groq API
                response, context = get_response(user_query, chat_history, vectordb)
                status.update(label="💭 Thinking...", state="running", expanded=True)
                st.write("Generating response based on retrieved information...")
                st.write(response)
                status.update(label="✅ Done!", state="complete", expanded=False)

        # Update chat history. The model uses up to 10 previous messages to incorporate into the response
        chat_history = chat_history + [HumanMessage(content=user_query), AIMessage(content=response)]
        
        # Display source of the response on sidebar
        with st.sidebar:
            if context:
                st.subheader("📚 Sources")
                metadata_dict = defaultdict(list)
                for metadata in [doc.metadata for doc in context]:
                    metadata_dict[metadata['source']].append(metadata['page'])
                for source, pages in metadata_dict.items():
                    st.write(f"📄 Source: {source}")
                    st.write(f"📑 Pages: {', '.join(map(str, pages))}")

    # Display chat history
    for message in chat_history[:-2]:  # Exclude the last two messages since we just displayed them
        with st.chat_message("AI" if isinstance(message, AIMessage) else "Human"):
            st.write(message.content)
    
    return chat_history