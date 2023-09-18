def hofstadter_f_m(n: int):
    F = [0] * (n)
    M = [0] * (n)

    M[0] = 0
    F[0] = 1

    for i in range(1, n):
        F[i] = i - M[F[i - 1]]
        M[i] = i - F[M[i - 1]]

    return zip(F[:], M[:])


n = 5
for f, m in hofstadter_f_m(n):
    print(f"F({n}): {f}, M({n}): {m}")

