def my_generator():
  for i in range(50000):
    #complex computation
    yield i

gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
for j in gen:
  print(j)