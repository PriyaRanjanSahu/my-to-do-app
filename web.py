import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + "\n"

    # Check if the new todo already exists
    if new_todo not in todos:
        todos.append(new_todo)
        functions.write_todos(todos)
        st.session_state['new_todo'] = ""  # Clear the input field
        st.success("Task Added Successfully!")

    else:
        st.warning("Task already exists.")


# def add_todo():
#     todo = st.session_state['new_todo'] + "\n"
#     todos.append(todo)
#     functions.write_todos(todos)


st.title("To-Do App")
st.subheader("Manage Your To-Do List")
st.write("This app is designed to help you stay organized and boost your productivity!")

selected_indices = []

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        selected_indices.append(index)

if st.button("Completed"):
    todos = [todo for index, todo in enumerate(todos) if index not in selected_indices]
    functions.write_todos(todos)
    st.experimental_rerun()


st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")
