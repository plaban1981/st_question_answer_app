import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
import json
#
image_path = "image.jpg"
image = Image.open(image_path)

st.set_page_config(page_title="Question Answer Generation App", layout="centered")
st.image(image, caption='Any To Any Language Translation')
#
# Create a dropdown menu with options
# page header
st.title(f"Question Answer Generation App")
with st.form("Translate"):
   text = st.text_input("Enter text here")
   submit = st.form_submit_button("Generate Question Answer")
   #
   if submit:    
        print(text)
        #
        context = []
        question = []
        #
        context.append(text)
        input = pd.DataFrame({'context': context})
        print(input)
        input.to_csv('input.csv', index=False) 
        os.chmod("input.csv", 0o777)
        # Faq Generation API
        url = "https://app.aimarketplace.co/api/marketplace/models/faq-generation-8e6665b1/predict/"
        payload={'data': open('input.csv','rb')}
        headers = {'Authorization': 'Api-Key MCrwooHy.M3L5LCVeW1j6QajhA4mGdNazTQajYreu'}

        response = requests.request("POST", url, headers=headers, files=payload)

        #print(type(response))
        #print(response.json()['output'])
        #print(response.text)
        #print(response.text.split("Predictions: [")[1].split("]")[0])
        print(type(response.text))
        #
        ques = response.text.split("Predictions: [")[1].split("]")[0]
        question.append(ques)
        input['question'] = question
        print(input)
        input.to_csv('input1.csv', index=False) 
        os.chmod("input1.csv", 0o777)
        # Question Answer Generation API
        url = "https://app.aimarketplace.co/api/marketplace/models/question-and-answer-generation-20d24f81/predict/"
        payload={'data': open('input1.csv','rb')}
        headers = {'Authorization': 'Api-Key tulO8i86.MKFyv3tqoUXdhzovKUJpJ4Ds2xEW06kq'}

        response = requests.request("POST", url, headers=headers, files=payload)

        print(response.text)
        answer = response.text.split("Answer is [")[1].split("]")[0]
        # output header
        st.header("Translated Text")
        # output results
        st.success(f"Question : {ques} Answer : {answer}")