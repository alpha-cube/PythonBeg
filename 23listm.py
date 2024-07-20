l=[5,3,2,6,9,5,2,1,10]
print(l)
l.sort() #ascending
print(l)
l.sort(reverse=True)#descending
print(l)
l.reverse
print(l)

print(l.count(5))

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green")) #o/p-1
print(colors.count('green'))

#append
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)

#insert(adds)
colors = ["voilet", "indigo", "blue"]
colors.insert(1, "green")             
print(colors) #o/p-['voilet', 'green', 'indigo', 'blue']


l1=[1,2,4,5,7]
l2=[3,6,8,9,10]
print(l1+l2) #concate
l1.extend(l2)
print(l1) #extend
