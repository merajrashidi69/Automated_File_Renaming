import os
import time
def main():
    start = int(input('Folder numbers start from : '))
    number = 0
    number += start
    print('Starting from',number)

    path = input('Path : ')
    print('Changed path to',path)
    os.chdir(path)
    time.sleep(1.5)
    for x in os.listdir():
        number += 1
        os.rename(x,str(number) + '.mp4')
        print(x)

while True:
    main()
