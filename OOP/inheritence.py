class Employee:
  def __init__(self,name,id):
    self.name = name
    self.id = id

  def showDetail(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Progammer(Employee):
  def showLanguage(self):
    print("Default language is Python")

e= Employee("Aksa", 230)
e.showDetail()
e1= Employee("Muaz", 200)
e1.showDetail()
e2=Progammer("Niki",400)
e2.showDetail()
e2.showLanguage()