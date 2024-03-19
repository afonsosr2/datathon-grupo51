import streamlit as st
import pandas as pd
import numpy as np
from plotly import express as px
from plotly import graph_objs as go

###### Páginal Inicial do Streamlit ######
st.set_page_config(layout= 'wide')

cols = st.columns(6, gap="large")
with cols[0]:
    st.image("images/Passos-magicos-icon-cor.png")
with cols[1]:
    if st.button("Home"):
        st.switch_page("home.py")
with cols[2]:
    if st.button("PSE (2020)"):
        st.switch_page("pages/PSE (2020).py")
with cols[3]:
    if st.button("Sobre"):
        st.switch_page("pages/MVP (sobre).py")
with cols[4]:
    if st.button("Referências"):
        st.switch_page("pages/Referências.py")

st.header("", divider="gray")

st.header(":footprints: Análise dos dados da ONG Passos Mágicos")

