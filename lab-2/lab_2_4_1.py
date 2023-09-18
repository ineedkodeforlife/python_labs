import os
import random

example_dir = "./example"

if not os.path.exists(example_dir):
    os.makedirs(example_dir)

for i in range(100):
    file_size = random.randint(1, 100) * 1024  # 1 Кб = 1024 байта

    file_name = os.path.join(example_dir, f"file_{i+1:03d}.txt")

    # Создать файл с случайным содержимым
    with open(file_name, "wb") as file:
        file.write(os.urandom(file_size))
