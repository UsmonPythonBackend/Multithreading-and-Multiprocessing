import multiprocessing
import time
from datetime import datetime

def write_to_file(file_path: str, data: str) :
    time.sleep(2)
    with open(file_path, 'r+') as file:
        file.write(data)
        print(f"Data written t0 {file_path}\n")



def main():
    file_path1 = 'data/data_1.txt'
    file_path2 = 'data/data_2.txt'
    file_path3 = 'data/data_3.txt'
    file_path4 = 'data/data_4.txt'
    file_path5 = 'data/data_5.txt'
    file_path6 = 'data/data_6.txt'
    file_path7 = 'data/data_7.txt'
    file_path8 = 'data/data_8.txt'

    data1 = "Process1"
    data2 = "Process2"
    data3 = "Process3"
    data4 = "Process4"
    data5 = "Process5"
    data6 = "Process6"
    data7 = "Process7"
    data8 = "Process8"

# Create process
    process1 = multiprocessing.Process(target=write_to_file, args=(file_path1, data1))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_path2, data2))
    process3 = multiprocessing.Process(target=write_to_file, args=(file_path3, data3))
    process4 = multiprocessing.Process(target=write_to_file, args=(file_path4, data4))
    process5 = multiprocessing.Process(target=write_to_file, args=(file_path5, data5))
    process6 = multiprocessing.Process(target=write_to_file, args=(file_path6, data6))
    process7 = multiprocessing.Process(target=write_to_file, args=(file_path7, data7))
    process8 = multiprocessing.Process(target=write_to_file, args=(file_path8, data8))


#Start process
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()

#Wait for both process to finish
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()

    print("Main process continues execution.")

if __name__ == "__main__":
    print(datetime.now())
    main()
    print(datetime.now())

#Xulosa:Python-dagi multiprocessing moduli jarayonlarni yaratish va boshqarish imkonini beradi.
# Har bir bunday jarayon o'z xotira maydonida ishlaydi va o'zining Python interpritatoriga ega.
# Bu shuni anglatadiki, har bir jarayon mustaqil ishlashi mumkin va boshqa jarayonlarning bajarilishiga bog'liq emas.