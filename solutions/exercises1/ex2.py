import random

number_list = []
for i in range(10):
    random_number = random.randint(1, 100)
    number_list.append(random_number)

print(sorted(number_list))
