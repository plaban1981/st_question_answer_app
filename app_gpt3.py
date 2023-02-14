import streamlit as st
from streamlit import secrets
import openai
import os
import json
from PIL import Image
import pandas as pd

#
image_path = "image.jpg"
image = Image.open(image_path)
#
api_key = secrets["API_KEY"]
openai.api_key = api_key
print(api_key)
#

def preprocess_function(text_path,content_type = None ):
    prompt=f"Generate  Multiple Questions and Answers from the context provided.\n\nContext :{text_path}\n\n"
    return prompt

# 
@st.cache
def predict_function(prompt): 
    print(prompt)
    response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=300,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
    answer = response.choices[0].text
    print(answer)
    return answer
   
#
st.image(image, caption='Question & Answer Generator')
st.write("""## ⚡️ Question & Answer Generator App ⚡️""")

query = st.text_input("Enter the Context here.", "")

if query != "":
    with st.spinner(text="Preprocessing the Context...It might take a while..."):
        data = preprocess_function(query)
    with st.spinner(text="Making Predictions...It might take a while..."):    
        predictions = predict_function(data)

    with st.spinner(text="Questions & Answers Generated 🚀🚀🚀"):
        st.text(predictions) 
