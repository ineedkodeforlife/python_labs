s, x = input(), input()
ss, xx = s.lower(), x.lower()
while True:
    if xx in ss:
        new_ind = ss.index(xx)
        s = s[:new_ind] + s[new_ind + len(xx):]
        ss = ss[:new_ind] + ss[new_ind + len(xx):]
        # print(s)
    else:
        break
print(s)
