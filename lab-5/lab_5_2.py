#Сохранение, Восстановление файла
data_to_save = 'Я помню чудное мгновенье, передо мной явилась ты'

# Сохраняем данные в файл в формате JSON
try:
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write(data_to_save)
    print("Данные успешно сохранены в файл 'data.txt'.")
except IOError as e:
    print(f"Произошла ошибка ввода/вывода при сохранении файла: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

# Восстанавливаем данные из файла
try:
    with open('data.txt', 'r', encoding='utf-8') as file:
        loaded_data = file.read()
    print("Данные успешно загружены из файла 'data.txt':", loaded_data)
except FileNotFoundError:
    print("Файл 'data.txt' не найден. Убедитесь, что файл существует и указан правильный путь.")
except IOError as e:
    print(f"Произошла ошибка ввода/вывода при чтении файла: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
