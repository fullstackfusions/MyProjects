"""
using streamlit you can perform following task:

- Produce data in kafka
- Submit data in rest api
- prepare minimum viable product

""" 
import os
import streamlit as st
from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime
import json

class Response(BaseModel):

    author: str
    timestamp: int
    payload: Dict[Any, Any]
    metadata: Dict[Any, Any]


def load_json_files():
    json_files = []
    json_data = []

    directory = "custom_data/"
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(fp=file)
                response = Response(**data)
                json_files.append(filename)
                json_data.append(response)
    
    return json_files, json_data


def create_json_structure():
    st.title("Customize JSON Data")

    
    json_files, json_data = load_json_files()

    selected_file = st.selectbox("Select JSON file", ["None"] + json_files)

    response_instance = None
    if selected_file and selected_file != "None":
        selected_json_data = json_data[json_files.index(selected_file)]
        selected_json_data.timestamp = int(round(datetime.now().timestamp()) * 1e3)

        # do some other operation if you like

        response_instance = selected_json_data
        st.subheader("Selected JSON Data")
        st.json(response_instance.json())


    # Button to produce JSON to Kafka or any other operation
    if st.button("Submit Data"):
        st.json(response_instance.json())
        # Here you can implement the logic to send the data to kafka
        # or you can also submit the data to any api
        st.success("Data submitted successfully!")
    

if __name__ == "__main__":
    create_json_structure()


# to run:
# streamlit run <filename>