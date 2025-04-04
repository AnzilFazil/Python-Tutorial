from breezypythongui import EasyFrame

class UppercaseConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Uppercase Converter")

        self.addLabel(text="Enter text:", row=0, column=0)
        self.inputField = self.addTextField(text="", row=0, column=1, width=30)

        self.addButton(text="Convert", row=1, column=0, columnspan=2, command=self.convertToUpper)

        self.addLabel(text="Uppercase:", row=2, column=0)
        self.outputField = self.addTextField(text="", row=2, column=1, width=30, state="readonly")

    def convertToUpper(self):
        """Convert input text to uppercase and display the result."""
        text = self.inputField.getText()
        uppercase_text = text.upper()
        self.outputField.setText(uppercase_text)

if __name__ == "__main__":
    UppercaseConverter().mainloop()
