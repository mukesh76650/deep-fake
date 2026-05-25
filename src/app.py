import streamlit as st
from PIL import Image
import torch
import os

# Placeholders for your existing detection code
from image_detector import load_model, preprocess_image, predict

MODEL_PATH = "../models/image_deepfake_model.pth"

st.title("Deepfake Detector (Image)")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
model = None

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    if model is None:
        if os.path.exists(MODEL_PATH):
            model = load_model(MODEL_PATH)
        else:
            st.error("Model file not found! Please train or add a model at models/image_deepfake_model.pth.")
    
    if model is not None:
        image_tensor = preprocess_image(uploaded_file)
        result = predict(model, image_tensor)
        st.success(f"The image is: {result.upper()}")

st.markdown(
    """
    ---
    **Note:** This demo currently only supports images. For videos, code extension is needed.
    """
)
