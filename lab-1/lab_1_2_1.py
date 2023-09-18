a, k = list(map(lambda x: int(x), input().split())), 0
while sum(a) != 0:
    if a[0] != 0:
        for i in range(len(a)):
            if a[i] != 0:
                a[i] -= 1
            else:
                break
        k += 1
    else:
        a = a[1:]
print(k)