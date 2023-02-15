#dic = {
#  "Aksa": "Human Being",
#   "Tea": "Object",
#  199 :"Muaz"
#}
#print(dic["Aksa"], 199)
info = {'name':"Aksa",'age':19,"eligible":True}
#print(info)
#print(info['name'])
#print(info.get('eligible1'))
#print(info.keys())
#print(info.values())

#for key in info.keys():
  #print(info[key])
# print(f"The value corresponding to key {key} is {info[key]}")

print(info.items())
for key , value in info.items():
 print(f"The value corresponding to key {key} is {value}")