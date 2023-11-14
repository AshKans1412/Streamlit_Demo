import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

# Load dataset
iris = sns.load_dataset('iris')

# Streamlit title
st.header('Iris Dashboard')

# Show dataset
if st.checkbox('Show Data'):
    st.write(iris)

# Histogram
st.sidebar.header('Histogram Settings')
selected_column = st.sidebar.selectbox('Select column', iris.columns)
bin_size = st.sidebar.slider('Number of bins', min_value=10, max_value=100, value=20)

fig, ax = plt.subplots()
sns.histplot(iris[selected_column], bins=bin_size, ax=ax)
st.pyplot(fig)

# Pairplot
if st.checkbox('Show Pairplot'):
    st.write(sns.pairplot(iris, hue='species'))
    st.pyplot()

# Boxplot
st.sidebar.header('Boxplot Settings')
selected_column_box = st.sidebar.selectbox('Select column for boxplot', iris.columns[:-1])
selected_species = st.sidebar.multiselect('Select species', iris['species'].unique(), default=iris['species'].unique())

if len(selected_species) > 0:
    filtered_data = iris[iris['species'].isin(selected_species)]
    fig2, ax2 = plt.subplots()
    sns.boxplot(x='species', y=selected_column_box, data=filtered_data, ax=ax2)
    st.pyplot(fig2)

# Scatter Plot
st.sidebar.header('Scatter Plot Settings')
x_axis_val = st.sidebar.selectbox('X axis', options=iris.columns)
y_axis_val = st.sidebar.selectbox('Y axis', options=iris.columns, index=1)

fig3, ax3 = plt.subplots()
sns.scatterplot(x=x_axis_val, y=y_axis_val, hue='species', data=iris, ax=ax3)
st.pyplot(fig3)
