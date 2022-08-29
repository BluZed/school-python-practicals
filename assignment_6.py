print("=====================================")
print("   Program to find out the grade of  ")
print("             a student               ")
print("=====================================")

def get_valid_integer(input_text):
    raw_input = input(input_text)
    if(raw_input.isdigit()):
        return int(raw_input)
    else:
        print("Invalid input provided! Please provide a valid integer.")
        quit()

def return_grade(grade):
    print("You got Grade {}!".format(grade))

marks = get_valid_integer("Enter your marks -> ")

if(marks >= 90):
    return_grade("A")
elif(marks >= 75):
    return_grade("B")
elif(marks >= 60):
    return_grade("C")
elif(marks >= 45):
    return_grade("D")
elif(marks >= 0):
    print("Too less Marks :(")
else:
    print("Invalid Marks!")