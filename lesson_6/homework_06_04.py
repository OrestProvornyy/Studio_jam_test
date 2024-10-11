import random

num_list = []

for num in range(10):
    num = random.randint(0, 100)
    num_list.append(num)

print(num_list)
#####

summ_even = 0

for numsumm in num_list:
    if numsumm % 2 == 0:
        summ_even += numsumm

print(summ_even)

####
summ_even_v2 = sum([num_v2 for num_v2 in num_list if num_v2 % 2 == 0])

print(summ_even_v2)
