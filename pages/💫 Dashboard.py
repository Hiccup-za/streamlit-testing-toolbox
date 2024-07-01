import pandas as pd
import streamlit as st
from data import Feature1, Feature2, Feature3, Feature4
from functions import calculate_cumulative_sum, display_metrics

st.set_page_config(
    page_title="Dashboard",
    page_icon="💫",
    layout="wide"
)

st.title('💫 Dashboard')

option = st.selectbox(
    "?",
    ("🔖 Feature 1", "🤖 Feature 2", "🐙 Feature 3", "🐉 Feature 4"),
    label_visibility="hidden",
    index=None,
    placeholder="Select a feature...",
)

# Mapping options to features and headers
features = {
    "🔖 Feature 1": Feature1,
    "🤖 Feature 2": Feature2,
    "🐙 Feature 3": Feature3,
    "🐉 Feature 4": Feature4
}

headers = {
    "🔖 Feature 1": '🔖 Feature 1',
    "🤖 Feature 2": '🤖 Feature 2',
    "🐙 Feature 3": '🐙 Feature 3',
    "🐉 Feature 4": '🐉 Feature 4'
}

if option in features:
    st.header(headers[option], divider='grey')
    display_metrics(features[option])

    cumulative_sum = calculate_cumulative_sum(features[option])
    chart_data = pd.DataFrame({"cumulative_sum": cumulative_sum})
    st.line_chart(chart_data)
