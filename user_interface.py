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

    def choose_operation(self):
        # Ask user to choose a math operation
        operation = input("Enter Operation (1-4): ")
        return operation
    
    def try_again(self):
        # Ask the user if they want to try again
        while True:
            try_again = input("Do you want to try again? (y/n): ")
            print()
            # if user enter n, it's means the program will end
            if try_again.lower() == 'n':
                print("Thank you!")
                return False
            # if user enter y, it's means the program will continue
            elif try_again.lower() == 'y':
                return True
            # if user enter a letter that is not a y/n, an error may occur
            else:
                print("Error: Invalid input")
                continue