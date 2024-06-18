import random
import streamlit as st

def add_test_result_random(feature_data):
    new_result = random.choice(["✅ Pass", "🔴 Fail"])
    feature_data.append(new_result)
    st.session_state.message = f"✨ New result generated: {new_result}"

def calculate_metrics(feature_data):
    filtered_results = [results for results in feature_data if not results.startswith("#")]

    pass_count = filtered_results.count("✅ Pass")
    fail_count = filtered_results.count("🔴 Fail")
    total_count = pass_count + fail_count

    if total_count == 0:
        pass_percentage = 100
    else:
        pass_percentage = (pass_count / total_count) * 100
    return pass_count, fail_count, total_count, pass_percentage

def calculate_cumulative_sum(feature_data):
    filtered_results = [results for results in feature_data if not results.startswith("#")]

    cumulative_sum = [0]
    current_value = 0
    for result in filtered_results:
        if result == "✅ Pass":
           current_value += 1
        elif result == "🔴 Fail":
            current_value -= 1
        cumulative_sum.append(current_value)
    return cumulative_sum

def display_metrics(feature_data):
    pass_count, fail_count, total_count, pass_percentage = calculate_metrics(feature_data)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("⚙️ :blue[**Pass Rate**]", f"{pass_percentage:.1f}%", delta=f"{-fail_count} Fails")
    col2.metric("#️⃣ :grey[**Count**]", total_count)
    col3.metric("⬆️ :green[**Pass Count**]", pass_count)
    col4.metric("⬇️ :red[**Fail Count**]", fail_count)

def reset_test_results():
    st.session_state.generated_data = []
    st.session_state.message = "🫧 Test results have been reset"