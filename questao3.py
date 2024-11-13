import streamlit as st
resposta = st.slider('Informe o grau de satisfação:', min_value=0, max_value=100)
st.write(str(resposta))
