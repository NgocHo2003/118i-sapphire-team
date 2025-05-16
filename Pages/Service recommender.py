import streamlit as st
import openai
import os

st.set_page_config(page_title="AI Resource Recommender", layout="wide")
st.title("🎯 AI Resource Recommender")
st.caption("Select your needs and let AI recommend relevant services in your city.")

openai.api_key = os.getenv("OPENAI_API_KEY")

st.markdown("---")
st.header("📦 Choose Your Needs")

needs = st.multiselect(
    "Select the services you need help with:",
    ["Meals", "Mental Health Support", "Job Assistance", "Medical Access", "Family Shelter", "Pet-Friendly Housing"]
)

user_city = st.text_input("What city are you in?", placeholder="e.g., San Jose")

if st.button("🔍 Get AI-Powered Resource Suggestions"):
    if not needs:
        st.warning("Please select at least one need.")
    elif not user_city:
        st.warning("Please enter your city.")
    else:
        prompt = f"I'm in {user_city}. I need services for: {', '.join(needs)}. Recommend resources and a short explanation for each."
        with st.spinner("Finding personalized resources..."):
            chat = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You're an AI that recommends real local services for housing and social support."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.success("📋 AI Suggestions:")
            st.markdown(chat.choices[0].message.content)
