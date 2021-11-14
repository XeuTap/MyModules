from multiprocessing import Process
import datetime


def mult(num):
    result = num
    start = datetime.datetime.now()
    for i in range(1, num):
        result += i
    end = datetime.datetime.now()
    # print(end-start)
    return result


proc1 = Process(target=mult, args=(10000000//2,))
proc2 = Process(target=mult, args=(10000000//2,))

if __name__ == '__main__':
    start = datetime.datetime.now()
    mult(10000000)
    end = datetime.datetime.now()
    print(end - start)

    start = datetime.datetime.now()
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()
    end = datetime.datetime.now()
    print(end-start)