import multiprocessing as mp
import time

def counter(num):
    count = 0
    while count < num:
        count += num
        
def main():
    a = mp.Process(target=counter, args=(25_000_000,))
    b = mp.Process(target=counter, args=(25_000_000,))
    c = mp.Process(target=counter, args=(25_000_000,))
    d = mp.Process(target=counter, args=(25_000_000,))
    
    a.start()
    b.start()
    c.start()
    d.start()
    
    a.join()
    b.join()
    c.join()
    d.join()
    
    print(time.time_count())
        
if __name__ == '__main__':
    main()