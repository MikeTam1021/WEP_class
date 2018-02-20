
class Thing:

    def __init__(self, data):
        """
        This is a docstring. It is used as a comment to explain what
        classes do. It will not do anything in executing code.

        the __init__ method is a constructor - when a class is instantiated
        this is run. 'self' is necessary in the class and contains all the
        class's data and methods

        parameter: data - string
        """

        self.data = data


    def method(self):
        """
        Another docstring! Please read me to learn more....

        this is a special type of function in a class called a method

        it can use or modify data that is in the class by using 'self'
        """


        self.data = self.data + ' method call '

# lets instatiate a thing
#
# we must include some data because it has no default value
#
# the docstring tells us data is a string, make sure the type is correct

thing = Thing("data")

# now let's call the method

thing.method()

# let's check the data

thing.data

#let's do it again

thing.method()
thing.data
