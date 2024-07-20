s = 'hello'
for index, c in enumerate(s):
    print(index, c)

fruits = ['apple', 'banana', 'mango']
for index, f1 in enumerate(fruits):
    print(index, f1)

fruits = ['apple', 'banana', 'mango']
for index, f1 in enumerate(fruits, start=1):
    print(index, f1)

marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index, m1 in enumerate(marks): #it will print after 88
  print(m1) 
  if(index == 3):
    print("Arc is awesome!")

for index, mark in enumerate(marks, start=1): #bef 98
  print(mark)
  if(index == 3):
    print("Arc is awesome!")

