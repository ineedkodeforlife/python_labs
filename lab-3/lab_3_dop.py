def subsegment(a: list, x: int):
    for i in range(len(a)):
        ans_arr, ans_sum = [a[i]], a[i]
        for j in range(i + 1, len(a)):
            if ans_sum + a[j] < x:
                    ans_sum += a[j]
                    ans_arr.append(a[j])
            elif ans_sum + a[j] == x:
                ans_sum += a[j]
                ans_arr.append(a[j])
                return ans_arr
            else:
                break
    return False


a = [3, 10, 5, 1, 2]
x = int(input())
print(subsegment(a, x))
