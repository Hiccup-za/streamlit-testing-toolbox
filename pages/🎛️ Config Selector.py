import streamlit as st

st.set_page_config(
    page_title="Config Selector",
    page_icon="🎛️",
    layout="wide"
)

st.title('🎛️ Config Selector')

if st.button('🔄 Reset State'):
    st.session_state.active_dataset = "none"
    st.rerun()

col1, col2, col3 = st.columns(3)

# Initialize session state for the success and active dataset
st.session_state.setdefault('success', "✨ Data generated for ...")
st.session_state.setdefault('active_dataset', "none")

# Function to create dataset container
def create_dataset_container(column, color, title, details, dataset_key):
    with column:
        container = st.container(border=True)
        container.subheader(f':{color}[{title}]')
        container.markdown(details)
        if container.button(f':{color}[Select Config]'):
            st.session_state.success = "Config Active"
            st.session_state.active_dataset = dataset_key
            st.success(st.session_state.success, icon="✅")

# Dataset details
datasets = [
    {
        "column": col1,
        "color": "orange",
        "title": "Config 1",
        "details": "This is the :orange[first] config ☝️",
        "dataset_key": "config1"
    },
    {
        "column": col2,
        "color": "blue",
        "title": "Config 2",
        "details": "This is the :blue[second] config ✌️",
        "dataset_key": "config2"
    },
    {
        "column": col3,
        "color": "violet",
        "title": "Config 3",
        "details": "This is the :violet[third] config 🤘",
        "dataset_key": "config3"
    }
]

# Create containers for each dataset
for dataset in datasets:
    create_dataset_container(**dataset)

# Function to display the active dataset container
def display_active_dataset(dataset_key, color, title, content):
    container = st.container(border=True)
    container.subheader(f':{color}[{title}]')
    container.markdown(f':{color}[{content}]')

# Conditionally display the related container based on the active dataset
if st.session_state.active_dataset == "config1":
    display_active_dataset("config1", "orange", "First Config ☝️", "This is the content for the first config ☝️")
elif st.session_state.active_dataset == "config2":
    display_active_dataset("config2", "blue", "Second Config ✌️", "This is the content for the second config ✌️")
elif st.session_state.active_dataset == "config3":
    display_active_dataset("config3", "violet", "Third Config 🤘", "This is the content for the third config 🤘")
else:
    st.info("Select a config ...")