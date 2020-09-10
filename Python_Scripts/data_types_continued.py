#!/usr/bin.env python3

s = "I am a string."

yes = True 
print(type(yes))

no = False 
print(type(no))

alpha_list = ["a", "b", "c"]
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

alpha_tuple = ("a", "b", "c",)
print(type(alpha_tuple))

try: 
	alpha_tuple[2] = "d" 
except TypeError: 
	print("we can't add element to tuples!")
print(alpha_tuple)
