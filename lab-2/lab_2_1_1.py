with open('ip.log', 'w') as file:
    a, a_str, check, counter = [0, 0, 0, -1], ['0', '0', '0', '0'], 0, 0
    while counter != 10000:
        for _ in range(256):
            a[-1] += 1
            a_str[-1] = str(a[-1])
            file.write('.'.join(a_str) + '\n')
            if counter != 9999:
                counter += 1
            else:
                counter += 1
                break
        a[-1] = -1
        if check >= 2:
            check = -1
        check += 1
        a[check] += 1
        a_str[check] = str(a[check])