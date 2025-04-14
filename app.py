# app.py (Simplified Demo Version)
import streamlit as st
import json
from datetime import datetime, timedelta
from utils import load_data, save_data, calculate_total_hours

st.set_page_config(page_title="Time Tracker Chatbot", layout="centered")

# ---------------- User Login ----------------
st.title("🕒 Time Tracker Chatbot")
username = st.text_input("Enter your name to login:")
if username:
    data = load_data(username)

    # --------------- Setup Month ----------------
    st.subheader("1. Select Month Duration")
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", key="start")
    with col2:
        end_date = st.date_input("End Date", key="end")

    # --------------- Work Hours Setup ----------------
    st.subheader("2. Set Your Daily Work Hours")
    start_time = st.time_input("Start Time", key="work_start")
    end_time = st.time_input("End Time", key="work_end")

    # --------------- Daily Time IN/OUT ----------------
    st.subheader("3. Daily Time Entry")
    today = datetime.now().date()
    time_in = st.time_input("Time IN", key="in")
    time_out = st.time_input("Time OUT", key="out")

    if st.button("Submit Today's Timing"):
        if "entries" not in data:
            data["entries"] = []
        data["entries"].append({
            "date": str(today),
            "in": str(time_in),
            "out": str(time_out)
        })
        save_data(username, data)
        st.success("Time entry saved!")

    # --------------- Show Summary ----------------
    if st.button("Show Month Summary"):
        total_hours = calculate_total_hours(data.get("entries", []))
        st.info(f"🧾 Total hours worked: **{total_hours} hours**")
