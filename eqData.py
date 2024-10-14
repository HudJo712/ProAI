import pandas as pd
import streamlit as st
import os


title1="Global Earthquake Data"
st.title(title1)
st.write("Comprehensive dataset of global earthquakes with key attributes for analysis: https://www.kaggle.com/datasets/shreyasur965/recent-earthquakes")
eq_data=pd.read_csv("https://github.com/HudJo712/ProAI/blob/main/earthquakes.csv")
eq_frame=pd.DataFrame(eq_data)
st.dataframe(eq_frame)

title2="Magnitude"
st.title(title2)
st.write(f'Min:{eq_data['magnitude'].min()}')
st.write(f'Mean:{eq_data['magnitude'].mean()}')
st.write(f'Max:{eq_data['magnitude'].max()}')

title3="Network"
st.title(title3)
network_list=eq_data['net'].unique()
eq_numbers=eq_data['net'].value_counts().reset_index()
selected_Network=st.selectbox('Network',network_list)
df_network=eq_data[eq_data['net']==selected_Network]
st.write(f'The number of earthquakes for {selected_Network}:{df_network['net'].count()}')

title4="Number of earthquakes by network"
st.title(title4)
eq_numbers=eq_data['net'].value_counts().reset_index()
eq_numbers.columns=['net','Count']
st.bar_chart(eq_numbers.set_index('net'))

st.write(os.getcwd())
