a=int(input('Enter a no:'))

print(f'Multi of {a} is :')

for i in range(1,11):
    print(f'{a} * {i} = {a*i}')

print('EXE complete')
print('if any error this will not print')

#exception handling
a=int(input('Enter a no:'))

print(f'Multi of {a} is :')

try:
    for i in range(1,11):
        print(f'{a} * {i} = {a*i}')

except Exception as e:
    print(e) #it will display error

except: #exception handling is gen used to continue the exe of the code even after error occurs
    print('Invalid input')

print('EXE complete')
print('if any error this will print')

#another one
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")

#finally
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.") #this block always execute