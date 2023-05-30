import threading as thr
import time

def x():
    time.sleep(5)
    print("x")
    
def y():
    while True:
        time.sleep(1)
        print("y")

x_t = thr.Thread(target=x)
x_t.start()

y_t = thr.Thread(target=y, daemon=True)
y_t.start()

time.sleep(2)
print("Why?")