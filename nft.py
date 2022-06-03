import streamlit as st
import request, json


endpoint = st.sidebar.selectbox("Endpoints", ['Assets', 'Events', 'Rarity'])
st.header(f"OpenSea NFT API Explorer - {endpoint}")

st.write("")
st.sidebar.write("")
