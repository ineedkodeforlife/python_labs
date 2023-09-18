import datetime


def nearest_date(*args):
    now_date, ans = datetime.date.today(), ('', 0)
    min_dif = now_date - datetime.date(1, 1, 1)
    for i in args:
        dat = i.split('.')
        difference = datetime.date(int(dat[2]), int(dat[1]), int(dat[0])) - now_date
        print(difference)
        if abs(difference) < min_dif:
            min_dif = abs(difference)
            ans = i, difference
        elif difference == min_dif:
            if difference > ans[1]:
                ans = i, difference
    print(ans[0])


