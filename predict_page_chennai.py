import streamlit as st
import numpy as np
import pickle


#loading the ml model
def load_model():
    with open('saved_steps_of_chennai_prediction.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


#encoding the categorical variables
linear_regressor = data["model"]
le_area = data["le_area"]
le_sale_cond = data["le_sale_cond"]
le_park_facil = data["le_park_facil"]
le_buildtype = data["le_buildtype"]
le_utility_avail = data["le_utility_avail"]
le_street = data["le_street"]
le_mzzone = data["le_mzzone"]


#function to run on page load
def show_predict_page_chennai():
    st.title("CHENNAI PROPERTY PRICE PREDICTION")
    st.write("""### We need some information for prediction""")

    area = (
        "chrompet",
        "karapakkam",
        "kk nagar",
        "velachery",
        "anna nagar",
        "adyar",
        "t nagar"
    )

    sale_cond = (
        "AdjLand",
        "Normal Sale",
        "Partial",
        "AbNormal",
        "Family",
        "Adj Land",
        "Ab Normal",
        "Partiall",
        "PartiaLl"
    )

    park_facil = (
        "yes",
        "no"
    )

    buildtype = (
        "house",
        "other",
        "commercial"
    )

    utility_avail = (
        "nosewr",
        "allpub",
        "elo"
    )

    street = (
        "paved",
        "gravel",
        "no access"
    )

    mzzone = (
        "rl",
        "rh",
        "rm",
        "c",
        "a",
        "i"
    )



    area = st.selectbox("Area", area)
    int_sqft = st.number_input("Enter the sqft area")
    dist_mainroad = st.number_input("Enter the distance from the mainroad")
    n_bedroom = st.number_input("Enter the number of bedrooms")
    n_bathroom = st.number_input("Enter the number of bathrooms")
    n_room = st.number_input("Enter the number of rooms")
    sale_cond = st.selectbox("Sale Condition", sale_cond)
    park_facil = st.selectbox("Park Facil", park_facil)
    buildtype = st.selectbox("Buildtype", buildtype)
    utility_avail = st.selectbox("Utility Available", utility_avail)
    street = st.selectbox("Street", street)
    mzzone = st.selectbox("Mzzone", mzzone)
    reg_fee = st.number_input("Enter the registration fee")
    commis = st.number_input("Enter the commission")
    sales_price = st.number_input("Enter the sales price")
    property_age = st.number_input("Enter the age of the property")


    ok = st.button("PREDICT PRICE")

    #if ok is true, which means the button is clicked, prediction result is to be shown

    if ok:
        XINPUT = np.array([[area, int_sqft, dist_mainroad, n_bedroom, n_bathroom, n_room, sale_cond, park_facil, buildtype, utility_avail, street, mzzone, reg_fee, commis,sales_price, property_age ]])

        XINPUT[:, 0] = le_area.transform(XINPUT[:, 0])
        XINPUT[:, 6] = le_sale_cond.transform(XINPUT[:, 6])
        XINPUT[:, 7] = le_park_facil.transform(XINPUT[:, 7])
        XINPUT[:, 8] = le_buildtype.transform(XINPUT[:, 8])
        XINPUT[:, 9] = le_utility_avail.transform(XINPUT[:, 9])
        XINPUT[:, 10] = le_street.transform(XINPUT[:, 10])
        XINPUT[:, 11] = le_mzzone.transform(XINPUT[:, 11])

        XINPUT = XINPUT.astype('float')

        price = linear_regressor.predict(XINPUT)
        st.subheader("The price(in lacs) of the property you desire is {}  : ".format(price[0]))