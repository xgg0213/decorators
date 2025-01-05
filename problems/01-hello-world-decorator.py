# Implement a decorator function called `hello_world_decorator` that will be
# used to `print` statements. The decorator function should take another
# function argument as a callback, implement an inner wrapper function, and
# finally return the wrapper function object.

# Implement the inner wrapper function with the following:
# - A print statement of the string "Hello"
# - Calls the callback function
# - Another print statement after the callback containing the string "Goodnight"
 
# Finally, be sure to decorate the `world` function using the decorator syntax.

# Write your function here.
def hello_world_decorator(callback):
    def wrapper():
        print("Hello")
        callback()  # Call the callback function
        print("Goodnight")
    return wrapper
# Define the function to be decorated
# @hello_world_decorator
def world():
  print("World")

# world() #> Hello World Goodnight

# or use below
hello_world=hello_world_decorator(world)
hello_world()