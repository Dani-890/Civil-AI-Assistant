import streamlit as st

st.set_page_config(page_title="Civil AI Assistant", layout="wide")

st.title("🏗️ Civil AI Assistant")
st.write("Welcome to Civil AI Engineer")

st.header("Modules")

col1, col2 = st.columns(2)

with col1:
    st.button("🧱 Concrete Calculator")
    st.button("🦾 Steel BBS")

with col2:
    st.button("🌍 Earthwork")
    st.button("📄 Excel Reports")
