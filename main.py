from tkinter import Tk, Canvas
from dices import Dices
from rollbutton import RollButton
from score import Score
from selection import Selection
from supportbutton import SupportButton
from themebutton import ThemeButton

class ChuckALuck:
    def __init__(self):
        # Initialize the window
        self.window = Tk()
        self.window.title("Chuck a Luck")
        self.window.geometry("500x600")
        self.window.resizable(False, False)

        # Initialize a canvas
        self.canvas = Canvas(self.window, bg="#FFFFFF", width=500, height=600, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        # Create the subcomponents
        self.dices = Dices(self.canvas)
        self.score = Score(self.canvas)
        self.selection = Selection(self.canvas)
        self.rollbutton = RollButton(self.canvas, self.roll)
        self.supportbutton = SupportButton(self.canvas, lambda: None)
        self.themebutton = ThemeButton(self.canvas, self.change_theme)

        # Start the mainloop
        self.window.mainloop()

    def roll(self, event):
        # Roll the dices
        self.dices.roll()

        # Show and get the matches
        matches = self.dices.matches(self.selection.get())

        # Recalculate the score
        self.score.recalculate(matches)

    def change_theme(self, mode):
        # Adjust the background
        if mode == ThemeButton.LIGHT:
            self.canvas.config(bg="#FFFFFF")
            self.score.set_fill("black")
        elif mode == ThemeButton.DARK:
            self.canvas.config(bg="#121212")
            self.score.set_fill("white")

if __name__ == "__main__":
    ChuckALuck()

