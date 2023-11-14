import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import seaborn as sns
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import date, timedelta

# Function to display the main page
#def main_page():
########################################################## Text and Display Data #####################################

st.title('Streamlit Tutorial')  # Display a title
st.write("Here's our first attempt at using data to create a table:")  # Display text
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)  # Display a dataframe as a table


########################################################## Widgets #####################################


############### 1. Slider
age = st.slider('Select your age', 0, 100, 25)  # Min, Max, Default values
st.write('Your age is:', age)

############### 2. Text Input
name = st.text_input('Enter your name', 'Type here...')
st.write('Hello,', name)

############### 3. Checkbox
if st.checkbox('Show/Hide'):
    st.write('The Cat has been Revealed!')
    st.image("https://static.streamlit.io/examples/cat.jpg")  # Display an image in the second column

else:
    st.write('The hidden message is now hidden.')

############### 4. Selectbox


favorite = st.selectbox(
    'Choose a Character?',
    ( "Rick Sanchez",
    "Morty Smith",
    "Summer Smith",
    "Beth Smith",
    "Jerry Smith",
    )
)
l = [ "Rick Sanchez",
    "Morty Smith",
    "Summer Smith",
    "Beth Smith",
    "Jerry Smith",
    ]
temp = l.index(favorite) + 1
st.write('Choosed:', favorite)
st.sidebar.image(f"https://rickandmortyapi.com/api/character/avatar/{temp}.jpeg")

############### 5. Date Input
appointment_date = st.date_input(
    "Select an appointment date",
    min_value=date.today() + timedelta(days=10),  # Minimum value as today's date
    value=date.today()  + timedelta(days=10) # Default value as today's date
)


st.write('Your appointment date is:', appointment_date)

############### 6. Radio Input
st.radio('Choose:',[1,2])


############### 7. Markdown Text

text = '''

**Baldur's Gate 3** is an upcoming role-playing video game that has been the center of attention among RPG enthusiasts. Developed and published by *Larian Studios*, it is the third main game in the Baldur's Gate series and is based on the *Dungeons & Dragons* tabletop role-playing system.

The game is set in the Forgotten Realms and features a mix of new and returning characters. It promises to deliver an enriching story combined with deep strategic gameplay, allowing players to experience the thrill and challenge of navigating a world filled with magic, monsters, and intrigue.

One of the most anticipated features of **Baldur's Gate 3** is its multiplayer functionality, where players can join forces in cooperative gameplay or challenge each other in strategic combats. The game is currently in early access, with fans eagerly awaiting the full release.

> "Baldur's Gate 3 is more than just a technological advancement, it is a journey into the heart of what makes Dungeons & Dragons so captivating."

For more information, visit the [official Baldur's Gate 3 website](https://baldursgate3.game/).


'''

st.markdown(text)


st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # Play an audio file



############################# Visualizations ################################


iris = sns.load_dataset('iris')
#col1, col2, col3 = st.columns(3)

#with col1:
st.header("Matplotlib Visualization")
fig, ax = plt.subplots()
species = iris['species'].astype('category').cat.codes
scatter = ax.scatter(iris['petal_length'], iris['petal_width'], c=species)
legend = ax.legend(*scatter.legend_elements(), title="Species")
ax.add_artist(legend)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Petal Length vs Width (Matplotlib)')
st.pyplot(fig)

#with col2:
# Using Streamlit's inbuilt function
st.header("Streamlit Inbuilt Function Visualization")
st.scatter_chart(data=iris, x="petal_length", y="petal_width", color="species")

#with col3:
# Using Plotly for visualization
st.header("Plotly Visualization")
fig = px.scatter(iris, x='petal_length', y='petal_width', color='species')
st.plotly_chart(fig)




'''
def second_page():
    st.title('Second Page')
    st.write("This is another page of the app.")



# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'Main Page'

# Sidebar navigation
page = st.sidebar.selectbox('Choose a page:', ['Main Page', 'Second Page'])

# Update the page in session state
st.session_state['page'] = page

# Display the selected page
if st.session_state['page'] == 'Main Page':
    main_page()
elif st.session_state['page'] == 'Second Page':
    second_page()

'''