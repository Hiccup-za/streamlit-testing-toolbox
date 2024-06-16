import pandas as pd
import streamlit as st
from data import Feature1, Feature2, Feature3, Feature4
from functions import calculate_cumulative_sum, display_metrics

st.title('💫 Dashboard')

option = st.selectbox(
    "Which feature would you like to view?",
    ("🔖 Feature 1", "🤖 Feature 2", "🐙 Feature 3", "🐉 Feature 4"),
    label_visibility="hidden",
    index=None,
    placeholder="Select a feature...",
    )

if option == "🔖 Feature 1":
    st.header('🔖 Feature 1', divider='grey')
    display_metrics(Feature1)

    cumulative_sum = calculate_cumulative_sum(Feature1)
    chart_data = pd.DataFrame({"cumulative_sum": cumulative_sum})
    st.line_chart(chart_data)

elif option == "🤖 Feature 2":
    st.header('🤖 Feature 2', divider='grey')
    display_metrics(Feature2)

    cumulative_sum = calculate_cumulative_sum(Feature2)
    chart_data = pd.DataFrame({"cumulative_sum": cumulative_sum})
    st.line_chart(chart_data)

elif option == "🐙 Feature 3":
    st.header('🐙 Feature 3', divider='grey')
    display_metrics(Feature3)

    cumulative_sum = calculate_cumulative_sum(Feature3)
    chart_data = pd.DataFrame({"cumulative_sum": cumulative_sum})
    st.line_chart(chart_data)

elif option == "🐉 Feature 4":
    st.header('🐉 Feature 4', divider='grey')
    display_metrics(Feature4)

    cumulative_sum = calculate_cumulative_sum(Feature4)
    chart_data = pd.DataFrame({"cumulative_sum": cumulative_sum})
    st.line_chart(chart_data)