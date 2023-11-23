print("Enter the num:")
n = int(input("num is :"))
count = 0
if n==0:
    print("not prime no")
elif n==1:
    print("not prime no")
else:

    for i in range(1,n):
        if n%i==0:
            count+=1

    if count > 2:
        print("Not a Primary num")
    else:
        print("primary num")