import os
import time
def main():
    start = int(input('Folder numbers start from : '))
    number = 0
    number += start
    print(f'Starting from {number}')
    
    path = input('Path : ')
    print(f'Changed path to {path}')
    os.chdir(path)
    
    file_format = input('Enter the file format : ')
    form = f'.{file_format}'
    print(f'File format has been set to {file_format}.')
    
    time.sleep(1.5)
    for x in os.listdir():
        number += 1
        os.rename(x,str(number) + form)
        print(x)

while True:
    main()
