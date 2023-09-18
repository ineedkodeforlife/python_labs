import os

left = int(input("Введите левую границу (в Кб): "))
right = int(input("Введите правую границу (в Кб): "))

example_dir = "./example"

count_matching_files = 0

for filename in os.listdir(example_dir):
    file_path = os.path.join(example_dir, filename)
    if os.path.isfile(file_path):
        file_size_kb = os.path.getsize(file_path) / 1024  # 1 Кб = 1024 байта

        if left <= file_size_kb <= right:
            count_matching_files += 1

# Вывести результат
print(f"Количество файлов размером от {left} Кб до {right} Кб в директории 'example': {count_matching_files}")