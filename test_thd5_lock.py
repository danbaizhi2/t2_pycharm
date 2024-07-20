import threading
import time

count = 0
l = threading.Lock()

def add():
    global count
    while count < 20:
        print(f",  {count}")
        count += 1

def add_(name, stop):
    l.acquire()
    global count
    while count < stop:
        print(f"{name},  <{count}>")
        count += 1
        time.sleep(0.2)
    l.release()

# add()
# add_('yi')
t1 = threading.Thread(target=add_, args=('t1', 6))
t2 = threading.Thread(target=add_, args=('t2', 20))
t3 = threading.Thread(target=add_, args=('t3', 40))
print('now start')

t1.start()
t2.start()
t3.start()

# t1.join()
t2.join()
print('end all')