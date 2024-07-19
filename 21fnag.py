#required arg
def avg(a,b):
    print('avg',(a+b)/2)
avg(3,5)

#return

def add_numbers(a, b):
    result = a + b
    return result
sum_result = add_numbers(4, 5)
print("The sum", sum_result)

#default arg
def avg(a=4,b=7):
    print('avg',(a+b)/2)

avg(3,5)#it will coverwrite the def arg
avg(8)#it will ass a=8
avg(b=9) #it will ass b=9

#req arg- uh should atleast specify ones

def nm(fn='',mn='loves',ln='python'):
    print(fn,mn,ln)

nm('sai')
nm('sai','hates')

#variable arg
def avg(*n1): #n1 is tuple (tuple=(),list=[])
    sum=0
    for i in n1:
        sum+=i
    print('avg: ', sum/len(n1))

avg(4,5,8,2)

