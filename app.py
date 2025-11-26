import streamlit as st
from agent import ai_agent, load_tasks

st.set_page_config(page_title="AI Productivity Agent", page_icon="⚡")

st.title("⚡ AI Productivity Agent")

st.write("Add, complete, and view tasks using natural language.")

user_input = st.text_area("What would you like to do? (Example: 'add task finish homework')")

if st.button("Run Agent"):
    if user_input.strip():
        response = ai_agent(user_input)
        st.success(response)

st.subheader("📋 Current Tasks")
tasks = load_tasks()
if tasks:
    for t in tasks:
        st.write(f"**{t['id']}. {t['task']}** — *{t['status']}*")
else:
    st.write("No tasks yet!")
