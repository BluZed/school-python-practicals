print("=====================================")
print("   Program to print the table of     ")
print("             any number              ")
print("=====================================")

def get_valid_integer(input_text):
    raw_input = input(input_text)
    if(raw_input.isdigit()):
        return int(raw_input)
    else:
        print("Invalid input provided! Please provide a valid integer.")
        quit()

number = get_valid_integer("Enter the number you want the table of -> ")

for x in range(11):
    print("{} x {} = {}".format(number, x, number*x))