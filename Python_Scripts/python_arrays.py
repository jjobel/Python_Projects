#!/usr/bin/env python3

x = [0.0, 3.0, 5.0, 2.5, 3.7] 
print(type(x))

x.pop(2)
print(x)

x.remove(2.5)
print(x)

x.append(1.2)
print(x) 

y = x.copy()
print(y) 

print(y.count(0.0))

print(y.index(3.7))

y.sort() 
print(y) 

y.reverse()
print(y) 

y.clear()
print(y) 
