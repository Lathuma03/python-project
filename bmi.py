import streamlit as st

st.set_page_config(page_title="BMI CALCULATOR", page_icon=":white_flower:", layout="wide")

st.title("BMI CALCULATOR")
st.header("A webpage to calculate Body Mass Index of a Person")

name = st.text_input("Enter Your name", "")
if st.button('Submit Name'):
    result = name.title()
    st.success(f"Hello, {result}!")

gender = st.radio("What is your Gender?", ('Female', 'Male', 'Transgender'))
st.success(gender)

age = st.number_input("Enter your Age:", min_value=0, max_value=150)
add = st.text_input("Enter your Address:")

hobbies = []
if st.checkbox("Dancing"):
    hobbies.append("Dancing")
if st.checkbox("Music"):
    hobbies.append("Music")
if st.checkbox("Watching Movies"):
    hobbies.append("Watching Movies")
if st.checkbox("Exercise"):
    hobbies.append("Exercise")
if st.checkbox("Gaming"):
    hobbies.append("Gaming")

weight = st.number_input("Enter your weight (in kgs)", min_value=0.0)
status = st.radio('Select your height format:', ('cms', 'meters', 'feet'))

if status == 'cms':
    height = st.number_input('Centimeters', min_value=0.0)
    height_in_meters = height / 100
elif status == 'meters':
    height = st.number_input('Meters', min_value=0.0)
    height_in_meters = height
else:
    height = st.number_input('Feet', min_value=0.0)
    height_in_meters = height / 3.28

if st.button('Calculate BMI'):
    if height_in_meters > 0:
        bmi = weight / (height_in_meters ** 2)
        st.text(f"Your BMI Index is {bmi:.2f}.")
        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Healthy")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        else:
            st.error("Extremely Overweight")
    else:
        st.error("Please enter a valid height.")
