#!/usr/bin/env python3

import numpy as np 

def main(): 

	i = 0 
	x = 119.0 
	
	for i in range(120): 
		if((i%2)==0):
			x += 3
		else: 
			x -= 5
	s = "%3.2e" % x 
	
	print(s)
	
if __name__ == "__main__": 
	main()
	