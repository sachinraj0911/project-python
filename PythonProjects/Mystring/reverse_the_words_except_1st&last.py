input = "Hi how are you World"
output = "Hi woh era uoy World"

list1 = input.split()

n = len(list1)
for i in range(1,n-1):
    b = list1[i][::-1]
    list1.remove(list1[i])
    list1.insert(i, b)

print(list1)

print(" ".join(list1))

