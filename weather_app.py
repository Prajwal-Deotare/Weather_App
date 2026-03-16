import streamlit as st
import requests

API_KEY = "000ceb8de5ef048f6a687e788ff2df75"

st.set_page_config(page_title="Weather Dashboard", page_icon="🌦", layout="centered")

st.title("Live Weather Dashboard")
st.write("Enter a city name to get real-time weather information")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                description = data["weather"][0]["description"]
                wind = data["wind"]["speed"]

                st.success(f"Weather in {city}")

                col1, col2 = st.columns(2)

                col1.metric("🌡 Temperature (°C)", temp)
                col2.metric("💧 Humidity (%)", humidity)

                st.metric("🌬 Wind Speed (m/s)", wind)
                st.write(f"☁ Condition: **{description.title()}**")

            else:
                st.error("City not found!")

        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a city name")