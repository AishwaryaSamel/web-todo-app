#we are using streamlit library. easy to create webpps, intuitive, easy to integrate with graphs. so easy to make graphs and data.
# run below code on python terminal
# streamlit run web.py
# run below code on terminal to generate the requirements.txt file
#it installs the packages with their versions that streamlit uses and then run our python code
# pip freeze > requirements.txt

import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    functions.write_todos(todos)

st.set_page_config(layout="wide")

st.title("My ToDo App")
st.subheader("This is my todo app")
st.write("<i>This app is designed to increase one's productivity.</i>",unsafe_allow_html=True)

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new todo...", on_change=add_todo, key="new_todo")

# st.session_state





