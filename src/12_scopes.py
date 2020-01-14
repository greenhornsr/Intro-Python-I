# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    x = 99
    print("local var x: ", x)

change_x()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print("global var x: ", x)


# This nested function has a similar problem.

def outer():
    y = 120
    print("outer var y: ", y)
    def inner():
        y = 999
        print("inner var y: ", y)
    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print("Global var y: ", y)

outer()