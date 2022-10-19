number1 = input("Enter whole number : ")
number2 = input("Enter decimal number : ")

# I think this code will specify the first number inputted will be an integer with no decimal points
#I think the second number that is inputted will have to be a float (have a decimal point)
# The round function will round the integer to the nearest decimal point.
int_num = int(number1)
float_num = float(number2)
round_num = int(round(float_num))

print(int_num, float_num, round_num)