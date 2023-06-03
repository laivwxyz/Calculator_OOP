# Adding a design in the program 
from termcolor import colored
from pyfiglet import Figlet

f = Figlet(font = 'isometric3', width = 240)
print(colored(f.renderText(' CALCULATOR'), 'cyan'))
print(colored('=' * 169, 'cyan'))
f = Figlet(font = 'serifcap',  width = 240)
print(colored(f.renderText('Choose one mathematical operation'), 'light_green'))
f = Figlet(font = 'serifcap', width = 240)
print(colored(f.renderText(' ' * 30 + '+ - x /'),'light_green'))

# Creating a class named UserInterface
class UserInterface:
    # Display mathematical operation
    def operation(self):
        print(" " * 35, "\033[93m 1. \033[0mAddition", " " * 45, "\033[91m 3. \033[0mMultiplication \n", 
        " " * 34, "\033[94m 2. \033[0mSubtraction"," " * 42, "\033[95m 4. \033[0mDivision \n", 
        " " * 34, "\033[91m 5. \033[0mModulus"," " * 46, "\033[92m 6. \033[0mExponent")
        print()

    def input_number(self):
        # Ask user to input a number
        while True:
            try:
                num = float(input("\033[92mInput a number: \033[0m"))
                return num
            except ValueError as error:
                print()
                print(f"\033[91mError: \033[0m{error}")
                print()
                continue

    def answer(self, answer):
        # Print result
        print()
        print("\033[93mResult: " + "\033[0m",str(answer))

    def choose_operation(self):
        # Ask user to choose a math operation
        operation = input("\033[92mEnter Operation (1-4): \033[0m")
        return operation
    
    def try_again(self):
        # Ask the user if they want to try again
        while True:
            print()
            try_again = input("\033[92mDo you want to try again? (y/n): \033[0m")
            print()
            # if user enter n, it's means the program will end
            if try_again.lower() == 'n':
                print("\033[96mThank you!")
                print(colored('=' * 171, 'cyan'))
                return False
            # if user enter y, it's means the program will continue
            elif try_again.lower() == 'y':
                return True
            # if user enter a letter that is not a y/n, an error may occur
            else:
                print("\033[91mError: \033[0mInvalid input!")
                continue