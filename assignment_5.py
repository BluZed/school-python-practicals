print("=====================================")
print("   Program to check if a number is   ")
print("    divisible by another number      ")
print("=====================================")

def get_valid_integer(input_text):
    raw_input = input(input_text)
    if(raw_input.isdigit()):
        return int(raw_input)
    else:
        print("Invalid input provided! Please provide a valid integer.")
        quit()

dividend = get_valid_integer("Enter the dividend -> ")
divisor = get_valid_integer("Enter the divisor -> ")

if(divisor%dividend==0):
    print("{} is divisible by {}".format(divisor, dividend))
else:
    print("{} is not divisible by {}".format(divisor, dividend))