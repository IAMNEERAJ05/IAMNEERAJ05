import streamlit as st 

st.write("Displaying an Image")

st.image(r'C:\Users\seera\OneDrive\Desktop\wallpapers\luffy_smile.jpg')
st.markdown("## code:")
st.code("""
st.image("file_path.jpg")
""", language='python')
st.markdown("## code for multiple images: ")
st.code("""
animal_images = [
 'files/animal1.jpg',
 'files/animal2.jpg',
 'files/animal3.jpg',
 'files/animal4.jpg',
Chapter 4 Data and Media Elements
85
 'files/animal5.jpg', 'files/animal6.jpg',
 'files/animal7.jpg',
 'files/animal8.jpg',
 'files/animal9.jpg',
 'files/animal10.jpg'
]
# Displaying Multiple images with width 150
st.image(animal_images, width=150)""",language="python")
st.write("sample output:")
st.image(r"D:\sample_multi.png")