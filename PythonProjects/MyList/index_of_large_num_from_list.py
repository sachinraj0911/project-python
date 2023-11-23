def find_the_index_large_num(list1, large_num):
    index_of_large_num = list1.index(large_num)
    return index_of_large_num

def find_large_num(list2):
    a1 = sorted(list2)
    val1 = a1[-1]
    return val1

a = [3, 2, 1, 9, 16, 7, 6, 5]
large_num = find_large_num(a)
val = find_the_index_large_num(a, large_num)
print(val)