import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["Login page","Projects","Contacts"],
        menu_icon="cast",
        orientation="vertical",

    )

if selected == "Login page":
    def app():
        st.title("Welcome to :violet[smartbyte]")
        choice = st.selectbox("Login/Signup", ['Login', 'Signup'])
        if choice == 'Login':
            Email = st.text_input('Email address')
            Password = st.text_input('Password', type='password')
            st.button('Login')
        else:
            Email = st.text_input('Email address')
            Password = st.text_input('Password', type='password')

            username = st.text_input("enter the unique username")
            st.button("Create my account")
    app()

if selected == "Projects":
    st.title("sample chart")
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)

    st.title("Map chart")
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)

if selected == "Contacts":
    st.title(f"{selected}")


