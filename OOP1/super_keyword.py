class Employee:
 def __init__(self,name,id):
   self.name=name
   self.id=id
  
class Programmer(Employee):
 def __init__(self,name,id,lang):
   super().__init__(name,id)
   self.lang=lang

niki=Employee("Niki","430")
aksa=Programmer("Aksa","4300","Python3")
print(aksa.name)
print(aksa.id)
print(aksa.lang)