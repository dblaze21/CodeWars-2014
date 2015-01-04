f=input()
l=1
while(l<=f):
 def ifactors(n):
    return [i for i in range(2, n/2+1) if n % i == 0]
 def perfect(n):
    return [i for i in range(2, n+1) if sum(ifactors(i)) + 1 == i]
 n=input() 
 k=perfect(n)
 print(k)
 l=l+1