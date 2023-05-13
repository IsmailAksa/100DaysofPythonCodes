class Student:
  def __init__(self):
    self._name="Aksa"

  def _funName(self): #protected method
    return "AksaisaProgrammer"

class Subject(Student): #inherted
  pass

obj=Student()
obj1=Subject()
# Calling by object of the Student class
print(obj._name) #single undercore is accesible
print(obj._funName())
# Calling by object of the Subject class
print(obj1._name)
print(obj1._funName()) 
# __ underscore is private method/mangling