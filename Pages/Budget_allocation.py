import streamlit as st
import pandas as pd

def main():
    # Page setup
    st.set_page_config(page_title="EIH Budget", layout="wide")
    st.title("💰 EIH Budget Overview")
    st.write("✅ App loaded successfully!")

    # Budget data
    data = {
        'Category': [
            'Facility Leasing', 'Staff Wages', 'Food & Supplies',
            'Mental Health', 'Security', 'Transportation', 'Admin'
        ],
        'Cost': [1200000, 850000, 500000, 400000, 200000, 150000, 100000]
    }
    df = pd.DataFrame(data)

    # Show table and bar chart
    st.header("📊 Budget Breakdown")
    st.dataframe(df)
    st.bar_chart(df.set_index("Category"))

    # Total cost
    total = df["Cost"].sum()
    st.metric("Total Budget", f"${total:,}")

    # Funding
    st.header("💬 Funding Sources")
    funding_total = 1000000 + 800000 + 600000 + 300000
    st.write("- HUD: $1,000,000")
    st.write("- State: $800,000")
    st.write("- City: $600,000")
    st.write("- Private: $300,000")

    # Budget gap
    st.header("🧮 Budget Gap")
    gap = total - funding_total

    if gap <= 0:
        st.success("Fully funded! 🎉")
    else:
        st.error(f"Shortfall: ${gap:,}")
        st.write("Suggestions:")
        st.write("- Apply for FEMA")
        st.write("- Start donor campaign")

if __name__ == "__main__":
    main()
