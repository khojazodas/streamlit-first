import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

st.title('Student Performance Data')

with st.expander('Initial data'):
  df = pd.read_csv('student_performance.csv')
  df

  st.write('**X**')
  x_row = df.drop(['GradeClass', 'StudentID', 'Ethnicity'], axis=1)
  x_row

  st.write('**y**')
  y_row = df['GradeClass']
  y_row


with st.sidebar:
  st.header('Input Features')
  gender = st.selectbox('Gender(0 - Male, 1 - Female)', ('0', '1'))
  tutoring = st.selectbox('Tutoring(0 - No, 1 - Yes)', ('0', '1'))
  extracurriculars = st.selectbox('Extracurriculars(0 - No, 1 - Yes)', ('0', '1'))
  sport = st.selectbox('Sports(0 - No, 1 - Yes)', ('0', '1'))
  music = st.selectbox('Music(0 - No, 1 - Yes)', ('0', '1'))
  volunteering = st.selectbox('Volunteering(0 - No, 1 - Yes)', ('0', '1'))
  age = st.slider('Age', 15, 19, 17)
  parental_edu = st.slider("Parental Education(0-none, 1-high school, 2-some college, 3-bachelor's, 4-higher)", 0, 4, 2)
  stw = st.slider('Study Time Weekly', 0, 20, 10)
  absences = st.slider('Absences', 0, 30, 15)
  parents = st.slider('Parental Support(0-none, 1-low, 2-moderate, 3-high, 4-very high)', 0, 4, 2)
  gpa = st.slider('GPA', 2.0, 4.0, 3.0)

  # Create a DataFrame for the input features
  data = {'gender': gender,
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
  return target_napper[val]

y = y_row.apply(target_encode)

with st.expander('Data Preparation'):
  st.write('**Encoded X (input penguin)**')
  input_row
  st.write('**Encoded y**')
  y

# Model training and inference
## Train the ML model
clf = RandomForestClassifier()
clf.fit(x_row, y)

## Apply model to make predictions
prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)

df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gentoo']
df_prediction_proba.rename(columns={0: 'Adelie',
                                 1: 'Chinstrap',
                                 2: 'Gentoo'})

# Display predicted species
st.subheader('Predicted Species')
st.dataframe(df_prediction_proba,
             column_config={
               'Adelie': st.column_config.ProgressColumn(
                 'Adelie',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),
               'Chinstrap': st.column_config.ProgressColumn(
                 'Chinstrap',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),
               'Gentoo': st.column_config.ProgressColumn(
                 'Gentoo',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),
             }, hide_index=True)


penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.success(str(penguins_species[prediction][0]))
