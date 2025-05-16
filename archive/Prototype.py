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
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an empathetic AI that helps users navigate emergency housing."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

# Feature 2: Housing Space Visualization (Image Generation)
def generate_shelter_image():
    response = openai.Image.create(
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
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a calm, friendly assistant helping users prepare their documents."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

# Streamlit UI
st.title("Emergency Housing Assistance App")
st.text("This AI-powered app helps you navigate urgent housing needs, visualize shelter options, and prepare your application.")

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

st.caption("Created by the Sapphire Team 💎 • Powered by OpenAI & Streamlit")

#------------------------------------------------------------------------------------------------------------------------------------------------------

# chatbot on the side
st.sidebar.title("💬 HelpBot")
st.sidebar.write("Need help with Emergency Interim Housing (EIH)? Ask anything.")

# Initialize chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# user input area
user_input = st.sidebar.text_input("You:", key="user_input", placeholder="e.g., Can I apply for shelter if I have a pet?")

# If user submits a message
if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append(("You", user_input))

    # Generate AI response using OpenAI
    with st.spinner("Thinking..."):
        try:
            messages = [{"role": "system", "content": "You are a helpful assistant that specializes in Emergency Interim Housing (EIH) in San Jose and Santa Clara County. Be concise, helpful, and clear."}]
            
            # Add all previous messages to maintain context
            for sender, message in st.session_state.chat_history:
                role = "user" if sender == "You" else "assistant"
                messages.append({"role": role, "content": message})

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                temperature=0.6,
                max_tokens=500
            )

            bot_reply = response.choices[0].message.content.strip()
            st.session_state.chat_history.append(("Bot", bot_reply))

        except Exception as e:
            bot_reply = "⚠️ Sorry, I ran into an error. Please try again."
            st.session_state.chat_history.append(("Bot", bot_reply))
            st.error(f"Error: {e}")