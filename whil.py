i=0
while(i<=3):
    print(i)
    i=i+1
print('done with loop') 

j=5
while(j>0):
    print(j)
    j=j-1
#else will even exe if while doesnt work
else:#when the while loop is false it will exe else 
    print('invalid')


#do while loop does exist for py
i=1
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break