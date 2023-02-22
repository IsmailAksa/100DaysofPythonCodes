#with open('file.txt','r') as f:
# print(type(f))
# MOVE TO THE 10TH BYTE IN THE  FILE
#f.seek(10)
 # read the next 5 bytes
 #print(f.tell())
 #data = f.read(5)
 #print(data)

with open('file2.txt','w') as f:
 f.write("Hello world")
 f.truncate(5)

with open('file2.txt','r') as f:
 print(f.read())