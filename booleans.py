number1 = float(input("Enter first number : "))
number2 = float(input("Enter second number : "))

#This is an if statement. 
# This means if the number1 variable is bigger/greater than number2 variable
# Print a statement which states which number entered by the user is bigger/smaller using True or false.
if number1 > number2:
    number1bigger = True
else:
    number1bigger = False


#Print out the result depending on which one is bigger
print("It is ", number1bigger, "that number 1 is bigger")