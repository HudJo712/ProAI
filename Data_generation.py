import pandas as pd
import numpy as np
import random
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def read_files():
    if FileNotFoundError or pd.errors.EmptyDataError or pd.errors.ParserError:
        st.stop
    else:    
        return pd.read_csv("/home/hudjo712/ProAI/last_names.csv"),pd.read_csv("/home/hudjo712/ProAI/first_names.csv"),pd.read_csv("/home/hudjo712/ProAI/subjects.csv")
def regenerate_data(num_students,first_names_df,last_names_df,subjects_df,num_subjects,num_grades_per_stubject,min_grade,max_grade):
    """student_list=[['Student ID'],['Name'],['Subject'],['Grade']]
    for x in num_students:
        student_list['Student ID'].append(np.arange(1,num_students+1))
        student_list['First name'].append(random.choice(first_names_df['First name'].tolist())+" "+random.choice(last_names_df['Last name'].tolist()))
    """
    student_ids=np.arange(1,num_students+1)
    repeated_ids=np.repeat(student_ids, num_subjects*num_grades_per_stubject)
    first_names=first_names_df.values.flatten().tolist()
    last_names=last_names_df.values.flatten().tolist()
    student_names=[f"{random.choice(first_names)} {random.choice(last_names)}" for x in range(num_students)]
    subjects=subjects_df.values.flatten().tolost()
    grades=[np.random.randint for x in range(num_students)]
    sorted_student_names=sorted(student_names,key=lambda name: name.split()[-1])
    repeated_student_names=np.repeat(sorted_student_names,num_students*num_grades_per_stubject)
    repeated_subjects=np.title(np.repeat(subjects[:num_subjects],num_grades_per_stubject), num_students)
    grades=[[random.randint(min_grade,max_grade)for x in range(num_grades_per_stubject)] for x in range(num_students*num_subjects)]
    flattened_grades=np.array(grades).flatten()
    data={'Student ID':repeated_ids,'Name':repeated_student_names,'Subject':repeated_subjects,'Grade':flattened_grades}
    generated_df=pd.DataFrame(data)
    return generated_df
"""#@st.cache_data
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
"""