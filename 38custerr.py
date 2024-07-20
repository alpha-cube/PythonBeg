salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
print(salary)


# Define a custom exception
class CustomError(Exception):
    pass

# Example function that raises the custom exception
def risky_function(x):
    if x < 0:
        raise CustomError("Negative value error")
    return x * 2

# Using the custom exception in a try-except block
try:
    result = risky_function(-5)
    print(result)
except CustomError as e:
    print(f"Caught an error: {e}")

# Output will be: Caught an error: Negative value error

