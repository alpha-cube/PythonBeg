print('''jkshh
sjkfbsjkfh
sdjkbsdfb\n'''
)

#looping (to print all string char)
a1='''arc
ane
711\n'''

for op in a1:
    print(op)

a='arcane'
print(a[2]) #index  o/p 'c'

print(len(a)) #length of string

#slicing
a2='arcane'
print(a2[0:3]) #it will take 0,1,2 index char only !! o/p-arc
print(a2[:3]) #same as above o/p-arc

print(a2[0:-2]) #it cal [0:len (a2)-2] o/p-arca
print(a2[-4:-1]) #charleng-6 (6-4=2) ie 'c' end -1 ie 'n'

nm='harry'
print(nm[-4:-2]) #o/p-ar