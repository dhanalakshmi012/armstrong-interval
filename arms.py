# armstrong-interval
upper=raw_input("enter the num:")
lower=raw_input("enter the num:")
n=raw_input("enter the num:")
for n in range(lower,upper+1)
temp=n
sum=0
while(n>0):
   digit=n%10
   sum+=digit**3
   n=n//10
if(temp=sum):
   print(sum)
