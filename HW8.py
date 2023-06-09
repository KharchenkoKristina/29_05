lst = [1, 3, 5]

if not lst:
    result = 0
else:
    sum_l = sum(lst[::2])
    result = sum_l * lst[-1]

print(result)
