from tkinter import Tk, Canvas
from dices import Dices
from helpbutton import HelpButton, TourGuide
from rollbutton import RollButton
from score import Score
from selection import Selection
from supportbutton import SupportButton
from themebutton import ThemeButton
import webbrowser

class ChuckALuck:
    def __init__(self):
        # Initialize the window
        self.window = Tk()
        self.window.title("Chuck a Luck")
        self.window.geometry("500x650")
        self.window.resizable(False, False)

        # Initialize a canvas
        self.canvas = Canvas(self.window, bg="#FFFFFF", width=500, height=650, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        # Create the subcomponents
        self.dices = Dices(self.canvas)
        self.score = Score(self.canvas)
        self.selection = Selection(self.canvas)
        self.rollbutton = RollButton(self.canvas, self.roll)
        self.supportbutton = SupportButton(self.canvas, self.open_support)
        self.themebutton = ThemeButton(self.canvas, self.change_theme)
        self.helpbutton = HelpButton(self.canvas, self.tour_guide)

        # Start the mainloop
        self.window.mainloop()

    def tour_guide(self, event):
        TourGuide(self.canvas, self.themebutton.mode)

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

    def open_support(self, event):
        # Open the github page
        webbrowser.open("https://github.com/DKolter/chuck_a_luck")

if __name__ == "__main__":
    ChuckALuck()

