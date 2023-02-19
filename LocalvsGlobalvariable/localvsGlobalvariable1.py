x = 10 #global variable

def myfunc():
  global x
  x = 4
  y = 5  #local variable
  print(y)

myfunc()
print(x)
#print(y) #this will cause an error because y is local variable and is not accesible outside of the function
