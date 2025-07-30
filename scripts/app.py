import streamlit as st

st.set_page_config(page_title="RosoiGhor 🍲", layout="wide")

st.title("🍲 Welcome to RosoiGhor")
st.subheader("Discover Local Famous Food and Stores")

st.write("Hello FoodFindr! This is the first version of my app 🚀")

# Take user location
location = st.text_input("Enter your location:")

if location:
    st.success(f"Showing popular food and stores near **{location}**!")

    popular_foods = {
        "Kolkata": ["Mughlai Paratha", "Kathi Roll", "Rosogolla"],
        "Madhyamgram": ["Phuchka", "Chowmein", "Momos"],
        "Delhi": ["Chole Bhature", "Paratha", "Jalebi"],
    }

    foods = popular_foods.get(location.capitalize(), ["No data available yet 😔"])
    
    st.write("### 🍴 Popular Foods")
    for food in foods:
        st.write(f"- {food}")

    # Add working images for Madhyamgram
    if location.lower() == "madhyamgram":
        st.image("https://i.imgur.com/UB0Xf3p.jpg", caption="Phuchka", width=300)
        st.image("https://i.imgur.com/f0X8qba.jpg", caption="Chowmein", width=300)
        st.image("https://i.imgur.com/q4npRPr.jpg", caption="Momos", width=300)



