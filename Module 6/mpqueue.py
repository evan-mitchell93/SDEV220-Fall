from multiprocessing import Process,Queue
import time

def f1(q):
    q.put("Hello from f1")

def f2(q):
    while q.empty():
        time.sleep(1)
    print(q.get(0))

if __name__ == "__main__":
    q = Queue()

    proccess_1 = Process(target=f1,args=(q,))
    process_2 = Process(target=f2,args=(q,))

    proccess_1.start()
    process_2.start()

    proccess_1.join()
    process_2.join()