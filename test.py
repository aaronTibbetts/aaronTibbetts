print("This is my calc,(it is short for calculator),in Python!")

try: 
    number_one = input("Please enter a whole number: ")
    number_one = int(number_one)

except ValueError:
    print("You did not enter a whole number!")

try:
    number_two = input("Please enter a second whole number: ")
    number_two = int(number_two)
except ValueError:
    print("You did not enter a whole number!")

print("What would you like to do with these numbers ? + , - , / or * ?")
operation = input()

match operation:
    case "+":
        output = number_one + number_two
        print(output)
    case "-":
        output = number_one - number_two
        print(output)
    case "/":
        try:
            output = number_one / number_two
            if output.is_integer():
                output = int(output)
            else:
                output = round(output, 5)
            print(output)
        except ZeroDivisionError:
            print("Undefined, can't divde by 0")           
    case "*":
        output = number_two * number_two
        print(output)
    case _:
        print ("You did not input a valid operation!")
