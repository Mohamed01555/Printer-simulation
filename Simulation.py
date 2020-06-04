from Printer import *
from Queue import *
from Task import *
import random

def Simulation(nom_of_seconds, pages_per_minute):
    labprinter = Printer(pages_per_minute)
    waiting_times = []
    printer_queue = Queue()

    for current_second in range(nom_of_seconds):
        if random.randrange(1,91) == 5:  #91 if there are 20 students on avg, 181 if 10 only
            task = Task(current_second)
            printer_queue.enqueue(task)
            #print(current_second,task.getpages())

        if (not printer_queue.is_empty() and (not labprinter.busy())):
            
            new_task = printer_queue.dequeue()
            
            waiting_times.append(new_task.wait_time(current_second))
            
            labprinter.start_next(new_task)
            
            #print(new_task.wait_time(current_second))
            
        labprinter.tick()
        
    #print(waiting_times,'len is ',len(waiting_times))
    return printer_queue.size(), round(sum(waiting_times) / len(waiting_times),2)
