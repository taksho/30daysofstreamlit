import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#3da9fc"
backgroundColor="#fffffe"
secondaryBackgroundColor="#d8eefe"
textColor="#272343"
font="leto"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)