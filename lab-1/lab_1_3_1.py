set_tickets, dict_ans = set(), dict()
for i in range(int(input())):
    set_tickets.add(input())

for i in set_tickets:
    key = tuple(i.split()[:2])
    if key in dict_ans:
        dict_ans[key] += 1
    else:
        dict_ans[key] = 1

for i, j in dict_ans.items():
    print(*i, "-", j)