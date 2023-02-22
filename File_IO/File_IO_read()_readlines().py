#f = open('myfile.txt', 'r')
#i=0
#while True:
#   i= i+1
#   line = f.readline()
#   if not line:
#     break
#  m1 = int(line.split(",")[0])
#   m2 = line.split(",")[1]
#   m3 = line.split(",")[2]
#   print(f"marks of student {i} in maths is: {m1*2}")
#   print(f"marks of student {i} in physics is: {m2}")
#   print(f"marks of student {i} in chemistry is: {m3}")
   
#   print(line)

f= open('myfile2.txt', 'w')
lines=["line1\n", "line2\n","line3\n" ]
f.writelines(lines)
f.close()

   
     
  