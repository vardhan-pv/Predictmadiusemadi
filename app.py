import streamlit as st
import pandas as pd
import pickle
from datetime import datetime, timedelta
import os

st.set_page_config(page_title="Storage AI Predictor", layout="wide")
st.title("📊 Storage AI Dashboard")

def get_tangible_estimates(free_mb):
    return {
        "photos": int(free_mb // 3.5),      # Avg 3.5MB per photo
        "video_mins": int(free_mb // 400),   # Avg 400MB per min of 4K
        "docs": int(free_mb // 0.5)         # Avg 0.5MB per Doc
    }

# Sidebar for User Inputs
with st.sidebar:
    st.header("⚙️ Storage Settings")
    total_gb = st.number_input("Total Drive Size (GB)", min_value=1, value=512)
    used_gb = st.number_input("Current Used (GB)", min_value=0, value=200)
    total_mb = total_gb * 1024
    used_mb = used_gb * 1024

if os.path.exists('trend_models.pkl'):
    with open('trend_models.pkl', 'rb') as f:
        trends = pickle.load(f)
    
    free_mb = total_mb - used_mb
    daily_usage = sum(trends.values())
    days_left = int(free_mb / daily_usage) if daily_usage > 0 else 999
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📅 Days Until Full", f"{max(0, days_left)} Days")
        st.write(f"Remaining Storage: **{max(0, free_mb):,.0f} MB**")

    with col2:
        st.subheader("💡 What fits in your leftover space?")
        est = get_tangible_estimates(free_mb)
        st.write(f"📸 **{est['photos']:,}** High-res Photos")
        st.write(f"🎥 **{est['video_mins']:,}** Mins of 4K Video")
        st.write(f"📄 **{est['docs']:,}** Documents")
else:
    st.warning("Please run models.py first to initialize the AI.")