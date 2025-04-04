from breezypythongui import EasyFrame
import math

class SquareRootCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Square Root Calculator")

        self.addLabel("Enter an integer:", row=0, column=0)
        self.inputField = self.addIntegerField(0, row=0, column=1)

        self.addButton("Compute", row=1, column=0, columnspan=2, command=self.computeSqrt)

        self.addLabel("Square Root:", row=2, column=0)
        self.outputField = self.addFloatField(0.0, row=2, column=1, state="readonly")

    def computeSqrt(self):
        """Compute and display the square root, handling errors."""
        try:
            num = self.inputField.getNumber()
            if num < 0:
                raise ValueError("Cannot compute square root of a negative number.")
            result = math.sqrt(num)
            self.outputField.setNumber(result)
        except ValueError:
            self.messageBox("Error", "Please enter a valid non-negative integer.")

if __name__ == "__main__":
    SquareRootCalculator().mainloop()
