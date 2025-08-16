import streamlit as st
import numpy as np                   # numpy for --> ND Array
import pandas as pd                  # pandas for --> DF
import matplotlib.pyplot as plt      # matplotlib--> for visualization   
from PIL import Image                # PIL for--> python imageing library
import requests                      # request from url, request --> is a library
from io import BytesIO               # Bytes for --> bufferd I/O implementation using an in-memory bytes buffer

# set streamlit page config
st.set_page_config(page_title = 'My Image Processor', layout = 'wide')

# Title
st.title('My Image - Multi Color Channel Visualizer')

# {{{{ load image from URL
#@st.cache_data              # @ --> is PYTHON Decorator 
#def load_image():
 #   url = "C:\Users\Hanshu\Desktop\3pics.jpg"
  #  response = requests.get(url)
   # return Image.open(BytesIO(response.content)).convert('RGB')  }}}}}


# Load image from local path
@st.cache_data
def load_image():
    path = r"C:\Users\Hanshu\Desktop\3pics.jpg"
    return Image.open(path).convert("RGB")


# load and diplay image
myimage = load_image()
st.image(myimage, caption="Original My Image", use_container_width = True)


# convert numpy to array
myimage_np = np.array(myimage)
R ,G , B = myimage_np[:, :, 0], myimage_np[:, :, 1], myimage_np[:, :, 2]    # here create list


# create a channel images
red_img = np.zeros_like(myimage_np)
green_img = np.zeros_like(myimage_np)
blue_img = np.zeros_like(myimage_np)


red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

myimage_gray = myimage.convert("L")
myimage_gray_np = np.array(myimage_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(6, 4))
ax.imshow(myimage_gray_np, cmap=colormap)
ax.axis("off")
st.pyplot(fig)

    
    
    