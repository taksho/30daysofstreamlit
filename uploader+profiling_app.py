import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.title('st.file_uploader + component')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('Streamlit Pandas Profiling')
  pr = df.profile_report()
  st_profile_report(pr)
else:
  st.info('☝️ Upload a CSV file')