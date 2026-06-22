import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Student Performance Prediction")

st.title("🎓 Student Performance Prediction System")

model = pickle.load(open("model.pkl","rb"))

st.header("Student Information")

school = st.selectbox("School",[0,1])
sex = st.selectbox("Sex",[0,1])

age = st.number_input("Age",15,22,17)

address = st.selectbox("Address",[0,1])
famsize = st.selectbox("Family Size",[0,1])
Pstatus = st.selectbox("Parent Status",[0,1])

Medu = st.slider("Mother Education",0,4,2)
Fedu = st.slider("Father Education",0,4,2)

Mjob = st.selectbox("Mother Job",[0,1,2,3,4])
Fjob = st.selectbox("Father Job",[0,1,2,3,4])

reason = st.selectbox("Reason",[0,1,2,3])
guardian = st.selectbox("Guardian",[0,1,2])

traveltime = st.slider("Travel Time",1,4,2)
studytime = st.slider("Study Time",1,4,2)

failures = st.slider("Past Failures",0,4,0)

schoolsup = st.selectbox("School Support",[0,1])
famsup = st.selectbox("Family Support",[0,1])
paid = st.selectbox("Extra Paid Classes",[0,1])

activities = st.selectbox("Activities",[0,1])
nursery = st.selectbox("Nursery",[0,1])
higher = st.selectbox("Higher Education",[0,1])
internet = st.selectbox("Internet Access",[0,1])
romantic = st.selectbox("Romantic Relationship",[0,1])

famrel = st.slider("Family Relationship",1,5,3)
freetime = st.slider("Free Time",1,5,3)
goout = st.slider("Go Out",1,5,3)

Dalc = st.slider("Workday Alcohol",1,5,1)
Walc = st.slider("Weekend Alcohol",1,5,2)

health = st.slider("Health",1,5,3)

absences = st.number_input("Absences",0,100,0)

G1 = st.slider("G1",0,20,10)
G2 = st.slider("G2",0,20,10)

if st.button("Predict Final Grade"):

    input_data = pd.DataFrame({
        'school':[school],
        'sex':[sex],
        'age':[age],
        'address':[address],
        'famsize':[famsize],
        'Pstatus':[Pstatus],
        'Medu':[Medu],
        'Fedu':[Fedu],
        'Mjob':[Mjob],
        'Fjob':[Fjob],
        'reason':[reason],
        'guardian':[guardian],
        'traveltime':[traveltime],
        'studytime':[studytime],
        'failures':[failures],
        'schoolsup':[schoolsup],
        'famsup':[famsup],
        'paid':[paid],
        'activities':[activities],
        'nursery':[nursery],
        'higher':[higher],
        'internet':[internet],
        'romantic':[romantic],
        'famrel':[famrel],
        'freetime':[freetime],
        'goout':[goout],
        'Dalc':[Dalc],
        'Walc':[Walc],
        'health':[health],
        'absences':[absences],
        'G1':[G1],
        'G2':[G2]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Final Grade (G3): {prediction[0]:.2f}")