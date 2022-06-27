from tracemalloc import Statistic
import streamlit as st
import pandas as pd
import seaborn as sns


#1.Title and subhedder
st.title("Data Analysis")
st.subheader("Data Analysis using python and streamlit")



#2. Upload Dataset
upload=st.file_uploader("Uplode Your Dataset (in CSV Formate)")

if upload is not None:
    data=pd.read_csv(upload)


#Show dataset
if upload is not  None:
    if st.checkbox("Preview Dataset"):

        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

#4.Cheak 
if upload is not None:
    if st.checkbox("DataType of Each Columns"):
        st.text("DataType")
        st.write(data.dtypes.astype(str))

if upload is not None:
    data_shape=st.radio("what Dimensions Do You Want To Cheak ?",("Rows",'Columns'))

    if data_shape=="Rows":
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of columns")
        st.write(data.shape[1])


#5.null values
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null in the Dataset"):
            sns.heatmap(data.isnull())
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    else:
        st.success("Congrotulations!!,NO Missing Values")


#Find duplicate values

if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")

        dup=st.selectbox("Do You Want To Remove Duplicate Values ?",("Select One","Yes","NO"))

        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="NO":
            st.text("Ok NO Problem")

#8.Get Overall Statistic

if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include="all").astype(str))


# About section
if st.button("About App"):
    st.text("Built By Amit")
    st.text("Thanks For Using")

if st.checkbox("By"):
    st.text("Muh Me lele")
