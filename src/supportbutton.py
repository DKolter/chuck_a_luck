from PIL import Image, ImageTk
from utils import load_asset

class SupportButton:
    def __init__(self, canvas, func):
        # Load the images
        self.normal = load_asset("supportnormal.png")
        self.hovered = load_asset("supporthovered.png")

        # Create the label and bind the click event to func
        self.label = canvas.create_image(40, 560, image=self.normal, activeimage=self.hovered)
        canvas.tag_bind(self.label, "<Button-1>", func)