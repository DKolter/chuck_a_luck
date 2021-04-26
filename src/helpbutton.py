from utils import load_asset, rounded_rectangle
from themebutton import ThemeButton

class HelpButton:
    def __init__(self, canvas, func):
        # Load the images
        self.normal = load_asset("helpnormal.png")
        self.hovered = load_asset("helphovered.png")

        # Create the label and bind the click event to func
        self.label = canvas.create_image(100, 610, image=self.normal, activeimage=self.hovered)
        canvas.tag_bind(self.label, "<Button-1>", func)

class TourGuide:
    def __init__(self, canvas, theme):
        # Store the canvas
        self.canvas = canvas

        # Check if the theme is light
        if theme == ThemeButton.LIGHT:
            self.outline_color = "black"
            self.hide_color = "white"
            self.text_color = "black"
            self.stipple = "gray50"

        # Check if the theme is dark
        if theme == ThemeButton.DARK:
            self.outline_color = "white"
            self.hide_color = "black"
            self.text_color = "white"
            self.stipple = "gray75"

        # Rounded rect around the dices
        self.region = rounded_rectangle(self.canvas, 65, 20, 435, 180, 20, outline=self.outline_color, fill="", width=3, tag="continue")

        # Create the hiding areas
        self.hides = [
            canvas.create_rectangle(0, 0, 62, 650, fill=self.hide_color, stipple=self.stipple, width=0, tag="continue"),
            canvas.create_rectangle(438, 0, 500, 650, fill=self.hide_color, stipple=self.stipple, width=0, tag="continue"),
            canvas.create_rectangle(62, 183, 438, 650, fill=self.hide_color, stipple=self.stipple, width=0, tag="continue"),
            canvas.create_rectangle(62, 0, 438, 17, fill=self.hide_color, stipple=self.stipple, width=0, tag="continue")
        ]

        # Describe the region
        self.description = canvas.create_text(250, 200, text="The dices have a purple outline if you won", font=("", 15), tag="continue", fill=self.text_color)

        # Bind the event to the tag
        canvas.tag_bind("continue", "<Button-1>", self.show_counter)

    def show_counter(self, event):
        # Destroy and recreate the region
        self.canvas.delete(self.region)
        self.region = rounded_rectangle(self.canvas, 65, 220, 435, 330, 20, outline=self.outline_color, fill="", width=3, tag="continue")

        # Adjust the hiding area
        self.canvas.coords(self.hides[3], 62, 0, 438, 217)
        self.canvas.coords(self.hides[2], 62, 333, 438, 650)

        # Adjust the description
        self.canvas.itemconfig(self.description, text="This counter shows your current score")

        # Rebind the tag
        self.canvas.tag_bind("continue", "<Button-1>", self.show_selection)

    def show_selection(self, event):
        # Destroy and recreate the region
        self.canvas.delete(self.region)
        self.region = rounded_rectangle(self.canvas, 65, 365, 435, 435, 20, outline=self.outline_color, fill="", width=3, tag="continue")

        # Adjust the hiding area
        self.canvas.coords(self.hides[3], 62, 0, 438, 362)
        self.canvas.coords(self.hides[2], 62, 438, 438, 650)

        # Adjust the description
        self.canvas.coords(self.description, 250, 345)
        self.canvas.itemconfig(self.description, text="Bet on a dice by selecting")

        # Rebind the tag
        self.canvas.tag_bind("continue", "<Button-1>", self.show_roll)

    def show_roll(self, event):
        # Destroy and recreate the region
        self.canvas.delete(self.region)
        self.region = rounded_rectangle(self.canvas, 65, 470, 435, 530, 20, outline=self.outline_color, fill="", width=3, tag="continue")

        # Adjust the hiding area
        self.canvas.coords(self.hides[3], 62, 0, 438, 467)
        self.canvas.coords(self.hides[2], 62, 533, 438, 650)

        # Adjust the description
        self.canvas.coords(self.description, 250, 450)
        self.canvas.itemconfig(self.description, text="Click to begin")

        # Rebind the tag
        self.bind = self.canvas.tag_bind("continue", "<Button-1>", self.close)

    def close(self, event):
        # Destroy all the objects
        self.canvas.delete(self.region)
        self.canvas.delete(self.description)

        # Loop over the hides and destroy them
        for obj in self.hides:
            self.canvas.delete(obj)

        # Unbind the tag
        self.canvas.tag_unbind("continue", "<Button-1>", self.bind)