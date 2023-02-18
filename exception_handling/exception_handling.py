#a = input("Enter the name:")
#print(f"multiplication table of {a} is:")
#try:
# for i in range (1,11):
#  print(f"int{a} X {i} = {int (a)*i }")
#except :
#  print("Sorry some error occured")
  
#  print("Some imp lines of code")
#  print("End of the program")
try:
  num = int(input("Enter an integer:"))
  a= [6,3]
  print(a[num])

except ValueError:
  print("Nubmer entered is not an integer.")

except IndexError:
  print("IndexError")
