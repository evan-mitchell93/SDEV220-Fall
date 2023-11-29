from multiprocessing import Process
import time

def f1(*args):
    print(f"We are doing something {args}")
    time.sleep(2)
    print("We are doing something later")

def f2():
    print("No sleep until the end")
    print("Resist the sleep")
    time.sleep(3)

if __name__ == "__main__":
    process_1 = Process(target=f1,args=("Evan","Bob"))
    process_2 = Process(target=f2)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()
    print("End of Main")