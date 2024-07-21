def welcome ():
    print('hey bro uh can do it !!') 

#o/p main (if the code is being run by itself ie not imported to other then it ill print the below welcome  )   
print(__name__)              #if arc is imported to other then o/p-arc ie arc/=main then below welcome will not print
if __name__ == "__main__":
    welcome()
arc=7
