import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="VGS Adventure India",page_icon="🚩")
st.snow()
st.header(":red[Vaibhav Borse] 😎")
st.sidebar.title("Smartbyte Computer Education")
st.sidebar.text_input("Mail address")
st.sidebar.text_input("Password")
st.sidebar.button('Click here')
st.sidebar.radio("Your age between",["5-10","11-15","16-20","21-25"])
st.title("Bar chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("Line chart")
st.line_chart(data)
st.title("Area chart")
st.area_chart(data)
st.sidebar.file_uploader(":yellow[Upload your file/folder]")
st.chat_input("Type here")
st.status("Working")
