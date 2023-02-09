
# > Define the number eleven
number = int(input("Please enter a number and press ENTER "))

number_copy = number

# > As long as result is larger than zero
while number > 0:
    
#   > Subtract three
    number -= 3

# > Check if is zero or not
if number == 0:
    print(f"{number_copy} is divisable by 3")
else:
    print(f"{number_copy} is not divisable by 3.")

#   > print result



