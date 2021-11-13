import numpy as np
from ipywidgets import interact, fixed
from PIL import Image


def imshow(X, resize=None):
    """
    You should create a way to resize an image from an array X.
    The use of widgets is optional but you can take a look to interact.
    We should be able to install this package in Google Colab from your Git
    repo.
    """
    # Convert array to image
    image = Image.fromarray(np.uint8(X))

    # In case resize is not empty, resize
    if resize:
        image = image.resize(resize)
    
    return image

