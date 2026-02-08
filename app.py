import streamlit as st
from ollama import Client

# Initialize Ollama client
client = Client(host='http://ollama:11434')

# UI Configuration with English comments
st.set_page_config(page_title="AI Forensics Lab", page_icon="🕵️‍♀️")
st.title("🕵️‍♀️ AI Text Forensics: xeniabrunel.com")
st.markdown("---")

# User text input
text_input = st.text_area("Paste the text for analysis:", height=250, placeholder="Enter text here...")

# Analysis button logic
if st.button("🚀 Start Deep Analysis", use_container_width=True):
    if text_input:
        with st.spinner('Llama 3 is analyzing linguistic patterns...'):
            try:
                # Requesting generation from Ollama
                response = client.generate(
                    model='llama3', 
                    prompt=f"Analyze if this text is AI-generated. Provide a score 0-100% and brief explanation: {text_input}"
                )
                st.subheader("Analysis Result")
                st.info(response['response'])
                st.balloons()
            except Exception as e:
                # Handle connection errors or model loading
                st.error("Engine is warming up. Please wait 30 seconds and try again.")
    else:
        st.warning("Please enter some text.")
