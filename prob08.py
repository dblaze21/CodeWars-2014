num=input()
flag=False

def reverse(n):
 rev=str(n)[::-1]
 return(int(rev))
temp=reverse(num)

while flag!=True:
 num+=1
 print(num)
 temp=reverse(num)
 print("num",num,"temp",temp)
 if num is temp:
  print(temp)
  flag=True
  