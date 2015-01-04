import math
f=input()
k=1
while(k<=f):
 num=raw_input()	
 s=num.split()
 s = [float(i) for i in s]
 c=math.factorial(s[0])/(math.factorial(s[1])*math.factorial(s[0]-s[1]))
 print(c)
 k=k+1