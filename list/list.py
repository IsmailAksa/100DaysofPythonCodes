marks = [3, 5, 6, "Muaz",True,6,7,2,32,345,23]
#print(marks)
#print(type(marks))
#print(marks[0])
#print(marks[1])
#print(marks[2])
#print(marks[3])
#print(marks[4])

#print(marks[-3]) #negative index
#print(marks[len(marks)-3]) #positive index
#if "6" in marks:
#  print("yes")
#else:
#  print("no")

#if "az" in "Muaz": #same thing applies for string
#  print("Yes")

#print(marks[8])
#print(marks[1:8])
#print(marks[1:8:2])
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2]
print(lst)