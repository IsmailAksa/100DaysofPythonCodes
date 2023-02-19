import os
#if(not os.path.exists("data")): #to create file automatically in vs code by creating main.py
#  os.mkdir("data")



for i in range(0,100):
  #os.mkdir(f"data/Day(i+1)")
  os.rename(f"data/Day{i+1}",f"data/Tutorial {i+1}")