import threading
import time
from datetime import datetime

def read_file(file_path):
    time.sleep(3)
    with open(file_path, 'r') as file:
        data = file.read()
        print(f"Data read from {file_path}: {data}")


def main():
    file_path1 = 'data/data_1.txt'
    file_path2 = 'data/data_2.txt'
    file_path3 = 'data/data_3.txt'
    file_path4 = 'data/data_4.txt'
    file_path5 = 'data/data_5.txt'
    file_path6 = 'data/data_6.txt'
    file_path7 = 'data/data_7.txt'
    file_path8 = 'data/data_8.txt'


#Create threads
    thread1 = threading.Thread(target=read_file, args=(file_path1,))
    thread2 = threading.Thread(target=read_file, args=(file_path2,))
    thread3 = threading.Thread(target=read_file, args=(file_path3,))
    thread4 = threading.Thread(target=read_file, args=(file_path4,))
    thread5 = threading.Thread(target=read_file, args=(file_path5,))
    thread6 = threading.Thread(target=read_file, args=(file_path6,))
    thread7 = threading.Thread(target=read_file, args=(file_path7,))
    thread8 = threading.Thread(target=read_file, args=(file_path8,))


#Start threads

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()

#Wait for both threads to finish

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()


print("Main thread continues execution")





if __name__ == "__main__" :
    print(datetime.now())
    main()
    print(datetime.now())

#Xulosa:Shunday qilib, multiprocessing va threading o'rtasidagi tanlov aniq vazifaga bog'liq. Agar vazifalar ko'p sonli hisob-kitoblarni talab qilsa va mustaqil ravishda bajarilishi mumkin bo'lsa, unda multiprocessing tanlash yaxshidir.
# Agar topshiriqlar asosan kiritish-chiqarish bilan bog'liq bo'lsa va resurslarga umumiy kirishni talab qilsa, u holda multithreading ishlatish yaxshiroqdir.