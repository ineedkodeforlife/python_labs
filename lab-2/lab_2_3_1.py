import csv
FILENAME = "players.csv"


def get_name(dictionary):
    return dictionary['Количество побед'], dictionary['Доп. показатель']

sportsman = [
 {"Спортсмен": "Tom", "Количество побед": 10, 'Доп. показатель': 256},
 {"Спортсмен": "Alice", "Количество побед": 30, 'Доп. показатель': 255},
 {"Спортсмен": "Bob", "Количество побед": 30, 'Доп. показатель': 10},
 {"Спортсмен": "Paul", "Количество побед": 30, 'Доп. показатель': 10}
]
with open(FILENAME, "w", newline="", encoding="utf8") as file:
    columns = ["Спортсмен", "Количество побед", "Доп. показатель"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    writer.writerows(sportsman)

with open(FILENAME, "r", newline="", encoding="utf8") as file:
    reader = csv.DictReader(file)
    lst_sportsman = []
    for row in reader:
        lst_sportsman.append({'Спортсмен': row['Спортсмен'], 'Количество побед': row['Количество побед'], 'Доп. показатель': row['Доп. показатель']})

    lst_sportsman.sort(key=get_name, reverse=True)

with open('results.csv', 'w', newline='', encoding="utf8") as file:
    columns, last = ['Спортсмен', 'Место'], lst_sportsman[0]
    counter = 1
    writer = csv.DictWriter(file, fieldnames=columns)
    for i in lst_sportsman:
        if i['Количество побед'] != last['Количество побед'] or i['Доп. показатель'] != last['Доп. показатель']:
            counter += 1
        last = i
        str_ans = {'Спортсмен': i['Спортсмен'], 'Место': counter}
        writer.writerow(str_ans)

