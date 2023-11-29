from multiprocessing import Process
import time

def my_function1():
    print("We are doing a thing")
    time.sleep(2)
    print("We are doing something later")

def my_function2():
    print("No sleep until the end")
    print("Resist the sleep")
    time.sleep(1)

if __name__ == "__main__":
    process_1 = Process(target=my_function1)
    process_2 = Process(target=my_function2)
    process_1.start()
    process_2.start()
    print("End of main")
