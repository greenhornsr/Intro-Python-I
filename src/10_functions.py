# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(somenum):
    if somenum % 2 == 0:
        #print or return?
        # print(True)
        return True
    else:
        # print(False)
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)


# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
if is_even(num) == True:
    print("Even!")
else: 
    print("Odd")

