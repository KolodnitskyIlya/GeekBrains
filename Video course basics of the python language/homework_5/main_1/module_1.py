import os

def create_dir():
    for i in range(1, 10):
        os.mkdir(f'dir-{i}')

def delete_dir():
    for i in range(1, 10):
        os.rmdir(f'dir-{i}')