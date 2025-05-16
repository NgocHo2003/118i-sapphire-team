# emergency_housing_app.py

import streamlit as st
import openai

# OpenAI API Key
openai.api_key = "your-api-key-here"

# Feature 1: Emergency Housing Guidance (Text Completion)
def generate_housing_guidance(situation, zip_code, urgency):
    prompt = f"""
    You are an emergency housing assistant. A user is facing the following housing crisis:
    Situation: {situation}
    ZIP Code: {zip_code}
    Urgency Level: {urgency}/5
    Based on this information, provide:
    1. Immediate housing options or shelters nearby
    2. Necessary documentation to apply
    3. Action steps they should take in the next 48 hours
    4. Community resources or support services they can contact
    """
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an empathetic AI that helps users navigate emergency housing."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

# Feature 2: Housing Space Visualization (Image Generation)
def generate_shelter_image():
    response = openai.images.generate(
        model="dall-e-2",
        prompt="A safe, clean, temporary shelter for a single parent and child. Warm lighting, basic amenities, calming colors.",
        n=1,
        size="1024x1024"
    )
    return response.data[0].url

# Feature 3: Application Preparation Assistance (Text Completion)
def generate_application_help():
    prompt = """
    Explain in simple steps how someone can prepare their documentation to apply for emergency housing.
    Include:
    1. Identification documents
    2. Proof of income or unemployment
    3. Childcare verification (if applicable)
    4. How to organize and submit these files
    Make this beginner-friendly and anxiety-free.
    """
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a calm, friendly assistant helping users prepare their documents."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

# Streamlit UI
st.title("Emergency Housing Assistance App")
st.write("This AI-powered app helps you navigate urgent housing needs, visualize shelter options, and prepare your application.")

# User inputs
situation = st.text_area("Describe Your Current Housing Situation", 
                         "I just lost my job and may be evicted soon. I have a daughter and no savings.")
zip_code = st.text_input("Your ZIP Code", "95112")
urgency = st.slider("Urgency Level", 1, 5, 4)

if st.button("Get Housing Assistance"):
    with st.spinner("Finding emergency options..."):
        guidance = generate_housing_guidance(situation, zip_code, urgency)
        st.subheader("🛏️ Emergency Housing Guidance")
        st.write(guidance)

    with st.spinner("Visualizing potential shelter..."):
        image_url = generate_shelter_image()
        st.subheader("🏠 Visual Representation of a Shelter")
        st.image(image_url, caption="Example of Temporary Shelter", use_container_width=True)

    with st.spinner("Preparing your application..."):
        prep_help = generate_application_help()
        st.subheader("📄 Application Preparation Help")
        st.write(prep_help)

st.caption("Created by the Sapphire Team • Powered by OpenAI & Streamlit")