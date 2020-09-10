#!/usr/bin.env python3

import numpy as np 

def main(): 
	i = 0 
	n = 10 
	x = 119.0 
	
	y = np.zeros(n,dtype=float)
	
	for i in range(n): 
		y[i] = 2.0 * float(i) + 1. 
		
	for y_element in y:
		print(y_element)
		
if __name__ == "__main__":
	main() 
	