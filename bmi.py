import streamlit as st
st.set_page_config(page_title="BMI CALCULATOR",page_icon=":white_flower:",layout="wide")
st.title("BMI CALCULATOR")
st.header("A webpage to calculate Body Mass Index of a Person")
name = st.text_input("Enter Your name", "")
if(st.button('Submit')):
	result = name.title()
	st.success(result)
gender= st.radio("what is your Gender?",('Female','Male','Transgender'))
if(gender=='Female'):
    st.success("Female")
elif(gender=='Male'):
    st.success("Male")
else:
    st.success("Transgender")
age=st.number_input("Enter your Age:")
add=st.text_input("Enter your Address:")
hob1=st.checkbox("Dancing")
hob2=st.checkbox("Music")
hob3=st.checkbox("Watching Movies")
hob4=st.checkbox("Exercise")
hob5=st.checkbox("Gaming")
weight = st.number_input("Enter your weight (in kgs)")
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))
if(status == 'cms'):
    height = st.number_input('Centimeters')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
elif(status == 'meters'):
    height = st.number_input('Meters')
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
else:
    height = st.number_input('Feet')
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
if(st.button('Calculate BMI')):
    st.text("Your BMI Index is {}.".format(bmi))
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")