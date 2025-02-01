class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imaginary_diff = self.imaginary - other.imaginary
        return ComplexNumber(real_diff, imaginary_diff)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = ComplexNumber(54, 34)
c2 = ComplexNumber(3, 64)

sum = c1 + c2
print(f"Sum: {sum}")

diff = c1 - c2
print(f"Difference: {diff}")