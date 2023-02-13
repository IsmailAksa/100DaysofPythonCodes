letter = "Hey my name is {1} and I am from {0}"
country = "Bangladesh"
name =  "Aksa"
#print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-string like this: Hey my name is {name} and I am from {{country}}") 

#txt = "For only {price:.2f} dollars!"
#print(txt.format(price=49.09999))
price=49.09999
txt = f"For only {price:.2f} dollars!" #python 3.6 version f-string 
print(txt)