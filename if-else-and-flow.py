#!/usr/bin/env python3
def flow_control(k):

	if(k==0):
		s = "Variable k = %d equals 0." % k 
		
	elif(k==1):
		s = "Variable k = %d equals 1." % k
	
	else: 
		s = "Variable k = %d does not equal 0 or 1." % k 
		
	print(s)
	
def main(): 

	i = 0 
	
	flow_control(i)
	i = 1 
	flow_control(i)
	i = 2 
	flow_control(i)
	
if __name__ == "__main__": 
	main()
	