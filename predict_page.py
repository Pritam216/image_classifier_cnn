import streamlit as st
import pickle
import numpy as np
import cv2
from PIL import Image
import io
import tensorflow as tf

@st.cache_resource
def load_trained_model():
    try:
        with open('saved_model.pkl', 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        st.error("Error: 'saved_model.pkl' not found.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

model = load_trained_model()

def image_classifier_page():
    st.title("Cat vs. Dog Image Classifier")
    st.write("Upload an image, and I'll tell you if it's a cat or a dog!")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.', use_container_width=True)
        st.write("")
        st.write("Classifying...")

        if st.button("Predict"):
            try:
                image_bytes = uploaded_file.read()
                image_np = np.frombuffer(image_bytes, np.uint8)
                img = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

                if img is None:
                    st.error("Error: Could not decode the image. Please upload a valid image file.")
                else:
                    img = cv2.resize(img, (256, 256))
                    test_input = img.reshape((1, 256, 256, 3))
                    prediction = model.predict(test_input)
                    
                    predicted_value = prediction[0][0] 

                    if predicted_value == 0:
                        st.success("Prediction: It's a **CAT!** ")
                    elif predicted_value == 1:
                        st.success("Prediction: It's a **DOG!**")
                    else:
                        if predicted_value > 0.5:
                            st.success("Prediction: It's a **DOG!**")
                        else:
                            st.success("Prediction: It's a **CAT!**")
                        st.info(f"Raw prediction value: {predicted_value}.")

            except Exception as e:
                st.error(f"An error occurred during image processing or prediction: {e}")
                st.info("Please try another image or ensure the uploaded file is a valid image type.")