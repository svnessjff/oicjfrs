import streamlit as st
from PIL import Image
from exif import Image

image = Image.open('cat.jpeg')
st.image(image, caption='Cute cat')
exif_data = image._getexif()
image.list_all()