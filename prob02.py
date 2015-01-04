f=input()
k=1
while(k<=f):
 if k<100:
  s=raw_input()
  st=s.split(",")
  st = map(int, st)
  st1=range(st[0],(st[len(st)-1]+(st[1]-st[0])),(st[1]-st[0]))
  if st1 == st:
   print("Yes")
  else:
   print("No")
  k+=1