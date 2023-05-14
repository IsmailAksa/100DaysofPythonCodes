# x=(1,2,3)
# print(dir(x)) 
# print(x.__add__)

class Person:
  def __init__(self,name,age):
    self.name= name
    self.age= age
    self.version=1
    # print(f"The name is {self.name} and age is {self.age}")

p=Person("Muaz",2)
print(p.__dict__)
# print(help(str))
print(help(Person)) #documentation
