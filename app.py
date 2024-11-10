import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
# file1=open("RandomForestModel.pk1","rb")
# model=pickle.load(file1)
# file1.close()
model=joblib.load(open('finalProject2.pkl','rb'))

data=pd.read_csv("finalProjectData.csv")

#Create a title for the website
st.title("Car Price Prediction Website:")

#Create a selection box for the model/company make type
Model=st.selectbox("Model",data["Model"].unique())

#Create a selection box for the company
filtered_make_options = data[data["Model"] == Model]["Make"].unique()
Make = st.selectbox("Select Make", filtered_make_options)

#Input the year the car was made
YOM=st.number_input("Year the car was made")

#Used=>Whether foreign used or brandnew or  locally used
Used=st.selectbox("Used",data["Used"].unique())

#Transmission of the car
Transmission=st.selectbox("Car Transmission",data["Transmission"].unique())

#Car mileage
Mileage=st.number_input("Enter the mileage of the car")

#Location where the car is used
Location=st.selectbox("Location",data["Location"].unique())

#input the age of the car
Age=st.number_input("Age of the Car")

#input the fuel type the car consumes
Fuel_Type=st.selectbox("Fuel_type",data["Fuel_Type"].unique())

#Create the predict button
if st.button('Predict Price'):
    # [Model, Make, YOM, Used, Transmission, Mileage, Location, Age, Fuel_Type]

    prediction=int(model.predict(pd.DataFrame(columns=["Model","Make","YOM","Used","Transmission","Mileage","Location","Age","Fuel_Type"],
                             data=np.array([Model,Make,YOM,Used,Transmission,Mileage,Location,Age,Fuel_Type]).reshape(1,9))))
    print("Hello world")
    st.title("The car price ranges between " +
             str(prediction - 20000) + " Ksh " + " - " + str(prediction +20000) + " Ksh " )

# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib

# # Cache the model and data loading
# def load_model():
#     return joblib.load(open('finalProject2.pkl', 'rb'))

# def load_data():
#     return pd.read_csv('finalProjectData.csv')

# # Load the model and data
# model = load_model()
# data = load_data()

# # Website Title
# st.title("Car Price Prediction Website")

# # User Input: Select Model
# Model = st.selectbox("Select Model", data["Model"].unique())

# # Filter Make options based on selected Model
# filtered_make_options = data[data["Model"] == Model]["Make"].unique()
# Make = st.selectbox("Select Make", filtered_make_options)

# # Year of Manufacture
# YOM = st.number_input("Year the car was made", min_value=1900, max_value=2024, step=1)

# # Foreign used/brand new/local
# Used = st.selectbox("Used", data["Used"].unique())

# # Car Transmission Type
# Transmission = st.selectbox("Car Transmission", data["Transmission"].unique())

# # Car Mileage
# Mileage = st.number_input("Enter the mileage of the car", min_value=0)

# # Car Location
# Location = st.selectbox("Location", data["Location"].unique())

# # Car Age
# Age = st.number_input("Age of the Car", min_value=0, step=1)

# # Fuel Type
# Fuel_Type = st.selectbox("Fuel_type", data["Fuel_Type"].unique())

# # Predict Button Logic
# if st.button('Predict Price'):
#     try:
#         # Prepare the input data
#         input_data = pd.DataFrame(
#             data=[[Model, Make, YOM, Used, Transmission, Mileage, Location, Age, Fuel_Type]],
#             columns=["Model", "Make", "YOM", "Used", "Transmission", "Mileage", "Location", "Age", "Fuel_Type"]
#         )

#         # Make the prediction
#         prediction = int(model.predict(input_data)[0])

#         # Display the prediction
#         st.title(f"The car price ranges between {prediction - 20000} Ksh - {prediction + 20000} Ksh")

#     except Exception as e:
#         st.error(f"Error during prediction: {e}")









