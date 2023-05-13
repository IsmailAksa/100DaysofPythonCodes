class Human:
  def __init__(self,n,o):  #everytime the method will call the funtion when the object a.Huma() will create 
    print("Hey I am a developer")
  # name = "Aksa"
  # occ = "Developer"
    self.name=n
    self.occ= o

  def info(self) :
   print(f"{self.name} is a {self.occ}")

a=Human("Aksa","Developer")
b=Human("Muaz","Engineer")
# print(a.name)
# a.name= "Lia"
# a.ooc= "Engineer"
a.info() 
b.info() 
