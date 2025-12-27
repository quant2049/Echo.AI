import streamlit as st  

st.title("🎈 Echo Journal")
st.write("Your AI  Journal")
audio_value = st.audio_input("Record a voice message")
if audio_value:
    st.audio(audio_value)