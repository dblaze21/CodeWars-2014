st1=raw_input()
st=st1.split()
k=1
s=0
d=0
while k<=int(float(st[3])):
 sup=[]
 inp=raw_input()
 inp1=inp.split(';')
 sup=inp1[0]
 dem=inp1[1]
 sup1=sup.split(',')
 dem1=dem.split(',')
 c=0
 while c<int(float(st[0])):
  s=s+int(float(sup1[c]))
  c+=1
 c=0
 while c<int(float(st[1])):
  d=d+int(float(dem1[c]))
  c+=1
 print(s,d) 
 if s>d:
  dif1=s-d
  t1=int(float(st[2]))-dif1*3
  print(t1)
  k+=1
 if s<d:
  dif2=d-s
  t2=t1+dif2*4
  print(t2)
  k+=1
 if s==d:
  print(t2)
  k+=1