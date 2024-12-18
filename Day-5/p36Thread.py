import time 
import threading
import os

id = os.getpid()
idd = os.getppid()

print(id, idd)

def f1():
    print('f1 thread is strated')
    for v in range(6):
        result = v+0
        #time.sleep(1)
    else:
        print(f'result: {result}')
    print("exit from f1 thread")
print('Main Thread')

obj = threading.Thread(target=f1)
print('B4 calling f1 thread')
#f1()

obj.start()#calling f1 block
#obj.join()
for v in range(5):
     time.sleep(1)
print("Exit from Main thread")