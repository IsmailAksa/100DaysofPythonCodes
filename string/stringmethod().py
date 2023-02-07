# String are immutable
a = "Aksa!! !!!!!! Aksa"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Aksa", "Mr.Unknown"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())
str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50))
print(a.count("Aksa"))

str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))
print(str1.find("the"))
#print(str1.index("thes"))
str1 = "WelcometotheConsole"
print(str1.isalnum())
str1 = "welcome000"
print(str1.isalpha())
str1 = "hello aksa"
print(str1.islower())

str1 = "hello aksa\n"
print(str1.isprintable())

str2 = "  "
print(str2.isspace())

str1 = "World Health"
print(str1.istitle())
str2 = "To kill a mocking bird"
print(str2.istitle())
print(str2.startswith("To"))
print(str2.swapcase())
print(str2.title())