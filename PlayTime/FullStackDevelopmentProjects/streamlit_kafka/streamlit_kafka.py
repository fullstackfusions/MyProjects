# Produce dummy data in kafka using streamlit ui

import streamlit as st
from pydantic import BaseModel
from typing import Dict
from datetime import datetime
import json
from kafka import KafkaProducer  # Adjust imports as necessary

# Define your Kafka Producer (assuming you have your settings in kafkaproducer.py)
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Replace with your Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize JSON data to UTF-8 bytes
)

def create_json_structure():
    st.title("Customize JSON Data")

    # Top-level fields
    total_count = st.number_input("Total Count", min_value=0, value=1)
    next_page_key = st.text_input("Next Page Key (Leave blank for null)", value="")
    resolution = st.text_input("Resolution", value="5m")

    st.header("Result")
    metric_id = st.text_input("Metric ID", value="some_id")
    data_point_count_ratio = st.number_input("Data Point Count Ratio", value=0.00000375, format="%f")
    dimension_count_ratio = st.number_input("Dimension Count Ratio", value=0.00015, format="%f")

    st.subheader("Data")
    # Inputs for list of timestamps
    timestamps = st.text_area("Timestamps (Enter each timestamp on a new line)", value="172540380000")
    timestamps_list = [int(ts.strip()) for ts in timestamps.split("\n") if ts.strip()]

    # Inputs for list of values
    values = st.text_area("Values (Enter each value on a new line)", value="1.447017585907307")
    values_list = [float(val.strip()) for val in values.split("\n") if val.strip()]

    # Inputs for list of dimensions
    dimensions = st.text_area("Dimensions (Enter each dimension on a new line)", value="")
    dimensions_list = [dim.strip() for dim in dimensions.split("\n") if dim.strip()]

    # Inputs for dictionary of dimensionMap
    st.text("Dimension Map")
    dim_keys = st.text_area("Keys (Enter each key on a new line)", value="")
    dim_values = st.text_area("Values (Enter each value on a new line)", value="")

    # Convert key-value input to dictionary
    dimension_map_dict = {}
    if dim_keys and dim_values:
        keys_list = dim_keys.split("\n")
        values_list_map = dim_values.split("\n")
        if len(keys_list) == len(values_list_map):
            dimension_map_dict = {k.strip(): v.strip() for k, v in zip(keys_list, values_list_map)}

    # Create the JSON structure
    json_result = {
        "totalCount": total_count,
        "nextPageKey": next_page_key if next_page_key else None,
        "resolution": resolution,
        "result": [
            {
                "metricId": metric_id,
                "dataPointCountRatio": data_point_count_ratio,
                "dimensionCountRatio": dimension_count_ratio,
                "data": [
                    {
                        "dimensions": dimensions_list,
                        "dimensionMap": dimension_map_dict,
                        "timestamps": timestamps_list,
                        "values": values_list,
                    }
                ]
            }
        ]
    }

    # Create a Response instance using the json_result as the payload
    response_instance = dict(payload=json_result)

    st.subheader("Generated JSON")
    st.json(response_instance.dict())  # Display the Response instance as JSON

    # Button to produce JSON to Kafka or any other operation
    if st.button("Submit Data"):
        # Produce the data to Kafka
        producer.send('your_topic', value=response_instance.dict())  # Replace 'your_topic' with your Kafka topic name
        producer.flush()  # Ensure all messages are sent
        st.success("Data submitted successfully and produced to Kafka!")

if __name__ == "__main__":
    create_json_structure()
