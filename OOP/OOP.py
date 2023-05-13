class Human:
  name = "Aksa"
  occupation = "Python Programmer"
  networth = 0

  def info(self):
    print(f"{self.name} is a {self.occupation}") #self is a object to call a.info/b.info method

a= Human() #object
b= Human() #oject
# a.name = "Muaz"
# a.occupation = "Software Engineer"
b.name = "Muaz"
b.occupation = "Software Engineer"
# print(a.name, a.occupation)
a.info()
b.info()