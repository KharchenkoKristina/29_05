import random

num_elements = random.randint(3, 10)
random_lst = [random.randint(1, 100) for _ in range(num_elements)]
print("Рандомний список:", random_lst)

new_lst = [random_lst[0], random_lst[2], random_lst[-2]]
print("Новий список:", new_lst)
