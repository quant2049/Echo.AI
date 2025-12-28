import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(
    page_title="The Echo Journal",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Inject Custom CSS for the "Cyber-Zen" look
st.markdown(f"""
    <style>
    /* Main Background */
    .stApp {{
        background-color: #0E1117;
        color: #FFFFFF;
    }}

    /* Title Styling */
    h1 {{
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
    }}

    /* Custom Card Styling for the sidebar stats */
    .stat-card {{
        background-color: #1A1C1E;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #2D2D2D;
        margin-bottom: 20px;
    }}

    /* The Glowing Record Button */
    div.stButton > button {{
        background-color: #00F2EA !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        height: 3.5rem !important;
        width: 100% !important;
        box-shadow: 0px 0px 20px 2px rgba(0, 242, 234, 0.4);
        transition: 0.3s;
    }}
    
    div.stButton > button:hover {{
        box-shadow: 0px 0px 30px 5px rgba(0, 242, 234, 0.6);
        transform: translateY(-2px);
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. Create the Layout (Main Area vs Sidebar)
col1, padding, col2 = st.columns([2.5, 0.2, 1])

with col1:
    st.title("The Echo Journal")
    st.write("### 7-Day Mood Sparkline")
    
    # Generate synthetic data for the chart (Replace this with DB data later)
    chart_data = pd.DataFrame(
        np.random.randn(20, 1).cumsum(axis=0),
        columns=['Mood Score']
    )
    
    # Display the Mood Chart
    # Streamlit's native area chart defaults to a nice purple/blue gradient in dark mode
    st.area_chart(chart_data, height=300, use_container_width=True)
    
    st.write("##") # Add some vertical space
    
    # 4. The Main Action
    # Use st.audio_input for the real recorder or a button for the design look
    if st.button("🎙️ Record New Entry"):
        st.info("Recording logic will go here in the next step!")

with col2:
    # 5. The Sidebar Stats (Using HTML for the Card Look)
    st.markdown("""
        <div class="stat-card">
            <p style="color: #B0B0B0; margin-bottom: 5px;">Quick Stats</p>
            <h2 style="margin: 0;">12 min</h2>
            <p style="color: #B0B0B0; font-size: 0.8rem;">recorded this week</p>
        </div>
        
        <div class="stat-card">
            <p style="color: #B0B0B0; margin-bottom: 5px;">Blast from the Past</p>
            <p style="font-style: italic; font-size: 0.9rem; color: #E0E0E0;">
                "Productive but slightly anxious about the meeting."
            </p>
            <p style="color: #00F2EA; font-size: 0.7rem; margin-top: 10px;">OCT 15, 2025</p>
        </div>
    """, unsafe_allow_html=True)