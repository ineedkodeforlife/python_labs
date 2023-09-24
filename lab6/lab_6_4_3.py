from threading import Thread
import os
import time


def count_files(directory):
    count = len(os.listdir(directory))
    return count


def create_size_file(directory):
    size = count_files(directory)
    file_path = os.path.join(directory, 'size.txt')
    with open(file_path, 'w') as file:
        file.write(str(size))


def search_and_create_size_files(directory):
    for root, dirs, files in os.walk(directory):
        create_size_file(root)


def search_create_size_matrix_thread(directory):
    threads = []
    for root, dirs, files in os.walk(directory):
        t = Thread(target=create_size_file, args=(root,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

st_time = time.time()
search_and_create_size_files('.') #without trhreading
print(f'Without threading {time.time() - st_time}')

st_time = time.time()
search_create_size_matrix_thread('.') #with threading
print(f'With threading {time.time() - st_time}')