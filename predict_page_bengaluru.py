import streamlit as st
import numpy as np
import pickle


#loading the ml model
def load_model():
    with open('saved_steps_of_bengaluru_prediction.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


#encoding the categorical variables
linear_regressor = data["model"]
le_location = data["le_location"]


#function to run on page load
def show_predict_page_bengaluru():
    st.title("BENGALURU PROPERTY PRICE PREDICTION")
    st.write("""### We need some information for prediction""")



    location = st.text_input("Location")
    total_sqft = st.number_input("Enter the total sqft. area")
    bath = st.number_input("Enter the number of bathrooms")
    bhk = st.number_input("Enter the number of bhk")


    ok = st.button("PREDICT PRICE")

    #if ok is true, which means the button is clicked, prediction result is to be shown

    if ok:
        XINPUT = np.array([[location, total_sqft, bath, bhk]])

        XINPUT[:, 0] = le_location.transform(XINPUT[:, 0])
        XINPUT = XINPUT.astype('float')



        price = linear_regressor.predict(XINPUT)
        st.subheader("The price(in lacs) of the property you desire is {}  : ".format(price[0]))