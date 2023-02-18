a = int(input("Enter any value between 7 and 13"))

if(a<7 or a>13):
  raise ValueError("Value should be between 7 and 13")