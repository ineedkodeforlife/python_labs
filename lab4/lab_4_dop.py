import random
lst_random = []
for i in range(random.randint(5, 15)):
    lst_random.append(random.randint(1, 20))

counter, lst_random_copy = 0, lst_random.copy()
while len(set(lst_random_copy)) != 1:
    ind_max, ind_min = lst_random_copy.index(max(lst_random_copy)), lst_random_copy.index(min(lst_random_copy))
    lst_random_copy[ind_max] = lst_random_copy[ind_max] - lst_random_copy[ind_min]
    counter += 1

print(lst_random, counter)
