# this code demonstrates defining and calling a function
# we define a function with 'def <YOUR NAME>:' and then an indented block
# functions end with a return to send the value from a call


def add_two_numbers(x, y):
    """
    this function adds x and y
    """
    z = x + y
    return z

# a function is called by passing arguments and using paranthesis

add_two_numbers(3, 5)   # this will return 8

# the arguments of a function cannot be used outside the function

print(z)

z = add_two_numbers(3, 5) # we can put the return value in a variable

# the variable 'z' can have any name here. it is a new variable

print(z)
