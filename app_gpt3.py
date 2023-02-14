import streamlit as st
import openai
import os
import json
from PIL import Image
import pandas as pd

#
image_path = "image.jpg"
image = Image.open(image_path)
#


def preprocess_function(text_path,content_type = None ):
    prompt=f"Generate  Multiple Questions and Answers from the context provided.\n\nContext :{text_path}\n\n"
    return prompt

# 
def predict_function(prompt,key): 
    print(prompt)
    openai.api_key = key
    print(key)
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
@st.experimental_singleton
def model_load_function(model_path=None):
    #
    print("loading model...")
    #retrive api key from json file
    with open("openai_api_key.json") as f:
        api_key = json.load(f)
    print("Your API key is: ", api_key['API_KEY'])
    #
    key= api_key['API_KEY']
    print("model was loaded")
    return key
#
st.image(image, caption='Question & Answer Generator')
st.write("""## ⚡️ Question & Answer Generator App ⚡️""")

query = st.text_input("Enter the Context here.", "")

if query != "":
    with st.spinner(text="Initializing the Model...It might take a while..."):
        key = model_load_function()
    with st.spinner(text="Preprocessing the Context...It might take a while..."):
        data = preprocess_function(query)
    with st.spinner(text="Making Predictions...It might take a while..."):    
        predictions = predict_function(data,key)

    with st.spinner(text="Questions & Answers Generated 🚀🚀🚀"):
        st.text(predictions) 