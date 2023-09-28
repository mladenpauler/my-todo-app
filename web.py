import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

if "my_text" not in st.session_state:
    st.session_state.new_todo = ""


st.title("Lista za kupovinu")
#st.subheader("This is my todo app.")
st.write("Ukucaj dole jedan po jedan artikal i pritisni Enter.")
st.write("Ako napravis gresku samo klikni na kockicu pored artikla i to ce ga izbrisati.")

st.text_input(label="Ukucaj proizvod", placeholder="Ukucaj novi proizvod...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



