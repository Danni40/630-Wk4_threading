import time
import threading

def current_time():
    #time.sleep(0.5)
    print("The current time is:",time.strftime("{0}:{1}:{2} {3}".format("%I", "%M", "%S", "%p")))

def military_time():
    time.sleep(0.5)
    print("The current time in military time is:",time.strftime("{0}{1}{2}".format("%H", "%M", "%S")))
    
def current_date_time():
    time.sleep(1.0)
    print("The current date and time is:",time.strftime("{0} {1} {2} - {3}:{4}:{5} {6}".format("%m", "%d", "%Y", "%I", "%M", "%S", "%p")))
    
if __name__ =="__main__":
    t1 = threading.Thread(target=current_time, args=())
    t2 = threading.Thread(target=military_time, args=())
    t3 = threading.Thread(target=current_date_time, args=())
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    t = time.time()
    print("Done in", t)
    