############
# Example 1
############
# Get a character input from the user
ch = input("Enter a character: ")
# Print the ASCII value of the character
print(ord(ch))


############
# Example 2
############
# For loop in Python

for letter in 'Python': # First Example
    print('Current Letter :', letter)
fruits = ['banana', 'apple', 'mango']
for fruit in fruits: # Second Example
    print('Current fruit :', fruit)
print("Good bye!")


############
# Example 3
############
# IF else in Python

var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)
else:
    print("1 - Got a false expression value")
    print(var1)
var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)
else:
    print("2 - Got a false expression value")
    print(var2)
print("Good bye!")

############
# Example 4
############
# Nested IF in Python

var = 100
if var < 200:
    print("Expression value is less than 200")
    if var == 150:
        print("Which is 150")
    elif var == 100:
        print("Which is 100")
    elif var == 50:
        print("Which is 50")
elif var < 50:
    print("Expression value is less than 50")
else:
    print("Could not find true expression")
print("Good bye!")


############
# Example 5
############
# Nested While

i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): 
            break
        j = j + 1
        if (j > i/j) : 
            print(i, " is prime")
    i = i + 1
print("Good bye kaza !")





