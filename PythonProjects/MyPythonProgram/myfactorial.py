def my_Factorial(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n<0:
        return "invalid"
    else:
        return (n)*my_Factorial(n-1)

n=my_Factorial(-6)
print(n)