import streamlit as st
from PIL import Image

# Streamlit form title
st.title("Streamlit Form Example")

# Using Streamlit's form
with st.form(key="my_form"):
    # Input Text
    name = st.text_input("Enter your name")

    # Text Area (Multiline input)
    address = st.text_area("Enter your address")

    # Radio Button Selection
    gender = st.radio("Select your gender", ("Male", "Female", "Other"))

    # To-Do List (Checkboxes)
    st.subheader("To-Do List")
    task1 = st.checkbox("Task 1: Complete Project")
    task2 = st.checkbox("Task 2: Attend Meeting")
    task3 = st.checkbox("Task 3: Read Documentation")

    # Slider (Volume Control)
    volume = st.slider("Set the Volume", 0, 100, 50)

    # File Upload (Generic file)
    uploaded_file = st.file_uploader("Upload a file", type=['txt', 'pdf', 'docx'])

    # File Upload (Photo)
    uploaded_photo = st.file_uploader("Upload a photo", type=['png', 'jpg', 'jpeg'])

    # Submit button to submit the form
    submit_button = st.form_submit_button(label="Submit")

# Check if form was submitted
if submit_button:
    st.success(f"Form submitted successfully by {name}")

    # Displaying the user inputs
    st.write(f"Name: {name}")
    st.write(f"Address: {address}")
    st.write(f"Gender: {gender}")

    st.subheader("To-Do List:")
    if task1:
        st.write("- Task 1: Complete Project")
    if task2:
        st.write("- Task 2: Attend Meeting")
    if task3:
        st.write("- Task 3: Read Documentation")
    
    st.write(f"Volume level: {volume}")

    # Handling file upload
    if uploaded_file:
        st.write(f"Uploaded file: {uploaded_file.name}")
    
    # Display uploaded photo if available
    if uploaded_photo is not None:
        image = Image.open(uploaded_photo)
        st.image(image, caption='Uploaded photo', use_column_width=True)

# Using other Streamlit widgets outside the form to explore more features
st.header("Other Streamlit Features")

# Example of a sidebar
st.sidebar.header("Sidebar")
st.sidebar.text("This is an example sidebar")

# Example of a drag-and-drop numeric input
st.sidebar.subheader("Drag-and-Drop Numeric Input")
number_input = st.sidebar.number_input("Select a number", min_value=0, max_value=100, value=25)
st.sidebar.write(f"Selected number: {number_input}")

# Example of a color picker
st.sidebar.subheader("Color Picker")
color = st.sidebar.color_picker("Pick a color")
st.write(f"Selected color: {color}")

# Example of a progress bar
st.sidebar.subheader("Progress Bar")
progress_value = st.sidebar.slider("Progress", 0, 100, 50)
progress_bar = st.progress(progress_value)

# Example of a map
st.header("Map Example")
st.map()  # Displays a default map

# to run:
# streamlit run <filename>