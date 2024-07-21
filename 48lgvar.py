x = 10  # global variable


def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)
#print(y) cant be print directly



x = 10  # global variable
def my_function():
    global x
    x = 5  # this will change the value of the global variable x
    y = 4  # local variable
    return y  # return the local variable

# Call the function and store the returned value in a global variable
y = my_function()

print(x)  # prints 5
print(y)  # prints 4
