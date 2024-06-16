import streamlit as st

st.title('🏠 Home')

with st.container():
    prompt = st.chat_input("✨ Ask AI for metrics on a specific feature...")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")