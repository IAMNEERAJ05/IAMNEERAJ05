import streamlit as st 
st.metric(label="Temperature", value='23 C', delta='1.2 C')
# defining columns 
c1, c2, c3 = st.columns(3)
 
 #definninf metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric("Population", value="123 Billion", delta = '-1 Billion')
c3.metric("Customers", value=100,delta=10, delta_color="off")

st.metric("speed", value=None,delta=0)
st.metric("Trees", "91456", "1132648")

st.markdown("# displaying json data")

st.json(
    {
        "Books":
        [{
"BookName" : "Python Testing with Selenium",
"BookID" : "1",
"Publisher" : "Apress",
"Year" : "2021",
"Edition" : "First",
"Language" : "Python",
},
{
"BookName": "Beginners Guide to Streamlit with Python",
"BookID" : "2",
"Publisher" : "Apress",
"Year" : "2022",
"Edition" : "First",
"Language" : "Python"
}]
    }
)