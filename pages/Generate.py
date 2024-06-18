import pandas as pd
import streamlit as st

from data import Generated_Data
from functions import add_test_result_random, reset_test_results, calculate_cumulative_sum, display_metrics

st.title('🪄 Generate Test Data')

if "generated_data" not in st.session_state:
    st.session_state.generated_data = Generated_Data

col1, col2 = st.columns(2)

with col1:
    if st.button("✨ Add Random Test Result", key="add_random_test_result", type="secondary"):
        add_test_result_random(st.session_state.generated_data)
    
with col2:
    if st.button("🫧 Reset Test Results", key="reset_test_results", type="secondary"):
        reset_test_results()

message_placeholder = st.empty()

if "message" in st.session_state:
    message_placeholder.info(st.session_state.message)
    del st.session_state.message

display_metrics(st.session_state.generated_data)
cumulative_sum = calculate_cumulative_sum(st.session_state.generated_data)
chart_data = pd.DataFrame({"cumulative_sum": cumulative_sum})
st.line_chart(chart_data)