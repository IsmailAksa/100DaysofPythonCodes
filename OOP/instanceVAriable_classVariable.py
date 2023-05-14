class Employee:
  companyName="Apple" #class variable
  noOfEmployee= 0
  def __init__(self,name):
    self.name = name
    self.raise_amount = 20
    Employee.noOfEmployee+=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)

emp1 = Employee("Aksa")
emp1.raise_amount = 3 #instance variable
emp1.companyName="Apple Bangladesh" #instance variable
emp1.showDetails()
emp2 = Employee("Muaz")
emp2.showDetails()
 