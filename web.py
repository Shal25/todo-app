import streamlit as st
import functions
todo = functions.get_todos()
st.title("My Todo App")
for i in todo:
    st.checkbox(i)
st.text_input(label="", placeholder="Add a new todo...")
print("hello")
