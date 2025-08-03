import streamlit as st
import torch
from PIL import Image
import numpy as np
import os

# Load model
@st.cache_resource
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='../yolov5/runs/train/smart_office_m/weights/best.pt', force_reload=True)
    return model

model = load_model()

# Streamlit UI
st.title("🧠 Smart Office Object Detector")
st.write("Upload an image to detect people and office objects.")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert image to numpy and run detection
    results = model(image)

    # Show detection results
    st.subheader("Detected Objects:")
    results_df = results.pandas().xyxy[0]
    st.dataframe(results_df[['name', 'confidence']])

    # Show image with bounding boxes
    st.image(np.squeeze(results.render()), caption='Detection Output', use_column_width=True)
