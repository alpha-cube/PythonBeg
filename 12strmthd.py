a = "Arcane"
print(a)
print(a.upper())
print(a.lower())

# center
print(a.center(25))

b = "--dog- -dark- --!!"
print(b)
print(b.rstrip("-"))  # only rm ending one
print(b.lstrip("-"))  # only rm starting one

print(b.count("a"))

print(b.replace("dog", "cat"))

print(b.split("d"))
print(b.split(" "))

# capitalize
a1 = "heLLO mY Friend"
print(a1.capitalize())

# startswith disp boo
b1 = "i am a boy"
print(b1.startswith("i"))

# endwith dis boolean
b1 = "i am a boy"
print(b1.endswith("boy"))
print(b1.endswith("dog"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

# find dis index val
str2 = "He's name is Dan. He is an honest man."
print(str2.find("ishh"))

str1 = "WelcomeToTheConsole"  # A-Z,a-z,0-9
print(str1.isalnum())

str1 = "Welcome"  # A-Z,a-z
print(str1.isalpha())

str1 = "Welcome00"  # A-Z,a-z
print(str1.isalpha())  # false

str1 = "hello world"
print(str1.islower())  # true

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())  # false (as \n is not prt)
str1 = "         "  # using Spacebar
print(str1.isspace())
str2 = "  "  # using Tab
print(str2.isspace())

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())
