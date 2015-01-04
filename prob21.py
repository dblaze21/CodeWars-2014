n=raw_input()
mn=n.split()
stahp=int(float(mn[0]))
mx=[]
my=[]
st1=st2=st3=st4=False
f1=f2=False
l1=l2=False
k=1
while k<=stahp:
 temp=raw_input() 	
 temp1=temp.split(',')
 mx.append(temp1[0])
 my.append(temp1[1])
 zipped=zip(mx,my)
 szipped=sorted(zipped)
 k+=1
k=0
mx1=[]
my1=[]
while k<stahp:
 mx1.append(int(float(szipped[k][0])))
 my1.append(int(float(szipped[k][1])))
 k+=1
print("mx1=",mx1)
print("my1=",my1)
f=input()
k=1
while k<=f:
 ans=[]
 inp=raw_input()
 inp1=inp.split(',')
 """if mx1.index(int(float(inp1[0]))) is my1.index(int(float(inp1[1]))) or mx1.index(int(float(inp1[1]))) is my1.index(int(float(inp1[0]))):
  print("1")
  k+=1
  continue"""
 """if int(float(inp1[0])) in my1 and int(float(inp1[1])) in my1:
  p1=my1.index(int(float(inp1[0])))
  p2=my1.index(int(float(inp1[1])))
  out2=abs(p2-(p1+1))
  print(out2+1)
  st2=True
  l2=True
  k+=1
  if l2 is True:
   continue"""
 #if x1.index(int(float(inp1[0]))) is not my1.index(int(float(inp1[1]))) and mx1.index(int(float(inp1[1]))) is not my1.index(int(float(inp1[0]))):
 if int(float(inp1[0])) in mx1 and int(float(inp1[1])) in my1:
  p1=mx1.index(int(float(inp1[0])))
  p2=my1.index(int(float(inp1[1])))
  out3=abs((p1+1)-p2)
  f1=True
  print("out3",out3,(p2+1)-p1)
  print(abs(out3)-abs((p2+1)-abs(p1)))
  k+=1
 if int(float(inp1[0])) in my1 and int(float(inp1[1])) in mx1:
  p1=my1.index(int(float(inp1[0])))
  p2=mx1.index(int(float(inp1[1])))
  out4=abs(p2-(p1+1))
  f2=True
  print("out4",out4,(p2+1)-p1)
  print(abs(out4-(p2+1)-(p1+1)))
  k+=1

 """if int(float(inp1[0])) in mx1 and int(float(inp1[1])) in mx1:
  p1=mx1.index(int(float(inp1[0])))
  p2=mx1.index(int(float(inp1[1])))
  out1=abs(p2-(p1+1))
  st1=True
  l1=True
  k+=1"""
  
 
  
 
  
 if int(float(inp1[0])) not in mx1 and int(float(inp1[0])) not in my1 and int(float(inp1[1])) not in mx1 and int(float(inp1[1])) not in my1:
  print("No Path Found")
 """if st1 is True:
  ans.append(out1)
 if st2 is True:
  ans.append(out2)
 if st3 is True:
  ans.append(out3)
 if st4 is True:
  ans.append(out4)
 if f1 is True or f2 is True:
  print(ans[1])
 if l1 is True or l2 is True:
  print(max(ans))
 print("ans=",ans)
 print(ans[len(ans)-1])"""

