import streamlit as st

# Set up the page
st.set_page_config(page_title="RosoiGhor 🍲", layout="wide")

# Title and subtitle
st.title("🍲 Welcome to RosoiGhor")
st.subheader("Discover Local Famous Food and Stores")

st.write("Hello FoodFindr! This is the first version of my app 🚀")

# Example input
location = st.text_input("Enter your location:")
if location:
    st.success(f"Showing popular food and stores near **{location}**!")
