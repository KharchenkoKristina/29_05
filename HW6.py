my_list = [1, 23, 3, 13]

if len(my_list) > 1:
    my_list = [my_list[-1]] + my_list[:-1]

print(my_list)
