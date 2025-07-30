import streamlit as st

st.set_page_config(page_title="RosoiGhor 🍲", layout="wide")

st.title("🍲 Welcome to RosoiGhor")
st.subheader("Discover Local Famous Food and Stores")

st.write("Hello FoodFindr! This is the first version of my app 🚀")

# Take user location
location = st.text_input("Enter your location:")

if location:
    st.success(f"Showing popular food and stores near **{location}**!")

    # Example data (later we will fetch from YouTube/Google)
    popular_foods = {
        "Kolkata": ["Mughlai Paratha", "Kathi Roll", "Rosogolla"],
        "Madhyamgram": ["Phuchka", "Chowmein", "Momos"],
        "Delhi": ["Chole Bhature", "Paratha", "Jalebi"],
    }

    foods = popular_foods.get(location.capitalize(), ["No data available yet 😔"])
    
    st.write("### 🍴 Popular Foods")
    for food in foods:
        st.write(f"- {food}")

# Add sample images for Madhyamgram
if location.lower() == "madhyamgram":
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f2/Pani_Puri_Golgappa.jpg", caption="Phuchka", width=300)
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Indian_Chowmein.jpg", caption="Chowmein", width=300)
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Momo_nepal.jpg", caption="Momos", width=300)


