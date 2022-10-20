temperature = 40
if (temperature > 30):
    print("Too hot")
    print("aagh")
    if (temperature > 50):
        print("AAH")
print("Too cold")

# You dont get a chance to enter in a number firstly because there is no input line
their are 2 print values after the first if statement.
The second if statement is not indented properly and the indentation is inconsistent on the last two lines. The last line needs to be indented.

temperature = 10
if (temperature > 30):
    print("Too hot")
    print("aagh")
if (temperature < 0):
    print("Too cold")
if (temperature > 0):
    print("perfect")

If we set the temperature to 20 then it will print perfect
If we set the temp to 40 it will priint too hot aagh
If we set temp to -10 it should throw an error because there is no else specified in this block of code

temperature = 40
if (temperature > 30):
    print("Too hot")
    print("aagh")
if (temperature < 0):
    print("Too cold")
else:
    print("perfect")

The else specifies all unspecified conditions and sets it False for example. It can save you writing many if statements.


temperature = 10
if (temperature > 30):
    print("Too hot")
elif (temperature < 15):
    print("Too cold")
else:
    print("perfect")

# Its more precise and clear to instruct the program and for the reader of your code. Many if statements look messy and it is not good practice.
# Its more clear and specific using the elif that 2 ifs and an else.
