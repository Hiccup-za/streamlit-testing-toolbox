import streamlit as st

st.title('🏡 Home')

multi = '''
Welcome to my Testing Dashboard App.
'''
st.markdown(multi)


st.subheader('💫 Dashboard')

multi = '''
Use the drop down to view static data for each of the four features:


🔖 Feature 1 - Out of 10 tests, :orange[5 have failed] and :orange[5 have passed].  
🤖 Feature 2 - Out of 10 tests, :red[10 have failed] and :red[0 have passed].  
🐙 Feature 3 - Out of 10 tests, :green[0 have failed] and :green[10 have passed].  
🐉 Feature 4 - Out of 10 tests, :orange[6 have failed] and :orange[4 have passed].
'''
st.markdown(multi)

st.subheader('🪄 Generate')

multi = '''
Generate random test result data.

The :blue[metric widgets] as well as the :blue[line chart] will update as test result data is generated.  
You can reset the test result data at any time.
'''
st.markdown(multi)