src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(src)

repeated_nums = src[:]
for i in set(repeated_nums):
    repeated_nums.remove(i)

print([el for el in src if el not in repeated_nums])
