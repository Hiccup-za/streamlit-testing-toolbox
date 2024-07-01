import pandas as pd
import streamlit as st

from data import Generated_Data
from functions import add_test_result_random, reset_test_results, calculate_cumulative_sum, display_metrics

# Set Streamlit page configuration
st.set_page_config(
    page_title="Generate Test Data",
    page_icon="🪄",
    layout="wide"
)

st.title('🪄 Generate Test Data')

# Initialize session state for generated data
if "generated_data" not in st.session_state:
    st.session_state.generated_data = Generated_Data

# Define columns for buttons
col1, col2 = st.columns(2)

# Add Random Test Result button
with col1:
    if st.button("✨ Add Random Test Result", key="add_random_test_result", type="secondary"):
        try:
            add_test_result_random(st.session_state.generated_data)
        except Exception as e:
            st.error(f"Error adding test result: {e}")

# Reset Test Results button
with col2:
    if st.button("🫧 Reset Test Results", key="reset_test_results", type="secondary"):
        try:
            reset_test_results()
        except Exception as e:
            st.error(f"Error resetting test results: {e}")

# Placeholder for messages
message_placeholder = st.empty()

# Display message if exists in session state
if "message" in st.session_state:
    message_placeholder.info(st.session_state.message)
    del st.session_state.message

# Display metrics
display_metrics(st.session_state.generated_data)

# Calculate and display cumulative sum
try:
    cumulative_sum = calculate_cumulative_sum(st.session_state.generated_data)
    chart_data = pd.DataFrame({"cumulative_sum": cumulative_sum})
    st.line_chart(chart_data)
except Exception as e:
    st.error(f"Error calculating cumulative sum: {e}")

# Display generated data in a dataframe
st.dataframe(st.session_state.generated_data, use_container_width=True)
