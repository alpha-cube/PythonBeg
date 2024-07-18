#if-else
a=int(input('Enter ur age: '))

# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

if(a>=18):
    print('U r eligible for voting')

else:
    print('U r not eligible for voting')

#elif
num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")

elif (num == 0):
  print("Number is Zero.")

elif (num == 7):
  print("Number is Special.")

else:
  print("Number is positive.")

#nested else if
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")