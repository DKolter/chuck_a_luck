from PIL import Image, ImageTk
from utils import load_asset

class ThemeButton:
    # Mode
    LIGHT = 0
    DARK = 1

    def __init__(self, canvas, func):
        # Store the canvas and the function
        self.canvas = canvas
        self.func = func

        # Translator from mode to image
        self.translator = {
            ThemeButton.LIGHT: load_asset("themelight.png"),
            ThemeButton.DARK: load_asset("themedark.png")
        }

        # Set initial value of mode
        self.mode = ThemeButton.LIGHT

        # Create the label and bind the click event
        self.label = canvas.create_image(450, 565, image=self.translator[ThemeButton.LIGHT])
        canvas.tag_bind(self.label, "<Button-1>", self.invert)

    def invert(self, event):
        # Invert the mode and config the label
        self.mode = not self.mode
        self.canvas.itemconfig(self.label, image=self.translator[self.mode])

        # Notify the function
        self.func(self.mode)