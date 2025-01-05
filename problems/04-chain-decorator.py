# Implement a decorator function called chain_decorator that will be used to
# chain function calls. The decorator function should take another function
# argument as a callback, implement two inner wrapper functions, and finally
# return the wrapper function object in each respective wrapper function.

# Implement the inner wrapper function with the following:
# - Takes a variable number of positional and keyword arguments
# - Initializes a variable that calls the callback function with arguments
#   passed to the wrapper
# - Returns the variable multiplied by itself.

# Implement another inner wrapper function with the following:
# - Takes a variable number of positional and keyword arguments
# - Initializes a variable that calls the callback function with arguments
#   passed to the wrapper
# - Returns the variable multiplied by 3
 
# Finally, be sure to decorate num function using the decorator syntax.

# Write your function here.
def chain_decorator(cb):
    def wrapper(*args, **kwargs):
        result=cb(*args,**kwargs)
        return result*result
    def wrapper1(*args, **kwargs):
        result=cb(*args, **kwargs)
        return result * 3
    return wrapper, wrapper1

@chain_decorator
def num(a, b):
    return a + b

print(num(5, 2))  #> 441
print(num(8, 2))  #> 900
print(num(4, 9))  #> 1521