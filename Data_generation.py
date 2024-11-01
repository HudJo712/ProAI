import pandas as pd
import numpy as np
import random
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 1: Read CSV files with error handling
@st.cache_data
def read_files():
    try:
        last_names_df = pd.read_csv("last_names.csv")
        first_names_df = pd.read_csv("first_names.csv")
        subjects_df = pd.read_csv("subjects.csv")
        return last_names_df, first_names_df, subjects_df
    except FileNotFoundError:
        st.error("File not found.")
        st.stop()
    except pd.errors.EmptyDataError:
        st.error("No data in file.")
        st.stop()
    except pd.errors.ParserError:
        st.error("Parse error.")
        st.stop()
    except Exception as e:
        st.error(f"Some other exception: {e}")
        st.stop()

# Step 2: Generate student data
def regenerate_data(num_students, first_names_df, last_names_df, subjects_df, num_subjects, num_grades_per_subject, min_grade, max_grade):
    student_ids = np.arange(1, num_students + 1)
    first_names = first_names_df.values.flatten().tolist()
    last_names = last_names_df.values.flatten().tolist()
    student_names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(num_students)]
    sorted_student_names = sorted(student_names, key=lambda name: name.split()[-1])
    
    repeated_ids = np.repeat(student_ids, num_subjects * num_grades_per_subject)
    repeated_names = np.repeat(sorted_student_names, num_subjects * num_grades_per_subject)
    
    subjects = subjects_df.values.flatten().tolist()
    repeated_subjects = np.tile(np.repeat(subjects[:num_subjects], num_grades_per_subject), num_students)
    
    grades = np.random.randint(min_grade, max_grade + 1, size=num_students * num_subjects * num_grades_per_subject)
    
    data = {
        'Student ID': repeated_ids,
        'Name': repeated_names,
        'Subject': repeated_subjects,
        'Grade': grades
    }
    return pd.DataFrame(data)

# Step 3: Plot grade distribution using Plotly
def plot_grade_distribution(df):
    fig = px.histogram(
        df, x="Grade", color="Subject", nbins=20, barmode="overlay",
        title="Grade Distribution by Subject"
    )
    fig.update_layout(xaxis_title="Grade", yaxis_title="Count")
    return fig

# Step 4: Plot KDE using Seaborn
def plot_kde(df, min_grade, max_grade):
    fig, ax = plt.subplots()
    sns.kdeplot(data=df, x="Grade", ax=ax, fill=True, color='skyblue', alpha=0.5)  # fill=True for density area
    ax.set_xlim(min_grade, max_grade)
    ax.set_ylabel("Density")
    ax.set_xlabel("Grade")
    ax.set_title("Grade Density")
    return fig

# Step 5: Main function for Streamlit layout and logic
def main():
    st.set_page_config(layout="wide", page_title="Grade analyser")
    st.title("Grade analyser")
    
    col1, col2 = st.columns(2)
    
    # Read data files
    last_names_df, first_names_df, subjects_df = read_files()
    
    # Initialize session state for data and parameters
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame()
    if 'params' not in st.session_state:
        st.session_state.params = {}
    
    # Sidebar inputs
    num_students = st.sidebar.number_input("Number of Students", min_value=1, max_value=100000, value=100)
    num_subjects = st.sidebar.number_input("Number of Subjects", min_value=1, max_value=100, value=10)
    num_grades_per_subject = st.sidebar.number_input("Grades per Subject", min_value=2, max_value=100, value=3)
    min_grade = st.sidebar.number_input("Minimum Grade", min_value=0, max_value=95, value=0)
    max_grade = st.sidebar.number_input("Maximum Grade", min_value=min_grade + 5, max_value=100, value=60)
    
    # Determine if data needs regeneration
    current_params = {
        'num_students': num_students,
        'num_subjects': num_subjects,
        'num_grades_per_subject': num_grades_per_subject,
        'min_grade': min_grade,
        'max_grade': max_grade
    }
    if st.session_state.df.empty or st.session_state.params != current_params:
        st.session_state.df = regenerate_data(
            num_students, first_names_df, last_names_df, subjects_df,
            num_subjects, num_grades_per_subject, min_grade, max_grade
        )
        st.session_state.params = current_params
    
    # Display data and statistics
    col1.write(st.session_state.df)
    col2.write(st.session_state.df.describe())
    
    # Plot KDE and grade distribution
    kde_fig = plot_kde(st.session_state.df, min_grade, max_grade)
    col1.pyplot(kde_fig)
    
    grade_dist_fig = plot_grade_distribution(st.session_state.df)
    col2.plotly_chart(grade_dist_fig)
    
    # Select student and show student-specific grade distribution
    student_names = pd.unique(st.session_state.df["Name"])
    selected_student_name = st.sidebar.selectbox("Select Student", student_names)
    student_df = st.session_state.df[st.session_state.df["Name"] == selected_student_name]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(
        student_df, x="Grade", hue="Name", bins=np.arange(min_grade, max_grade + 1, 5),
        palette="Set1", multiple="stack", ax=ax
    )
    ax.set_xlabel("Grade")
    ax.set_title(f"Grade Distribution for {selected_student_name}")
    col2.pyplot(fig)
    
    # CSV download
    csv = st.session_state.df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
        label="Download Data as CSV",
        data=csv,
        file_name="grades_data.csv",
        mime="text/csv"
    )

# Run main if script is executed
if __name__ == "__main__":
    main()
