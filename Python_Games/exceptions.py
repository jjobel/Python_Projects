#!/usr/bin/env python3 

try:
	print(a) 
except:
	print("a is not defined!")

try: 
	print(a)
except NameError:
	print("a is still not defined!")
except:
	print("Somethng else went wrong.")

print(a)
