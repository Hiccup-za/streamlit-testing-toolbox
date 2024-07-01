import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏡",
    layout="wide"
)

st.title('🏡 Home')

st.subheader('Welcome to my collection of Streamlit apps.')

container1 = st.container(border=True)
container1.subheader('🎛️ Config Selector')

container2 = st.container(border=True)
container2.subheader('💫 Dashboard')

container3 = st.container(border=True)
container3.subheader('🪄 Generate')