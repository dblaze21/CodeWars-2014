f=input()
c=1
while c<=f:
 num=input()
 k=0
 n1=0
 def check(n):
  r=1
  while n!=0: 
   d=n%10
   r=r*d
   n=n/10
  return r
 while len(str(num))!=1:
  num=check(num)
  k+=1
 print(num),
 print(k)
 c+=1