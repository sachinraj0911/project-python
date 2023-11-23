def my_Fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n < 0:
        return "invalid"
    else:
        return my_Fibonacci(n - 2) + my_Fibonacci(n-1)
n=6
print("Fibonacci series")
for i in range(n):
    n = my_Fibonacci(i)
    print(n,end=" ")
