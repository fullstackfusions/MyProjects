"""

A streamlit ui frontend for todo list

How to run this?

streamlit run streamlit_frontend.py

"""


import streamlit as st
import requests
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

# Backend API URLs
login_url = "http://127.0.0.1:8000/token"
user_me_url = "http://127.0.0.1:8000/users/me"
get_todos_url = "http://127.0.0.1:8000/todos"
get_single_todo_url = "http://127.0.0.1:8000/todo"
add_todo_url = "http://127.0.0.1:8000/todo"
update_todo_url = "http://127.0.0.1:8000/todo"
delete_todo_url = "http://127.0.0.1:8000/todo"



# Pydantic Model for To-Do Item
class TodoItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoItem(TodoItemBase):
    id: int
    created_by: Optional[str] = Field(None, exclude=True)  # Exclude from user input
    created_at: Optional[datetime] = Field(default_factory=datetime.now, exclude=True)  # Auto-populate with current time
    updated_at: Optional[datetime] = Field(default_factory=datetime.now, exclude=True)

    # class Config:
    #     orm_mode = True  # Enables using Pydantic model with ORMs, like MongoDB
    #     extra = 'forbid'  # Prevents users from adding extra fields



# Initialize session state for login
if "access_token" not in st.session_state:
    st.session_state["access_token"] = None
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def login(username, password):
    response = requests.post(login_url, data={"username": username, "password": password})
    if response.status_code == 200:
        st.session_state["access_token"] = response.json().get("access_token")
        st.session_state["logged_in"] = True
        st.success("Logged in successfully!")
    else:
        st.error("Login failed. Please check your credentials.")



# def get_current_user():
#     headers = {"Authorization": f"Bearer {st.session_state['access_token']}"}
#     response = requests.get(user_me_url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         st.error("Failed to fetch user details.")
#         return None


def add_todo_item(todo_item: TodoItemBase):
    headers = {"Authorization": f"Bearer {st.session_state['access_token']}"}
    data = todo_item.model_dump()
    response = requests.post(add_todo_url, json=data, headers=headers)
    if response.status_code == 200:
        st.success("To-Do item added successfully")
    else:
        st.error("Failed to add To-Do item")


def get_todos():
    headers = {"Authorization": f"Bearer {st.session_state['access_token']}"}
    response = requests.get(get_todos_url, headers=headers)
    try:
        # st.info(response.text)
        if response.status_code == 200:
            # may be here I am getting serialization error and for that reason it goes to else part.
            # print(response.json())
            return response.json()
        else:
            st.error("Failed to fetch To-Do items")
            return []
    except Exception as e:
        print(e)

def get_single_todo(id: int):
    headers = {"Authorization": f"Bearer {st.session_state['access_token']}"}
    response = requests.get(f"{get_single_todo_url}/{id}", headers=headers)
    try:
        # st.info(response.text)
        if response.status_code == 200:
            # may be here I am getting serialization error and for that reason it goes to else part.
            # print(response.json())
            return response.json()
        else:
            st.error("Failed to fetch To-Do items")
            return None
    except Exception as e:
        print(e)

def update_todo_item(id: int, todo_item: TodoItemBase):
    headers = {"Authorization": f"Bearer {st.session_state['access_token']}"}
    # json_data = {"title": title, "description": description, "completed": completed}
    json_data = todo_item.model_dump()
    st.info(json_data)
    response = requests.put(f"{update_todo_url}/{id}", json=json_data, headers=headers)
    if response.status_code == 200:
        st.success("To-Do item updated successfully")
    else:
        st.info(response.text)
        st.error("Failed to update To-Do item")

def delete_todo_item(id: int):
    headers = {"Authorization": f"Bearer {st.session_state['access_token']}"}
    response = requests.delete(f"{delete_todo_url}/{id}", headers=headers)
    if response.status_code == 200:
        st.success("To-Do item deleted successfully")
    else:
        st.error("Failed to delete To-Do item")


# App logic
if not st.session_state["logged_in"]:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username, password)
else:
    st.title("To-Do Manager")



    # Display buttons for To-Do operations
    # if st.button("Get To-Do Items"):
    #     todos = get_todos()
    #     if todos:
    #         st.write("Your To-Do Items:")
    #         for todo in todos:
    #             # st.write(f"Title: {todo['title']}, Completed: {todo['completed']}")
    #             st.write(f"**ID:** {todo['id']}, **Title:** {todo['title']}, **Completed:** {todo['completed']}")
    
    todos = get_todos()

    if todos:
        for todo in todos:
            if todo:
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    st.write(f"**ID:** {todo['id']}")
                    st.write(f"**Title:** {todo['title']}")
                    st.write(f"**Description:** {todo['description']}")
                    st.write(f"**Completed:** {todo['completed']}")

                # Update Section
                with col2:
                    # Create an expand button for each todo to show the update form
                    with st.expander(f"Update To-Do {todo['id']}"):
                        # Fields for updating the To-Do item
                        title = st.text_input(f"Update title {todo['id']}", todo['title'])
                        description = st.text_input(f"Update description {todo['id']}", todo['description'])
                        completed = st.checkbox(f"Completed {todo['id']}", todo['completed'])

                        # Once the user modifies the data, they can submit the update
                        if st.button(f"Submit Update {todo['id']}"):
                            updated_todo = TodoItemBase(title=title, description=description, completed=completed)
                            update_todo_item(todo['id'], updated_todo)
                            st.success(f"To-Do {todo['id']} updated successfully!")
                            # st.experimental_rerun()  # Rerun the app to show the updated todos

                # Delete Section
                with col3:
                    # Add delete button for each todo
                    if st.button(f"Delete {todo['id']}"):
                        delete_todo_item(todo['id'])
                        st.success(f"To-Do {todo['id']} deleted successfully!")
                        # st.experimental_rerun()  # Rerun the app to show updated todos after deletion
    
    try:
        st.write("Add a new To-Do item:")
        title = st.text_input("Title")
        description = st.text_input("Description")
        completed = st.checkbox("Completed")
        todo_item = TodoItemBase(title=title, description=description, completed=completed)
        if st.button("Add To-Do Item"):
            add_todo_item(todo_item)
    except Exception as e2:
        print(e2)


    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["access_token"] = None
        st.experimental_rerun()
