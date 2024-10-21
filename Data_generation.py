import pandas as pd
import numpy as np
import random
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


#@st.cache_data
def lastName():
    return pd.read_csv("/home/hudjo712/ProAI/last_names.csv")
#@st.cache_data
def firstName():
    return pd.read_csv("/home/hudjo712/ProAI/first_names.csv")
#@st.cache_data
def subject():
    return pd.read_csv("/home/hudjo712/ProAI/subjects.csv")

# Read the data
dfln = lastName()
dffn = firstName()
dfs = subject()

# Streamlit app setup
st.set_page_config(layout="wide")
st.sidebar.header("Interface")

# User inputs
studentNb = st.sidebar.number_input("Number of students", min_value=0, max_value=dfln.shape[0])
subjectNb = st.sidebar.number_input("Number of subjects", min_value=0, max_value=dfs.shape[0])
subjectGrade = st.sidebar.number_input("Grade of subjects", min_value=0, max_value=dfs.shape[0])
minimumGrade = st.sidebar.number_input("Minimum grade", min_value=0, max_value=55)
maximumGrade = st.sidebar.number_input("Maximum grade", min_value=0, max_value=60)

# Create random full names
def generate_random_names(studentNb):
    random_names = []
    for _ in range(studentNb):
        first_name = random.choice(dffn['First name'].tolist())
        last_name = random.choice(dfln['Last name'].tolist())
        full_name = f"{first_name} {last_name}"
        random_names.append(full_name)
    return random_names
studentList = generate_random_names(studentNb) if studentNb > 0 else []

# Select box for students
selectedStudent = st.sidebar.selectbox("Select a student", studentList)
dlButton = st.sidebar.button("Download data as CSV")

# Generate and display random names

def create_entries(studentList, subjectList, subjectGrade):
    data_entries = []
    for student_id, student_name in enumerate(studentList, start=1):
        for subject in subjectList:
            data_entries.append({
                'Student ID': student_id,
                'Student Name': student_name,
                'Subject': subject,
                'Grade': subjectGrade
            })
    return pd.DataFrame(data_entries)

studentList = generate_random_names(studentNb)
subjectList = dfs['Subject'].tolist()[:subjectNb]
student_data = create_entries(studentList, subjectList, subjectGrade)
st.dataframe(student_data)
# Placeholder for download functionality
if dlButton:
    st.write("Download functionality is not implemented yet.")
