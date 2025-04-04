from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")

        self.addLabel("Fahrenheit:", row=0, column=0)
        self.fahrenheitField = self.addFloatField(32.0, row=1, column=0)

        self.addLabel("Celsius:", row=0, column=1)
        self.celsiusField = self.addFloatField(0.0, row=1, column=1)

        self.addButton(">>>>", row=2, column=0, command=self.fToC)
        self.addButton("<<<<", row=2, column=1, command=self.cToF)

    def fToC(self):
        """Convert Fahrenheit to Celsius."""
        f = self.fahrenheitField.getNumber()
        c = (f - 32) * 5 / 9
        self.celsiusField.setNumber(c)

    def cToF(self):
        """Convert Celsius to Fahrenheit."""
        c = self.celsiusField.getNumber()
        f = (c * 9 / 5) + 32
        self.fahrenheitField.setNumber(f)

if __name__ == "__main__":
    TemperatureConverter().mainloop()
