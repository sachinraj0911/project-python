def prim(nums):
    a = []
    count = 0
    for num in nums:
        for i in range(1,num):
            if num%i==0: # last num is num-1
                count+=1

        if count == 1:
            a.append(num)
        count = 0
    return a


nums = [0,1,2,6,9,7,5,19,11,17]
prim_1=prim(nums)
print(prim_1)