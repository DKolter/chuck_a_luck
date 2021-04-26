from PIL import Image, ImageTk
from rounded_rect import rounded_rectangle

class Selection:
    def __init__(self, canvas):
        # Store the canvas
        self.canvas = canvas

        # Dictionary to translate integers to image
        self.translator = {
            1: ImageTk.PhotoImage(Image.open("assets/1.png").resize((50, 50))), 
            2: ImageTk.PhotoImage(Image.open("assets/2.png").resize((50, 50))), 
            3: ImageTk.PhotoImage(Image.open("assets/3.png").resize((50, 50))), 
            4: ImageTk.PhotoImage(Image.open("assets/4.png").resize((50, 50))), 
            5: ImageTk.PhotoImage(Image.open("assets/5.png").resize((50, 50))), 
            6: ImageTk.PhotoImage(Image.open("assets/6.png").resize((50, 50)))
        }

        # Create the image labels
        self.dice_labels = [
            canvas.create_image(110, 400, image=self.translator[1]),
            canvas.create_image(166, 400, image=self.translator[2]), 
            canvas.create_image(222, 400, image=self.translator[3]), 
            canvas.create_image(278, 400, image=self.translator[4]), 
            canvas.create_image(334, 400, image=self.translator[5]), 
            canvas.create_image(390, 400, image=self.translator[6])
        ]

        # Create the selection polygons
        self.selection_labels = [
            rounded_rectangle(canvas, 85, 375, 135, 425, 20, fill="", width=2, outline="#BB86FC"),
            rounded_rectangle(canvas, 141, 375, 191, 425, 20, fill="", width=2),
            rounded_rectangle(canvas, 197, 375, 247, 425, 20, fill="", width=2),
            rounded_rectangle(canvas, 253, 375, 303, 425, 20, fill="", width=2),
            rounded_rectangle(canvas, 309, 375, 359, 425, 20, fill="", width=2),
            rounded_rectangle(canvas, 365, 375, 415, 425, 20, fill="", width=2),
        ]

        # Set inital value of selection
        self.selection = 0

        # Bind the click events
        canvas.tag_bind(self.selection_labels[0], "<Button-1>", lambda x: self.select(0))
        canvas.tag_bind(self.selection_labels[1], "<Button-1>", lambda x: self.select(1))
        canvas.tag_bind(self.selection_labels[2], "<Button-1>", lambda x: self.select(2))
        canvas.tag_bind(self.selection_labels[3], "<Button-1>", lambda x: self.select(3))
        canvas.tag_bind(self.selection_labels[4], "<Button-1>", lambda x: self.select(4))
        canvas.tag_bind(self.selection_labels[5], "<Button-1>", lambda x: self.select(5))

    def select(self, selection):
        # Store selection and config outline
        self.canvas.itemconfig(self.selection_labels[self.selection], outline="")
        self.canvas.itemconfig(self.selection_labels[selection], outline="#BB86FC")
        self.selection = selection

    def get(self):
        # Transform index to dice value
        return self.selection + 1