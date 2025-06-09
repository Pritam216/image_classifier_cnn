# 🐱🐶 Cat vs. Dog Image Classifier 🐶🐱

This is a simple Streamlit web application that uses a deep learning model to classify uploaded images as either a cat or a dog.

## 🚀 Features

* **Image Upload:** Easily upload your `.jpg`, `.jpeg`, or `.png` image files.
* **Real-time Prediction:** Get instant classification results (Cat or Dog).
* **Streamlit Interface:** User-friendly web interface.

## ✨ How it Works

The application uses a Convolutional Neural Network (CNN) model, which has been trained on a dataset of cat and dog images. When you upload an image:
1.  The image is preprocessed (resized to 256x256 pixels).
2.  The preprocessed image is fed into the trained CNN model.
3.  The model outputs a prediction (0 for Cat, 1 for Dog, or a probability which is then thresholded).
4.  The result is displayed on the Streamlit interface.

## ⚙️ Setup and Installation

Follow these steps to get the application running on your local machine:

### 1. Clone the Repository (or Download)

If you're using Git:
```bash
git clone [https://github.com/Pritam216/image_classifier_cnn.git](https://github.com/Pritam216/image_classifier_cnn.git)
cd your-repo-name
```

If you prefer to download:
* Go to your GitHub repository page.
* Click on the green "Code" button and select "Download ZIP".
* Extract the contents of the ZIP file to your desired project directory.

### 2. Prepare the Model

This project relies on a pre-trained model saved as `saved_model.pkl`.
* **Ensure `saved_model.pkl` is present in the root directory of your project.** This file should be generated after you train your model (e.g., using the `cat_Vs_dog_classification.ipynb` notebook if you followed that path).

### 3. Install Dependencies

Navigate to your project directory in your terminal or command prompt and install the required Python packages:

```bash
pip install streamlit tensorflow opencv-python numpy Pillow
```

### 4. Run the Streamlit Application

Execute the Streamlit application from your project's root directory:

```bash
streamlit run app.py
```

This will open the application in your default web browser.

## 📁 Project Structure

```
your-repo-name/
├── app.py                     # Main Streamlit application file
├── predict_page.py            # Contains the classification logic and model loading function
├── saved_model.pkl            # The trained deep learning model (crucial for prediction)
└── README.md                  # This file
```

## ⚠️ Important Notes

* **Model Size:** If `saved_model.pkl` is very large (>100MB), you might need to use Git Large File Storage (Git LFS) to upload it to GitHub.
* **Model Accuracy:** The accuracy of the classification depends on the training data and the model architecture used.
* **Image Format:** Ensure uploaded images are standard formats (JPG, PNG).

## 🤝 Contributing

Feel free to fork this repository, open issues, or submit pull requests if you have suggestions or improvements!

---

**Made with ❤️ by [Pritam Kumar Roy/Pritam216]**
```
