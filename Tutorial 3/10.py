from breezypythongui import EasyFrame

class BouncyBallCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Bouncy Ball Distance Calculator")

        self.addLabel("Initial Height (meters):", row=0, column=0)
        self.heightField = self.addFloatField(0.0, row=0, column=1)

        self.addLabel("Bounciness Index (0-1):", row=1, column=0)
        self.bounceField = self.addFloatField(0.0, row=1, column=1)

        self.addLabel("Number of Bounces:", row=2, column=0)
        self.bouncesField = self.addIntegerField(0, row=2, column=1)

        self.addButton("Compute", row=3, column=0, columnspan=2, command=self.computeDistance)

        self.addLabel("Total Distance Traveled (meters):", row=4, column=0)
        self.resultField = self.addFloatField(0.0, row=4, column=1, state="readonly")

    def computeDistance(self):
        """Calculate and display the total distance traveled by the bouncing ball."""
        try:
            height = self.heightField.getNumber()
            bounce_index = self.bounceField.getNumber()
            bounces = self.bouncesField.getNumber()

            if height <= 0 or not (0 < bounce_index < 1) or bounces < 0:
                raise ValueError("Invalid input values!")

            total_distance = height 
            for _ in range(bounces):
                height *= bounce_index  
                total_distance += 2 * height  

            self.resultField.setNumber(total_distance)

        except ValueError:
            self.messageBox("Error", "Please enter valid positive values!")


if __name__ == "__main__":
    BouncyBallCalculator().mainloop()
