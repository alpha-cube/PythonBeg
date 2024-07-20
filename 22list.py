l1=[1,2,4,3,'arc']
print(l1)
l1.append('python')
print(l1)

print(l1[0])
print(l1[5])
print(l1[-3])#l1[len(marks)-3]

if 4 in l1:
    print('4 is present')
else:
    print('4 is not present')

if 'dog' in l1:
    print('dog is present')
else:
    print('dog is not present')

if 'ar' in 'arc':
    print('ar is present')
else:
    print('ar is not present')

print(l1[:])
print(l1[1:-1])
print(l1[0:5:2])# jumping index

lst=[i*i for i in range(10)]
print(lst)
lst=[i*i for i in range(10)if i%2==0]
print(lst)

#Accepts items with the small letter “o” 
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

#Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)