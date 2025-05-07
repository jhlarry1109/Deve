import streamlit as st

col1, col2 = st.columns([2, 3])
with col1:
  st.title("here is column1 title")

with col2:
  st.title("here is column2 title")
  st.checkbox("this is checkbox1 in col2 ")