import math
from math import ceil
f=input()
k=1
while(k<=f):
 num=raw_input()	
 s=num.split(",")
 s = [float(i) for i in s]
 dist=math.sqrt(math.pow(s[3]-s[0],2)+math.pow(s[4]-s[1],2)+math.pow(s[5]-s[2],2))
 print(ceil(dist*10000)/10000.0)
 k=k+1
