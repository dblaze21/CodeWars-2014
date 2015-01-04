from itertools import groupby
def encode(input_string):
    return [(len(list(g)), k) for k,g in groupby(input_string)]
f=input()
k=1
while(k<=f):
 st=raw_input()
 st1=encode(st)
 st1=map(list,st1)
 print(str(st1)[1:-1])
 k+=1