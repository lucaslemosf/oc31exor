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

    # In case resize is empty, return the same image
    if not resize:
        return X

    image = Image.fromarray(np.uint8(X))
    image = image.resize(resize)

    return image
