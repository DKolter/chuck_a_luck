from PIL import Image, ImageTk
from utils import load_asset

class RollButton:
    def __init__(self, canvas, func):
        # Load the images
        self.normal = load_asset("rollnormal.png")
        self.hovered = load_asset("rollhovered.png")

        # Create the label and bind the click event to func
        self.label = canvas.create_image(250, 500, image=self.normal, activeimage=self.hovered)
        canvas.tag_bind(self.label, "<Button-1>", func)