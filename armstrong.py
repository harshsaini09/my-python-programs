num=int(input("enter a number:"));
temp=num;
sum=0;
while(num!=0):
    a=num%10;
    sum+=a**3;
    num//=10;
if(temp==sum):
    print("the number",temp,"is amstrong");
else:
    print("the number",temp,"is not amstrong");