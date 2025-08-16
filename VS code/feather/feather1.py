import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from PIL import Image
import requests
from io import BytesIO



def load_image_from_url(url):
    response=requests.get(url)
    return Image.open(BytesIO(response.content))


peacock_feather_url ="https://m.media-amazon.com/images/I/81JSw5mE54L._UF894,1000_QL80_.jpg"
peacock_feather = load_image_from_url(peacock_feather_url)


## display 
plt.figure(figsize=(6,4))
plt.imshow(peacock_feather)
plt.title('Feather')
plt.axis('off')
plt.show()

# image to array
peacock_feather_np = np.array(peacock_feather)
print('Elephant Image Shape',feather_np.shape)