from Task import Task
class Printer:
    def __init__(self,pages):
        self.page_rate = pages
        self.current_task = None
        self.time_remaining = 0
        
    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None
                
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
        
    def start_next(self,newtask):
         self.current_task = newtask
         self.time_remaining = newtask.getpages() * 60/self.page_rate
                              

