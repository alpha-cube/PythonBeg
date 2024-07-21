# READING A FILE

# in read it will just look for file if doesnt exit = error
f = open("try.txt", "r")
# print(f)
text = f.read()
print(text)
f.close()

# in write mode if file doesnt exist it will create
f = open("try2.txt", "w")
f.write("Hello, world!")

# append-approach 1
f = open("try2.txt", "a")
f.write("keep adding")
f.close()  # this is import to save

# append-approach 2
with open("myfile.txt", "a") as f:
    f.write("Hey I am inside with")
