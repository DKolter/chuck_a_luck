class Score:
    def __init__(self, canvas):
        # Store the canvas
        self.canvas = canvas

        # Initialize score and color
        self.score = 100
        self.fill = "black"

        # Create score label
        self.label = canvas.create_text(250, 275, text="100", font=("", 80), fill="black")

    def recalculate(self, matches):
        if matches == 0:
            # No match, minus one
            self.score -= 1
        else:
            # Multiple matches
            self.score += matches

        # Update the label
        self.canvas.itemconfig(self.label, text=str(self.score))

        # Adjust the text color
        if self.score < 0:
            self.canvas.itemconfig(self.label, fill="#CF6679")
        else:
            self.canvas.itemconfig(self.label, fill=self.fill)

    def set_fill(self, fill):
        # Store the fill color
        self.fill = fill

        # Adjust the text color
        if self.score < 0:
            self.canvas.itemconfig(self.label, fill="#CF6679")
        else:
            self.canvas.itemconfig(self.label, fill=self.fill)
