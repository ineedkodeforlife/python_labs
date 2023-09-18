s, x = input(), input()
arr_del = []
for i in range(len(s) - len(x) + 1):
    if x.lower() == s[i: i + len(x)].lower():
        arr_del.append(s[i: i + len(x)])

for i in set(arr_del):
    s = s.replace(i, '')

print(s)
