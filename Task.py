import random
class Task:
    def __init__(self,time):
        self.time_stamp = time
        self.pages = random.randrange(1,21)

    def getpages(self):
        return self.pages

    def getstamp(self):
        return self.time_stamp

    def wait_time(self,current_time):
        return current_time - self.time_stamp
    
