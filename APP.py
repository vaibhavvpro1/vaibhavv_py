import streamlit  as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="VGS Adventure India",page_icon="🚩")
st.snow()
st.header(":red[Vaibhav Borse] 😎")
st.sidebar.title(":blue[Smartbyte Computer Education]")
st.sidebar.text_input(":Mail Address")
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
df = pd.DataFrame(columns=['name','age','color'])
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
}

result = st.data_editor(df, column_config = config, num_rows='dynamic')

if st.button('Get results'):
    st.write(result)
st.sidebar.file_uploader(":green[Upload your file/folder]")
st.chat_input("Type here")
st.status("Working")

