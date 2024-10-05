import streamlit as st

st.title('Student Performance Data')

with st.expander('Initial data'):
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  x_row = df.drop('species', axis=1)
  x_row

  st.write('**y**')
  y_row = df.species
  y_row
