import streamlit as st
import numpy as np
import pickle


#loading the ml model
def load_model():
    with open('saved_steps_of_delhi_prediction.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


#encoding the categorical variables
random_forest_regressor = data["model"]
le_location = data["le_location"]
le_Status = data["le_Status"]
le_Type = data["le_Type"]


#function to run on page load
def show_predict_page_delhi():
    st.title("DELHI PROPERTY PRICE PREDICTION")
    st.write("""### We need some information for prediction""")

    Status = (
        "Unfurnished",
        "Semi-Furnished",
        "Furnished",
    )

    Type = (
        "Floor",
        "Apartment",
        "Villa",
        "House",
        "penthouse"
    )



    location = st.text_input("Location")
    Status = st.selectbox("Status", Status)
    bhk = st.number_input("Enter the number of bhk")
    Type = st.selectbox("Type", Type)
    bath = st.number_input("Enter the number of bathrooms")
    balcony = st.number_input("Enter the number of balconies")


    ok = st.button("PREDICT PRICE")

    #if ok is true, which means the button is clicked, prediction result is to be shown

    if ok:
        XINPUT = np.array([[location, Status, bhk, Type, bath, balcony]])


        XINPUT[:, 0] = le_location.transform(XINPUT[:, 0])
        XINPUT[:, 1] = le_Status.transform(XINPUT[:, 1])
        XINPUT[:, 3] = le_Type.transform(XINPUT[:, 3])
        XINPUT = XINPUT.astype('float')

        price = random_forest_regressor.predict(XINPUT)
        st.subheader("The price(in lacs) of the property you desire is {}  : ".format(price[0] * 1000))