import streamlit as st
import numpy as np 
import pandas as pd 

st.title("Uber Pickups in New York City on Monday")

#Fetch some data
DATE_COLUMN = "date/time"
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data



#test function

data_load_state = st.text("Loading data ....")

data = load_data(10000)

data_load_state = st.text("Loading data...done!")



#inspect raw data

st.subheader("Raw data")

st.write(data)



#draw histogram

st.subheader("Number of Pickups by Hour")

hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

#use st.bar_chart()

st.bar_chart(hist_values)



#plotting data on Map

st.subheader("Map of all pickups")
st.map(data)



#histogram for busiest hour for pickups

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#subheader
st.subheader(f"Map of all pickups at {hour_to_filter}:00")
st.map(filtered_data)



#filter with a slider

hour_to_filter = st.slider("hour", 0, 23)



#using buttons to filter data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)



# Add a slider to the sidebar:

#st.sidebar.slider()

hour_to_filter = st.sidebar.slider("hour", 0, 23)



#Add a selectbox to the sidebar

add_selectbox = st.sidebar.selectbox(
    'How would you like explore the Uber dataset for Pickups?',
    ('Tabular Data', 'Histogram', 'Plot a Map')
)