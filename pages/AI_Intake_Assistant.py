"""AI Intake Assistant
Combines intake form, housing guidance, application tips, and image generation into one unified assistant.
"""

import streamlit as st
import os
import traceback
from openai import OpenAI

# --- OpenAI Setup ---
api_key = os.getenv("OPENAI_API_KEY") or "your-api-key-here"
client = OpenAI(api_key=api_key)

# --- Streamlit Page Setup ---
st.title("🏠 Emergency Housing Assistant")
st.caption("Get AI-generated guidance, shelter visuals, and application tips.")
st.markdown("---")

# --- User Input ---
situation = st.text_area("💬 Describe your housing situation", "e.g., I lost my job and may be evicted soon. I have a daughter and no savings.")
zip_code = st.text_input("📍 Enter your ZIP Code", "95112")
urgency = st.slider("🚨 Urgency Level", 1, 5, 4)

# --- AI Response Functions: guidance, tips, and shelter image ---
def get_housing_guidance():
    prompt = f"""
    Emergency housing request:
    Situation: {situation}
    ZIP Code: {zip_code}
    Urgency: {urgency}/5

    Please provide:
    1. Immediate shelter options
    2. Documents needed
    3. Steps to take in 48 hours
    4. Community resources
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for emergency housing support."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}\n\n{traceback.format_exc()}"

def get_application_tips():
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Help users prepare emergency housing documents."},
                {"role": "user", "content": "List simple steps and documents needed for applying to emergency housing."}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}\n\n{traceback.format_exc()}"

def get_shelter_image():
    try:
        image = client.images.generate(
            model="dall-e-2",
            prompt="A clean and calm temporary shelter room with beds and warm lighting for a parent and child.",
            n=1,
            size="1024x1024"
        )
        return image.data[0].url
    except Exception as e:
        st.error("❌ Error generating image.")
        st.code(traceback.format_exc())
        return None

# --- Main Action ---
if st.button("🧠 Get Emergency Help"):
    if not situation.strip():
        st.warning("Please describe your housing situation.")
    else:
        with st.spinner("Getting AI help..."):
            st.subheader("📋 Housing Guidance")
            st.markdown(get_housing_guidance())

            st.subheader("📄 Application Tips")
            st.markdown(get_application_tips())

            st.subheader("🏠 Sample Shelter Preview")
            image_url = get_shelter_image()
            if image_url:
                st.image(image_url, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.caption("Created by Sapphire Team 💎 | Powered by OpenAI & Streamlit")