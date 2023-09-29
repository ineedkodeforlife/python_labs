#Обработка исключений при чтении и зап

try:
    # Открываем файл для чтения
    with open('example.txt', 'r') as file:
        # Читаем содержимое файла
        content = file.read()
    print(content)

except FileNotFoundError:
    print("Файл не найден. Убедитесь, что файл существует и указан правильный путь.")
except IOError as e:
    print(f"Произошла ошибка ввода/вывода: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

try:
    # Открываем файл для записи
    with open('output.txt', 'w') as file:
        # Записываем данные в файл
        file.write("ZXs")

except IOError as e:
    print(f"Произошла ошибка ввода/вывода при записи файла: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")




