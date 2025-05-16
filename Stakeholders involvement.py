import streamlit as st

st.set_page_config(page_title="Stakeholder Involvement", layout="wide")
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
