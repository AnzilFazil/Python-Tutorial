class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)

    def display(self):
        print(f"{self.real} + {self.imag}i")

# Create two complex number objects
c1 = Complex(3, 4)
c2 = Complex(2, 5)
c3 = c1 + c2

print("First complex number:")
c1.display()

print("Second complex number:")
c2.display()

print("Sum of complex numbers:")
c3.display()
