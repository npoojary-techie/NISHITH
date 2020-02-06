class Add:
    num1 = 1  # First number
    num2 = 2  # Second number

    def __init__(self):

        # Initialisation
        self.num1 = 5
        self.num2 = 10

    def calculate(self):

        # Calculation
        print("number1=", self.num1)
        print("number2=", self.num2)

        init_sum = (self.num1+self.num2)
        print("sum is", init_sum)

        print("Number1=", Add.num1)
        print("Number2=", Add.num2)
        class_sum = Add.num1 + Add.num2
        print("sum is ", class_sum)


# Function calls
a1 = Add()
a1.calculate()
