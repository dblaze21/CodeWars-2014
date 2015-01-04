num=input()
def binary(n):
 binary = ""
 if (n == 0):
  return "0000"    
 while (n > 0):
  rem = n % 2
  binary = str(rem) + binary
  n = n / 2       
 return binary
print(binary(num))