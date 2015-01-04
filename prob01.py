f=input()
k=1
while(k<=f):
 posList=["units","tens","hundreds","thousands","ten thousands","lakh","ten lakhs","crore","ten crore","billion"]
 numList=raw_input()
 s=numList.split()
 pos=s[0][::-1].index(s[1])
 print(posList[pos])
 k=k+1