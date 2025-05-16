"""Stakeholder Involvement
Explains how various stakeholders collaborate in Emergency Interim Housing (EIH) programs,
and provides an EIH-focused chatbot assistant in the sidebar.
"""

import streamlit as st
import pandas as pd 
import numpy as np
import openai
import os
from openai import OpenAI

# for it to pop up on the sidebar
st.sidebar.markdown("# Stakeholder Involvement 🤝")

st.title("🤝 Stakeholder Roles in Emergency Interim Housing")
st.caption("Understand how different sectors collaborate to support temporary housing solutions.")

st.markdown("---")

st.header("🏛️ Who Are the Key Stakeholders?")

cols = st.columns(2)

with cols[0]:
    st.subheader("1. Local Government")
    st.markdown("""
    - **Funds infrastructure and grants**  
    - Coordinates with housing agencies  
    - Enforces building codes and safety standards  
    - Approves zoning and temporary shelter policies  
    """)

with cols[1]:
    st.subheader("2. Nonprofits & NGOs")
    st.markdown("""
    - Manage shelters and service delivery  
    - Offer wraparound services (mental health, job support)  
    - Provide culturally tailored solutions  
    """)

cols = st.columns(2)

with cols[0]:
    st.subheader("3. Health & Human Services")
    st.markdown("""
    - Mobile clinics for physical and mental health  
    - Partner on substance use treatment programs  
    - Medicaid coordination  
    """)

with cols[1]:
    st.subheader("4. Community Organizations")
    st.markdown("""
    - Local churches, mutual aid groups, volunteers  
    - Provide meals, clothing, hygiene kits  
    - Trusted by community for outreach  
    """)

st.markdown("---")
st.header("🛠️ How Do They Collaborate?")
st.markdown("""
1. **Weekly Coordination Meetings** between city staff, shelter operators, and service providers  
2. **Shared Database** to avoid duplication and ensure continuity  
3. **Joint Funding Applications** to state/federal grants  
4. **Feedback Loops** through client surveys and staff debriefs
""")

st.markdown("---")
st.header("📈 Example Collaborative Impact")
st.success("""
In 2024, San Francisco’s EIH Taskforce (15 agencies) housed 1,200+ people in 90 days.  
They shared intake data, rotated mental health teams, and deployed mobile showers citywide.
""")

st.image("https://images.unsplash.com/photo-1573164574572-cb89e39749b4", caption="Community-first response model", use_column_width=True)


# footer
st.markdown("---")
st.caption("Provided by the Sapphire Team 💎 • Powered by OpenAI & Streamlit")

#------------------------------------------------------------------------------------------------------------------------------------------------------

# chatbot on the side
st.sidebar.title("💬 HelpBot")
st.sidebar.write("Need help with Emergency Interim Housing (EIH)? Ask anything.")

# Initialize chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for sender, message in st.session_state.chat_history:
    st.sidebar.markdown(f"**{sender}:** {message}")

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

            response = openai.chat.completions.create(
                model="gpt-4",
                messages=messages,
                temperature=0.6,
                max_tokens=500
            )

            ai_reply = response.choices[0].message.content.strip()
            st.session_state.chat_history.append(("Bot", ai_reply))

        except Exception as e:
            ai_reply = "⚠️ Sorry, I ran into an error. Please try again."
            st.session_state.chat_history.append(("Bot", ai_reply))
            st.error(f"Error: {e}")