import streamlit as st
import pandas as pd
import numpy as np
import time

 
st.title("Chaitanya Purkar(Title)")
st.header("Chaitanya Purkar(Header)")
st.subheader("Chaitanya Purkar(Sub-Header)")
st.write("Chaitanya Purkar(Text)")
st.markdown("Chaitanya Purkar(Markdown)")
st.caption("Chaitanya Purkar(Caption)")

# st.image("xyz.jpg")
# st.audio("speech.wav")
# st.video("abc.mkv")

st.checkbox('checkbox')
st.button('Click button')
st.radio('Pick your city',['Pune','Mumbai','delhi','surat'])
st.selectbox('Pick your city',['Pune','Mumbai','delhi','surat'])
st.multiselect('Pick favourite sports',['cricket', 'football', 'basketball'])
st.select_slider('Give a Remark', ['Bad', 'Good', 'Excellent'])
st.slider('Your Marks', 0,100)

on = st.toggle("Activate feature")
if on:
    st.write("Feature activated!")

number = st.number_input("Insert a number")
st.write("The current number is ", number)

d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)

t = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", t)

st.number_input('Enter your marks', 0,100)
st.text_input('Enter Text')
st.date_input('Exam date')
st.time_input('Exam time')
st.text_area('Description')
st.file_uploader('Upload File')
st.color_picker('Choose a color')

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("Chaitanya Purkar")
# st.sidebar.image("xyz.jpg")

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)


df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)
st.table(df)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    
    

with st.status("Step 1"):
    st.write("Step 2")
    time.sleep(1)
    st.write("Step 3")
    time.sleep(1)
    st.write("Step 4")
    time.sleep(1)
st.button("Rerun")


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

df = pd.DataFrame({
    "lat" : [123],
    "lon" : [456]
})
st.map(df)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data)

with st.chat_message("user"):
    st.write("Hello ji")





