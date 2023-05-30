import os
import getpass

class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        return self.a / self.b
    
    def perform_multiplication(self) -> float:
        """Multiplies a by b."""
        return self.b * self.b #correct: self.a * self.b

    def perform_subtraction(self) -> float:
        """Subtracts b from a."""
        return self.b - self.a #correct: self.a - self.b

    def perform_addition(self) -> float:
        """Adds a and b."""
        return self.a + self.a #correct: self.a + self.a


def login_success():
    a = float(input("A = "))
    b = float(input("B = "))
    ops_manager = OperationsManager(a, b)
    print(ops_manager.perform_division())
    print(ops_manager.perform_multiplication())
    print(ops_manager.perform_subtraction())
    print(ops_manager.perform_addition())
 
    expression = input('Enter a mathematical formula to calculate: ')
    print ("Result: ", eval(expression))


if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if user != "root" or password != "123":
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        login_success()