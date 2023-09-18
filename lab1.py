#1
# s, x = input(), input()
# arr_del = []
# for i in range(len(s) - len(x) + 1):
#     if x.lower() == s[i: i + len(x)].lower():
#         arr_del.append(s[i: i + len(x)])
#
# for i in set(arr_del):
#     s = s.replace(i, '')
#
# print(s)

#2

# a, k = list(map(lambda x: int(x), input().split())), 0
# while sum(a) != 0:
#     if a[0] != 0:
#         for i in range(len(a)):
#             if a[i] != 0:
#                 a[i] -= 1
#             else:
#                 break
#         k += 1
#     else:
#         a = a[1:]
# print(k)

#3
# set_tickets, dict_ans = set(), dict()
# for i in range(int(input())):
#     set_tickets.add(input())
#
# for i in set_tickets:
#     key = tuple(i.split()[:2])
#     if key in dict_ans:
#         dict_ans[key] += 1
#     else:
#         dict_ans[key] = 1
#
# for i, j in dict_ans.items():
#     print(*i, "-", j)


#dop
# k, ans_counter, ans = int(input()), 0, 0
# while ans_counter != k:
#     for i in range(10, 1000):
#         lst = []
#         for j in str(i):
#             lst.append(int(j))
#         if(sum(lst)) == 10:
#             ans_counter += 1
#         if ans_counter == k:
#             ans = i
#             break
#
# print(ans)