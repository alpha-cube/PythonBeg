x=int(input('enter a no: '))

match x:
    case 0:
        print('x is zero')
    
    case 4:
        print('x is four')
    
    case _ if x< 10 :
        print('x is <10')

    case _ :
        print(x)