class Expression:
    def __init__(self, num1, num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add_num(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {result}")

e1 = Expression(5, 10, 15)
e2 = Expression(20, 30, 40)

e1.add_num()
e2.add_num()