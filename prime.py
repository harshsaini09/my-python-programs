count=0;
num=int(input("enter a number:"));
for x in range(1,num+1):
    if (num%x==0):
        count=count+1;
        continue;
    else:
        pass;
if (count == 2):
    print("the number",num,"is prime");
else:
     print("the number",num,"is not prime");