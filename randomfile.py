# var1 = 5

# #Flaw divison (//)
# #divison (/)
# # % tells us the remainder
# var2 = var1 % 2

# print(var2)

# var1 = 0
# num = int(input("Please enter a number : "))

# if num % 2 == var1:
#     print("Even")
# else: 
#     print("Odd")

# Draw.io or use whiteborard and take a screenshot
# a=5
# b=10
# c=12


#####Exercise attempt#########

# if a > b:
#     print(a)
# else:
#     print(b)

# if a > c:
#     print (c)
# else:
#     print(a)

# if b > c:
#     print(b)
# else:
#     print(c)

##Solution####
# num1 = int(input("Please enter a number : "))
# num2 = int(input("Please enter a number : "))
# num3 = int(input("Please enter a number : "))

# if num1 > num2:
#     if num1 > num3:
#         print("a is the biggest")
#     else:
#         print("c")
# else:
#     if num2 > num3:
#         print("b")
#     else:
#         print("c")


# Another line if you decide not to use the method .upper() or .lower() for example.
# https://www.w3schools.com/python/python_ref_string.asp - Handy links for python methods
#var1 = var1.upper()
#print(var1.lower())

#Splitting .split() method
# var1 = "Hello my name is Sean"
# var2 = var1.split()

# print(var2)

# var3 = " ".join(var2)

# print(var3)

# self directed study 12:30 - 1

#Trying to make 2 exit the program
# control = True

# while control:
#     print("Menu: Press 1 to continue, press 2 to exit ; ")
#     var1 = int(input("Please enter a number"))

# if var1 == 1:
#     control = True
# elif var1 == 2:
#     control = False
# else:
#     print("Invalid!")



# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# The line above is logically the same as the begining of the for loop.
# for num in range(11):
#     print(num)

# list1 = "here is a random string"

# for num in list1:
#     print(num)

# The steps option lets ou count in a specified format i.e. 2 = 0,2,4,6.
# Or you can use a -1 to count in reverse. (The third number in rnage is the step number.)
# for num in range(10,0,-1):
#     print(num)

# for num in range(11):
#     if num == 6:
#         continue
#     print(num)

## Tutorial ####
# number = 0
# while number <= 10:
#  number = number + 1
#  remainder = number % 2
#  if remainder == 1:
#      continue
#  print(number)

# for number in range(1,11):
#     remainder = number % 2
#     if remainder == 1:
#         continue
#     print(number)

# list1 = ["apple", "banana", "orange", 7]
# print(list1[0:3])

# list1 = ["apple","banana","orange", 7]

# list1[1] = "Lemon"

# list1.remove("apple")
# list1.pop(1)

# print(list1)


# control = 0
# while control < 5:
#     list1.append(input("Enter new list of items  : "))
#     control += 1


# dict1 = {1 : "John", 2 : "Dave"}

# print(dict1[1])

# dict1 = {"Anything" : ["John", "John2"], 2 : "Dave"}

# for num in range(3, 9):
#     #dict1[num] = input("enter")

#     print(dict1)

# dict1 = {"Anything" : ["John", "John2"], 2 : "Dave"}

# for key in dict1.values():
#     print(f"key: {key}, Value: {value}.")

# tup1 = "dog", "cat", "fish"

# print(tup1)

# ani1, ani2, ani3 = tup1

# print(ani1)
# print(ani2)
# print(ani3)

list1 = ["John", "John", "John", "Simon", "John"]

print(set(list1))