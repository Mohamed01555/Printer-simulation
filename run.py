from Simulation import *

if __name__ == '__main__' :
    for i in range(20):
        printer_queue_size, average_waiting_time = Simulation(3600,5)
        print("Average Wait " , average_waiting_time ," secs" ,printer_queue_size , " tasks remaining")
        #print('#################################')
