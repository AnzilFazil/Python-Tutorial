from breezypythongui import EasyFrame

class ComputerGuessGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Computer Guess the Number")

        self.low = 1
        self.high = 100
        self.computer_guess = (self.low + self.high) // 2
        self.game_over = False

        self.addLabel("Computer's Guess:", row=0, column=0)
        self.guessLabel = self.addLabel(str(self.computer_guess), row=0, column=1)

        self.tooSmallBtn = self.addButton("Too Small", row=1, column=0, command=self.tooSmall)
        self.tooLargeBtn = self.addButton("Too Large", row=1, column=1, command=self.tooLarge)
        self.correctBtn = self.addButton("Correct!", row=1, column=2, command=self.correctGuess)

        self.newGameBtn = self.addButton("New Game", row=2, column=0, columnspan=3, command=self.newGame)
        self.newGameBtn["state"] = "disabled"

    def tooSmall(self):
        """Adjust the range and make a new guess if the guess was too small."""
        if not self.game_over:
            self.low = self.computer_guess + 1
            self.makeGuess()

    def tooLarge(self):
        """Adjust the range and make a new guess if the guess was too large."""
        if not self.game_over:
            self.high = self.computer_guess - 1
            self.makeGuess()

    def makeGuess(self):
        """Make a new guess based on updated range."""
        if self.low > self.high:
            self.guessLabel["text"] = "Something went wrong!"
        else:
            self.computer_guess = (self.low + self.high) // 2
            self.guessLabel["text"] = str(self.computer_guess)

    def correctGuess(self):
        """End the game when the user confirms the guess is correct."""
        self.guessLabel["text"] = f"Yay! I guessed it!"
        self.disableButtons()

    def disableButtons(self):
        """Disable the buttons after the game ends."""
        self.game_over = True
        self.tooSmallBtn["state"] = "disabled"
        self.tooLargeBtn["state"] = "disabled"
        self.correctBtn["state"] = "disabled"
        self.newGameBtn["state"] = "normal"

    def newGame(self):
        """Reset the game to start over."""
        self.low = 1
        self.high = 100
        self.computer_guess = (self.low + self.high) // 2
        self.game_over = False
        self.guessLabel["text"] = str(self.computer_guess)

        self.tooSmallBtn["state"] = "normal"
        self.tooLargeBtn["state"] = "normal"
        self.correctBtn["state"] = "normal"
        self.newGameBtn["state"] = "disabled"

if __name__ == "__main__":
    ComputerGuessGame().mainloop()
