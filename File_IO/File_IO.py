#READING A FILE
#f = open ('myfile.txt', "r")

#text = f.read()
#print(text)
#f.close()

#WRITNG A FILE
#f = open ('myfile.txt2', "w")
#f = open ('myfile.txt2', "a") #append
#f.write("I am not okay")
#print(f)
#f.close()
with open("myfile.txt2","a") as f: # with--> this we can close file without f.close() function 
  f.write("Hey i am a looner")
