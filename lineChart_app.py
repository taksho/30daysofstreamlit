import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

source = data.stocks()

st.line_chart(chart_data)


st.line_chart(
    source,
    x='date',
    y='price',
)

st.header('Line chart using Altair')

c = alt.Chart(source).mark_line().encode(
    x='date',
    y='price',
    color='symbol',
    strokeDash='symbol',
)

st.altair_chart(c, use_container_width=True)
