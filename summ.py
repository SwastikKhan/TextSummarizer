import streamlit as st
from transformers import pipeline
from gemini import get_response_from_model
from streamlit_lottie import st_lottie  # type: ignore
import time

# Initialize summarization pipeline
summarizer = pipeline("summarization")


def summarize(text):
  summary = summarizer(text, max_length=100, min_length=30, truncation=True)
  return summary[0]['summary_text']

API_KEY=""
API_KEY=st.sidebar.text_input("Gemini API Key",key="gemini_api_key", type="password")
st.sidebar.markdown("[Click here to get API key](https://cloud.google.com/generative-ai-studio)")

st.title(":rainbow[Text Summarizer]")
st.write("A summarizer is something that condenses information into a shorter, key point version.")
url = "https://lottie.host/0d101b00-8268-4284-ab5e-159a701355d3/3T30KL4l9w.json"
if API_KEY=="":
  st.warning("Please enter API key")
else:
  user_text=st.text_area("Enter your text here")
  

  if st.button("Summarize"):
    
    if user_text:
      summary = get_response_from_model(user_text, API_KEY)
      st.markdown(f"""
    <div class="summary-box">
    <h3>Summary:</h3>
    <p>{summary}</p>
    </div>
    """, unsafe_allow_html=True)
      
    else:
      st.error("Please enter some text to summarize.")
    


