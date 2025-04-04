from breezypythongui import EasyFrame
import random

class GuessTheNumberGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Guess the Number")

        self.secretNumber = random.randint(1, 100)
        self.numGuesses = 0

      
        self.addLabel("Enter a number (1-100):", row=0, column=0)
        self.inputField = self.addIntegerField(0, row=0, column=1)

        self.addButton("Guess", row=1, column=0, columnspan=2, command=self.checkGuess)

        self.resultLabel = self.addLabel("", row=2, column=0, columnspan=2)

    def checkGuess(self):
        """Check the user's guess and give feedback."""
        try:
            guess = self.inputField.getNumber()
            if guess < 1 or guess > 100:
                raise ValueError("Out of range")

            self.numGuesses += 1

            if guess < self.secretNumber:
                self.resultLabel["text"] = "Too small, try again."
            elif guess > self.secretNumber:
                self.resultLabel["text"] = "Too large, try again."
            else:
                self.resultLabel["text"] = f"Congratulations! You guessed it in {self.numGuesses} tries."
        except ValueError:
            self.messageBox("Error", "Please enter a valid number between 1 and 100.")

if __name__ == "__main__":
    GuessTheNumberGame().mainloop()
