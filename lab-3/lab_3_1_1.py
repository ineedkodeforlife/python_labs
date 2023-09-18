def reducer(m: int, n: int) -> tuple:
    for i in range(n//2, 1, -1):
        if m % i == 0 and n % i == 0:
            m, n = m//i, n//i
            return m, n
    return m, n


while True:
    a, b = input(), input()
    if a.isdigit() and b.isdigit() and int(b) > int(a):
        print(reducer(int(a), int(b)))
        break
    else:
        print('Числа а и b должны быть целыми положительными , введите еще раз')

