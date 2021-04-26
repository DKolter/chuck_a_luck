from PIL import Image, ImageTk
from utils import rounded_rectangle, load_asset
import random

class Dices:
    def __init__(self, canvas):
        # Store the canvas
        self.canvas = canvas
        
        # Dictionary to translate integers to image
        self.translator = {
            1: load_asset("1.png", (100, 100)), 
            2: load_asset("2.png", (100, 100)), 
            3: load_asset("3.png", (100, 100)), 
            4: load_asset("4.png", (100, 100)), 
            5: load_asset("5.png", (100, 100)), 
            6: load_asset("6.png", (100, 100))
        }

	    # Create the image labels
        self.label_dice1 = canvas.create_image(130, 125, image=self.translator[1])
        self.label_dice2 = canvas.create_image(250, 75, image=self.translator[1])
        self.label_dice3 = canvas.create_image(370, 125, image=self.translator[1])

        # Create the matching polygons
        self.match_dice1 = rounded_rectangle(canvas, 80, 75, 180, 175, 30, fill="", width=3)
        self.match_dice2 = rounded_rectangle(canvas, 200, 25, 300, 125, 30, fill="", width=3)
        self.match_dice3 = rounded_rectangle(canvas, 320, 75, 420, 175, 30, fill="", width=3)
        
        # Set initial value of the dices
        self.value_dice1 = 1
        self.value_dice2 = 1
        self.value_dice3 = 1

    def roll(self):
    	# Create three random dice values
        self.value_dice1 = random.randint(1, 6)
        self.value_dice2 = random.randint(1, 6)
        self.value_dice3 = random.randint(1, 6)
        
        # Attach the correct image to the labels
        self.canvas.itemconfig(self.label_dice1, image=self.translator[self.value_dice1])
        self.canvas.itemconfig(self.label_dice2, image=self.translator[self.value_dice2])
        self.canvas.itemconfig(self.label_dice3, image=self.translator[self.value_dice3])

    def matches(self, selection):
        # Reset outlines
        self.canvas.itemconfig(self.match_dice1, outline="")
        self.canvas.itemconfig(self.match_dice2, outline="")
        self.canvas.itemconfig(self.match_dice3, outline="")

        # Initialize match counter
        matches = 0

        # Check if the first dice matches
        if self.value_dice1 == selection:
            self.canvas.itemconfig(self.match_dice1, outline="#BB86FC")
            matches += 1

        # Check if the second dice matches
        if self.value_dice2 == selection:
            self.canvas.itemconfig(self.match_dice2, outline="#BB86FC")
            matches += 1

        # Check if the third dice matches
        if self.value_dice3 == selection:
            self.canvas.itemconfig(self.match_dice3, outline="#BB86FC")
            matches += 1

        return matches