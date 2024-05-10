import streamlit as st
import numpy as np
import pickle


#loading the ml model
def load_model():
    with open('saved_steps_of_paris_prediction.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


#encoding the categorical variables
non_linear_regressor = data["model"]


#function to run on page load
def show_predict_page_paris():
    st.title("PARIS PROPERTY PRICE PREDICTION")
    st.write("""### We need some information for prediction""")


    square_metres = st.number_input("Enter the square meters area")
    number_of_rooms = st.number_input("Enter the number of rooms")
    hasYard = st.number_input("Yard : Enter 0 for no and 1 for yes")
    hasPool = st.number_input("Pool : Enter 0 for no and 1 for yes")
    floors = st.number_input("Enter the number of floors")
    cityCode = st.number_input("enter the city code")
    cityPartRange = st.number_input("Enter the range")
    numPrevOwners = st.number_input("Enter the number of previous owners")
    made = st.number_input("Enter the year in which it was made")
    isNewBuilt = st.number_input("Enter 0 if it is not newly built and 1 if it is newly built")
    hasStormProtector = st.number_input("Enter 0 if it doesn't have storm protector and 1 if it has storm protector")
    basement = st.number_input("Enter the number of basement")
    attic = st.number_input("Enter the number of attic")
    garage = st.number_input("Enter the number of garage")
    hasStorageRoom = st.number_input("Enter 0 if it does not have storage room and 1 if it has storage room")
    hasGuestRoom = st.number_input("Enter the number of guest rooms")



    ok = st.button("PREDICT PRICE")

    #if ok is true, which means the button is clicked, prediction result is to be shown

    if ok:
        XINPUT = np.array([[square_metres, number_of_rooms, hasYard, hasPool, floors, cityCode, cityPartRange, numPrevOwners, made, isNewBuilt, hasStormProtector, basement, attic, garage, hasStorageRoom, hasGuestRoom]])

        price = non_linear_regressor.predict(XINPUT)
        st.subheader("The price(in lacs) of the property you desire is {}  : ".format(price[0]))