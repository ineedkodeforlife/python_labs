k, ans_counter, ans = int(input()), 0, 0
while ans_counter != k:
    for i in range(10, 1000):
        lst = []
        for j in str(i):
            lst.append(int(j))
        if(sum(lst)) == 10:
            ans_counter += 1
        if ans_counter == k:
            ans = i
            break

print(ans)