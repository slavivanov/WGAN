import numpy as np, matplotlib.pyplot as plt
from PIL import Image
from IPython.display import display, Audio

# Print any variable that is on its own line
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def to_plot(img):
    return np.rollaxis(img, 0, 3).astype(np.uint8)
def plot(img):
    plt.imshow(to_plot(img))

def plot_multi(im, dim=(4,4), figsize=(10,10), **kwargs ):
    plt.figure(figsize=figsize)
    for i,img in enumerate(im):
        plt.subplot(*dim, i+1)
        plt.imshow(img, **kwargs)
        plt.axis('off')
    plt.tight_layout()
