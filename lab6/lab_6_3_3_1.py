import time
from multiprocessing import Pool
from math import sqrt



def formula(i: int, j: int):
    return sqrt((i - j) ** 2)


def sync_create_matrix(size: int):
    return [[formula(i, j) for j in range(1, size + 1)] for i in range(1, size + 1)]


def create_row(data: tuple):
    i, size = data
    return [formula(i, j) for j in range(1, size + 1)]


def multiprocessing_create_matrix(size: int):
    pool = Pool(5)
    return pool.map(create_row, [(i, size) for i in range(1, size + 1)])


if __name__ == '__main__':
    st_time = time.time()
    sync_create_matrix(5000)
    print(f'Время одноядерного: {time.time() - st_time}')
    st_time = time.time()
    multiprocessing_create_matrix(5000)
    print(f'Время многоядерного: {time.time() - st_time}')
