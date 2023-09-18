import csv

with open('D:\\!Downloads\\input_1.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    counter, lst_price = 0, []
    for numb_str in reader:
        if counter == 0:
            dates = ''.join(numb_str).split(';')[1:]
        else:
            price = ''.join(numb_str).split(';')
            lst_price.append(price)
        counter += 1

with open('output.csv', 'w', newline='') as file:
    lst_min, dict_min = [], dict()
    for j in range(1, len(lst_price) + 1):
        min_price = lst_price[0][j]
        for i in lst_price:
            if i[j] <= min_price:
                min_price = i[j]
                dict_min[dates[j-1]] = i[0] + " " + i[j]
    columns = ["date", "excursion", "sum"]
    writer = csv.DictWriter(file, fieldnames=columns)
    print(lst_price)

    # Записываем заголовки колонок
    writer.writeheader()

    # Записываем данные
    for date, value in dict_min.items():
        excursion, sum_value = value.split()  # Разделяем значение на "экскурсию" и "сумму"
        writer.writerow({"date": date, "excursion": excursion, "sum": sum_value})
    # writer = csv.DictWriter(file, fieldnames=columns)
    # writer.writeheader()

# print(lst_price)
    # for row in reader:
    #     print(row[0], " - ", row[1])