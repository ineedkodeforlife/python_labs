a, b = '192.168.1.2', '255.255.254.0'
s, lst_ans = '', []
for i in b.split('.'):
    s += str(bin(int(i))[2:]).zfill(8)
for i in range(len(s)):
    if s[i] == '0':
        stop_point = i
        break

with open('ip.log', 'r') as file:
    for i in file:
        str_bin, str_ans, str_ans_bin = '', '', ''
        counter = 0
        for digit_i, digit_b in zip(i.split('.'), b.split('.')):
            str_ans += str((int(digit_i) & int(digit_b)))
            counter += 1
            if counter != 4:
                str_ans += '.'
        lst_ans.append(str_ans)


    with open('ip_solve.log', 'w') as writefile:
        for i in lst_ans:
            writefile.write(i + '\n')