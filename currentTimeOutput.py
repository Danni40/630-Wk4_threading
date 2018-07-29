import time
import threading

def current_time():  #simple function to output the current time in popular format
    #time.sleep(0.5) commented out in order to output instantly
    print("The current time is:",time.strftime("{0}:{1}:{2} {3}".format("%I", "%M", "%S", "%p")))

def military_time():#simple function to output the current time in 24 hour or 'military' format
    time.sleep(0.5)  #wait a half second to ouput
    print("The current time in military time is:",time.strftime("{0}{1}{2}".format("%H", "%M", "%S")))
    
def current_date_time(): #simple function to output the current time with the date in popular format
    time.sleep(1.0) #wait a second to ouput
    print("The current date and time is:",time.strftime("{0} {1} {2} - {3}:{4}:{5} {6}".format("%m", "%d", "%Y", "%I", "%M", "%S", "%p")))
    
if __name__ =="__main__":
    #setup the threading of the functions
    t1 = threading.Thread(target=current_time, args=())  
    t2 = threading.Thread(target=military_time, args=())
    t3 = threading.Thread(target=current_date_time, args=())
    
    #start the functions
    t1.start()
    t2.start()
    t3.start()
    
    #join the functions back to the main function once they have all completed
    t1.join()
    t2.join()
    t3.join()
    
    #Lets time the entire process
    t = time.time()
    #display the time it took to complete
    print("Done in", t)
    