class Employee:
  def __init__(self,name):
    self.name= name
    
class Dancer:
  def __init__(self,dance):
   self.dance= dance

  def show(self):
    print(f"The dance is {self.dance}")
     
class DancerEmployee(Dancer,Employee):
  def __init__(self,name,dance):
    self.name= name
    self.dance= dance

o = DancerEmployee("Naomeen", "Twirky")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())
    
