import streamlit as st
from ollama import Client
import concurrent.futures
import os
import pandas as pd

# Initialize Ollama client
client = Client(host='http://ollama:11434')

# UI Configuration with English comments
st.set_page_config(page_title="AI Forensics Lab", page_icon="🕵️‍♀️", layout="wide")
st.title("🕵️‍♀️ AI Text Forensics: xeniabrunel.com")
st.markdown("**Parallel Model Comparison: Llama 3 vs Mistral**")
st.markdown("---")

# User text input
text_input = st.text_area("Paste the text for analysis:", height=250, placeholder="Enter text here...")

# Function to analyze with a specific model
def analyze_with_model(model_name, text):
    try:
        response = client.generate(
            model=model_name, 
            prompt=f"Analyze if this text is AI-generated. Provide a score 0-100% and brief explanation: {text}"
        )
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

# Analysis button logic
if st.button("🚀 Start Deep Analysis", use_container_width=True):
    if text_input:
        with st.spinner('Both AI models are analyzing...'):
            # Parallel execution for both models
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future_llama = executor.submit(analyze_with_model, 'llama3', text_input)
                future_mistral = executor.submit(analyze_with_model, 'mistral', text_input)
                
                llama_result = future_llama.result()
                mistral_result = future_mistral.result()
            
            # Display results in two columns
            st.subheader("📊 Analysis Results")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🦙 Llama 3")
                st.info(llama_result)
            
            with col2:
                st.markdown("### 🌟 Mistral")
                st.success(mistral_result)
            
            st.balloons()
    else:
        st.warning("Please enter some text.")

# --- SECURE ADMIN BLOCK ---
st.markdown("---")
st.subheader("🛠 Brunel Training Lab")

with st.expander("🔐 Access Secure Upload Area"):
    access_code = st.text_input("Enter Secret Access Code:", type="password")
    SECRET_PASSWORD = "Brunel_2026" 

    if access_code == SECRET_PASSWORD:
        st.success("✅ Access Granted")
        uploaded_file = st.file_uploader("Choose a CSV file to expand the brain", type="csv")
        
        if uploaded_file is not None:
            if st.button("Merge to Main Dataset"):
                try:
                    UPLOAD_DIR = "datasets/uploads"
                    MAIN_DATASET = "datasets/AI_Human.csv"
                    os.makedirs(UPLOAD_DIR, exist_ok=True)
                    
                    temp_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    new_data = pd.read_csv(temp_path)
                    main_data = pd.read_csv(MAIN_DATASET)
                    
                    combined = pd.concat([main_data, new_data], ignore_index=True)
                    combined.to_csv(MAIN_DATASET, index=False)
                    
                    st.success(f"Verified! New total dataset size: {len(combined)} rows.")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error merging data: {e}")
    elif access_code != "":
        st.error("❌ Access Denied: Incorrect Secret Code!")
