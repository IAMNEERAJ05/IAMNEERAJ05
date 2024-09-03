import streamlit as st 
import base64

st.markdown("## code to set image as background")

st.code("""
        import streamlit as st
import base64
# Function to set Image as Background
def add_local_backgound_image_(image):
 with open(image, "rb") as image:
 encoded_string = base64.b64encode(image.read())
 st.write("Image Courtesy: unplash")
 st.markdown(
 f""
 <style>
 .stApp {{
 background-image: url(data:files/
{"jpg"};base64,{encoded_string.decode()});
 background-size: cover
 }}
 </style>
 "",
 unsafe_allow_html=True
 )
st.write("Background Image")
# Calling Image in function
add_local_backgound_image_('files/animal7.jpg')
""", language='python')
#function to set image as background
def add_local_bimage(image):
    with open(image,'rb') as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image from local")
    st.markdown(
        f"""
        <style>
        .stApp{{
            background-image : url(data:image/jpg;base64,{encoded_string.decode()});
            background-size :cover
        }}
        </style>
""", unsafe_allow_html=True
    )
st.write("Background image")
st.image(r"C:\Users\seera\OneDrive\Desktop\wallpapers\plan.jpg")

add_local_bimage(r"C:\Users\seera\OneDrive\Desktop\wallpapers\plan.jpg")