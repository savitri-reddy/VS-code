import numpy as np                   # numpy for --> ND Array
import pandas as pd                  # pandas for --> DF
import matplotlib.pyplot as plt      # matplotlib--> for visualization   
from PIL import Image                # PIL for--> python imageing library
import requests                      # request from url, request --> is a library
from io import BytesIO               # Bytes for --> bufferd I/O implementation using an in-memory bytes buffer
                                    # Bytes io, used for buffer memory to store/capture images

# i am gonna create a helper fun
def load_image_from_url(url):     # iam create a fun (and i passed url)
    response = requests.get(url)    # i am craete a variable(response)
    return Image.open(BytesIO(response.content))    # return with those functions   # open() is a fun

# i create 1 url, iwant to go goolend search image url  --> a beatiful peacock a feather images.jpg 
elephant_url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"
elephant = load_image_from_url(elephant_url)


# display original image
plt.figure(figsize=(6,4))       # here , increase only dimension when u increase figsize=(100,100)
plt.imshow(elephant)
plt.title('Elephant')
plt.axis('off')
plt.show()



