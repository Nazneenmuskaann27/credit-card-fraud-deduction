import streamlit as st
import numpy as np
import pickle
def set_background_image(image_url):
    # Apply custom CSS to set the background image
    page_bg_img = '''
    <style>
    .stApp {
        background-position: top;
        background-image: url(%s);
        background-size: cover;
    }

    @media (max-width: 768px) {
        /* Adjust background size for mobile devices */
        .stApp {
            background-position: top;
            background-size: contain;
            background-repeat: no-repeat;
        }
    }
    </style>
    ''' % image_url
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    # Set the background image URL
    background_image_url ="https://image.slidesdocs.com/responsive-images/background/bank-card-credit-card-blue-powerpoint-background_7ca958fc07__960_540.jpg"
    # Set the background image
    set_background_image(background_image_url)

    custom_css = """
       <style>
       body {
           background-color: #4699d4;
           color: #ffffff;
           font-family: Arial, sans-serif;
       }
       select {
           background-color: #000000 !important; /* Black background for select box */
           color: #ffffff !important; /* White text within select box */
       }
       label {
           color: #ffffff !important; /* White color for select box label */
           font-size: 20px; /* Adjust font size for labels */
           font-weight: bold; /* Make labels bold */
       }
       h1, h2, h3 {
           font-weight: bold; /* Make headings bold */
           font-size: 24px; /* Adjust heading font size */
       }
       .whatsapp-stats {
           font-size: 20px; /* Adjust font size for WhatsApp stats */
           font-weight: bold; /* Make WhatsApp stats bold */
           color: #333333; /* Dark color for WhatsApp stats */
       }
       .stBlock {
           border-right: 2px solid #ffffff; /* Draw a vertical line */
           padding-right: 10px;
           margin-right: 10px;
       }
       .stBlock .stFileUploader {
           border: 1px solid #ffffff; /* Add a border around the file uploader */
           padding: 10px;
           margin: 10px;
       }
       </style>
       """

    st.markdown(custom_css, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
# Load the trained model
with open('credit_fraud_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Credit Card Fraud Detection")

# User inputs for features
V1 = st.number_input('V1', value=-1.359807)
V2 = st.number_input('V2', value=-0.072781)
V3 = st.number_input('V3', value=2.536346)
V4 = st.number_input('V4', value=1.378155)
V5 = st.number_input('V5', value=-0.338321)
V6 = st.number_input('V6', value=0.462388)
V7 = st.number_input('V7', value=0.239599)
V8 = st.number_input('V8', value=0.098698)
V9 = st.number_input('V9', value=0.363787)
V10 = st.number_input('V10', value=0.090794)
V11 = st.number_input('V11', value=-0.551600)
V12 = st.number_input('V12', value=-0.617801)
V13 = st.number_input('V13', value=-0.991390)
V14 = st.number_input('V14', value=-0.311169)
V15 = st.number_input('V15', value=1.468177)
V16 = st.number_input('V16', value=-0.470400)
V17 = st.number_input('V17', value=0.207971)
V18 = st.number_input('V18', value=0.025791)
V19 = st.number_input('V19', value=0.403993)
V20 = st.number_input('V20', value=0.251412)
V21 = st.number_input('V21', value=-0.018307)
V22 = st.number_input('V22', value=0.277838)
V23 = st.number_input('V23', value=-0.110474)
V24 = st.number_input('V24', value=0.066928)
V25 = st.number_input('V25', value=0.128539)
V26 = st.number_input('V26', value=-0.189115)
V27 = st.number_input('V27', value=0.133558)
V28 = st.number_input('V28', value=-0.021053)

# Amount input
Amount = st.number_input('Amount', value=149.62)

# Class input - Only include this if your model was trained with it
class_input = st.number_input('Class (0 or 1)', value=0)

# Prepare input features as a 2D array (30 features)
# Ensure the correct order and count of features
features = np.array([[V1, V2, V3, V4, V5, V6, V7, V8, V9, V10,
                      V11, V12, V13, V14, V15, V16, V17, V18,
                      V19, V20, V21, V22, V23, V24, V25, V26,
                      V27, V28, Amount, class_input]])  # Including the class feature

# Button to predict
if st.button("Predict"):
    try:
        prediction = model.predict(features)
        st.write("Prediction:", "Fraud" if prediction[0] == 1 else "Not Fraud")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
