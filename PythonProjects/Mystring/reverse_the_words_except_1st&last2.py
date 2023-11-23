input = "Hi how are you World"
output = "Hi woh era uoy World"

list1 = input.split()

n = len(list1)
for i in range(1,n-1):
    b = list1[i][::-1]
    list1[i] = b

print(" ".join(list1))

