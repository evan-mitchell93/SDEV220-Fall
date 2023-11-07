

#loops real fast

my_nums = [1,2,3,4]
i = 0
sum = 0
while i < len(my_nums):
    sum = sum + my_nums[i]
    if sum >= 10:
        print(sum, " greater than 10")
        break
    i += 1
else:
    print("Sum never exceeded 10")


