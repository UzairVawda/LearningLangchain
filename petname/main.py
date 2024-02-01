import helper
import streamlit as st

st.title("Pet Name Generator")

animalColor = None;
animalDetails = None;

animalType = st.sidebar.text_input(label="What type of pet do you have?", max_chars=15)
if animalType: animalColor = st.sidebar.text_input(label=f"What color is your {animalType}?", max_chars=15)
if animalColor: animalDetails = st.sidebar.text_area(label=f"Any additional details about your new {animalType}?", max_chars=150)

if (animalColor):
    results = helper.generateNames(animalType, animalColor, animalDetails)
    print (results) 
    st.text(results['petName'])