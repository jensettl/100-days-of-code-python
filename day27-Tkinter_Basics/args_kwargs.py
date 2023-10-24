# *args & **kwargs =====================================================================================================
# Default values are used for the parameters that are not specified func(param1, param2, param3="default value")
# *args and **kwargs are used to pass a variable number of arguments to a function


# *args
# *args is used to pass a variable number of non-keyworded arguments list of arguments
def add(*args):
    print([i for i in args])
    print(type(args))  # tuple
    return sum(args)


add(1, 3, 5, 9, 20)


# **kwargs
# **kwargs is used to pass a variable number of keyworded arguments dictionary of arguments
def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))  # dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
