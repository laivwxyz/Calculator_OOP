# Creating a class named UserInterface
class UserInterface:
    # Display mathematical operation
    def operation(self):
        print("Calculator")
        print("Choose one mathemathical operation: ")
        print("1 : Addition")
        print("2 : Subtraction")
        print("3 : Multiplication ")
        print("4 : Division")
        
    def input_number(self):
        # Ask user to input a number
        while True:
            try:
                num = float(input("Input a number: "))
                return num
            except ValueError as error:
                print()
                print(f"Error: {error}")
                continue

    def answer(self, answer):
        # Print result
        print("Result " + str(answer))
