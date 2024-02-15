import streamlit as st
from sklearn.linear_model import LogisticRegression
import numpy as np

# Title and description for intrusion detection section
st.title("Intrusion Detection System")
st.write("Enter the following features to check if the Connection is normal or abnormal:")

# Define features and their expected types
features = {
    'protocol_type': 'str', 'service': 'str', 'flag': 'str',
    'src_bytes': 'float', 'dst_bytes': 'float',
    'count': 'float', 'same_srv_rate': 'float',
    'dst_host_srv_count': 'float', 'dst_host_same_srv_rate': 'float',
    'dst_host_same_src_port_rate': 'float'
}

# Create input fields for user to enter feature values
feature_inputs = {}
for feature, feature_type in features.items():
    if feature_type == 'str':
        feature_inputs[feature] = st.text_input(f'{feature.capitalize()}')
    elif feature_type == 'float':
        feature_inputs[feature] = st.text_input(f'{feature.capitalize()} (numerical)')

# Create a button to submit input and get prediction
if st.button("Submit"):
    # Gather input values
    input_values = [feature_inputs[feature] for feature in features]

    # Check if all fields are filled
    if all(input_values):
        processed_data = []
        for feature, value in zip(features.keys(), input_values):
            try:
                if features[feature] == 'float':
                    numeric_value = float(value)
                    processed_data.append(numeric_value)
                else:
                    processed_data.append(value)
            except ValueError:
                st.write(f"Invalid input for {feature.capitalize()}. Please enter a valid value.")
                break
        else:
            # Make prediction using your machine learning model
            prediction = [0]  # Mock prediction: 0 for Normal, 1 for Anomal

            # Display result
            if prediction[0] == 0:
                st.write("Normal Connection")
            else:
                st.write("Anomal Connection")
    else:
        st.write("Please fill in all feature values.")