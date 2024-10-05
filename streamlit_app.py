import streamlit as st
import pandas as pd

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

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')
  st.scatter_chart(data=df, x='bill_depth_mm', y='sex', color='species')
  
with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgerson'))
  bill_length_mm = st.slider('Bill depth (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2) 
  flipper_length_mm = st.slider('flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('male', 'female'))


  # Create a DataFrame for the input features
  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, x_row], axis=0)


encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)

x = df_penguins[1:]
input_row = df_penguins[:1]


target_napper = {'Adelie': 0,
                 'Chinstrap': 1,
                 'Gentoo': 2}
def target_encode(val):
  return taget_napper[val]

y = y_row.apply(target_encode)

with st.expander('Data Preparation'):
  st.write('**Encoded X (input penguin)**')
  input_row
  st.write('**Encoded y**')
  y
