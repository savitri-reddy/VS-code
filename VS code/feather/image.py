import numpy as np
import pandas as pd
import PIL import Image
import requests
from io import BytesIO


def load_image_from url(url):
    response=requests.get(url)
    return Image.open(BytesIO(response.content))

elephant_url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"
elephent = load_image_from_url(elephant_url )


## display 
plt.figure(figuresize=(6,4))
plt.imshow(elephant)
plt.image('Elephant')
plt.axisp('off')
plt.show()