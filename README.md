# SmartHaven – Emergency Interim Housing Support Platform  
BUS4-118i, Spring '25 – San José State University

**Deployed App**:  
- [smarthaven.streamlit.app](https://smarthaven.streamlit.app) – Primary deployment hosted and maintained by me  
- [118i-sapphire-team.streamlit.app](https://118i-sapphire-team.streamlit.app) – Final iteration hosted by José

## 🎥 Demo & Presentation

- 📽️ [SmartHaven Demo Video](https://docs.google.com/file/d/1t693dj6CqUlb_MUc_4iyYmRMWd4ZfAUk/preview)  
- 🖥️ [SmartHaven Capstone Slide Deck](https://docs.google.com/presentation/d/1-5HBpcy_RAxaVdDiQ-VgAe2oxf7gBXv56v30LPr4k08/edit?usp=sharing)
---

**Role**: DevOps Engineer  
**Team**: 118i-Sapphire-Team  
**Course**: AI for Social Good

---

## 🔍 Project Overview

SmartHaven is a generative AI-powered platform designed to assist individuals and case managers in navigating emergency interim housing resources in Santa Clara County. The app integrates sentiment analysis, mapping, and an AI assistant to streamline access to local support services, aiming to reduce friction and promote digital equity for vulnerable communities.

---

## 👨‍💻 My Contributions

- Proposed early project ideas, including site mapping and sentiment analysis using the Nextdoor API (pivoted to Reddit after access was denied)
- Led prompt engineering and OpenAI API integration for the chatbot
- Audited and standardized teammate code contributions to ensure Streamlit app functionality across multiple pages
- Deployed and maintained the primary version on Streamlit Cloud
- Resolved cross-team environment inconsistencies (Python and API versions)
- Finalized structure and codebase, contributing 23 commits related to deployment, bug fixes, and formatting

---

## ⚙️ Technologies & Tools

- **Languages**: Python, HTML/CSS (Streamlit native elements)
- **Libraries**: Streamlit, OpenAI API, Reddit API, requests, folium
- **Tools**: Git, GitHub, Streamlit Cloud, VS Code
- **Methodologies**: Agile, Prompt Engineering, DevOps, Code Auditing

---

## 🔐 API Key Management

All API keys were stored securely via local environment variables.  
To comply with security best practices:
- My OpenAI API keys were revoked  
- Auto-recharge billing was disabled  

*Confirmation screenshots provided in a separate submission document.*

---

## 📂 Repo Structure

- `/pages/` – Modular Streamlit app components
- `/archive/` – Early prototype build
- `/documentation/` – Project planning and goals
- `main_page.py` – Unified entry point
- `requirements.txt` – Project dependencies
- `setup.sh` – Local setup script

---

## 🚀 How to Run Locally

1. Clone this repository  
2. Install dependencies:  
   `pip install -r requirements.txt`  
3. Run the app:  
   `streamlit run main_page.py`
