s1 = {1,2,5,6}
s2 = {3,5,6}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
cities = {"Dhaka","Delhi", "Karachi", "Seul", "Berlin"}
#cities2 = {"Tokyo", "Madrid", "Spain", "Berlin","Dhaka"}
#cities3 = cities.intersection(cities2)
#cities3 = cities.symmetric_difference(cities2)
#cities3 = cities.difference(cities2) # A-B
#cities3 = cities.isdisjoint(cities2) #no intersection
#cities3 = {"Dhaka", "Delhi", "Karachi"}
#cities3 = cities.issuperset(cities2) 
#print(cities3)
#print(cities.issuperset(cities3))
#print(cities3.issubset(cities))
#cities.remove("Karachi")
#item=cities.pop()
cities.clear()
print(cities)