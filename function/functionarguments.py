#def average(a,b):
#  print("The average is",(a+b)/2)

#average(4,6)

#default
#def name(fname, mname ="John",lname="Whatson"):
#   print("Hello",fname,mname,lname)


#name("Amy", "Agarwal","Zaidy")

#def average(*numbers):
#  #tupple class is *numbers
#  sum = 0
#  for i in numbers:
#    sum = sum + i
#  print("Average is", sum / len(numbers))


#average(5, 6)

#def name(**name):
#  print(type(name))
#  print("Hello,", name["fname"], name["mname"], name["lname"])

#name(mname="Aksa", lname="Ismail",fname="Unlucky")

def average(*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
#  print("Average is", sum / len(numbers))
  return sum / len(numbers) #return the value to the calling function


#average(5, 6)
c = average(5,6,7,1) #calling function
print(c)