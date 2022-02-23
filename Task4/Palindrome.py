a=int(input("Enter a number:"))
temp=a
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if(temp==rev):
    print("The given number is a PALINDROME")
else:
    print("The given number is not a PALINDROME")