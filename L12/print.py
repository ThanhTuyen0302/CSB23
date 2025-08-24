import queue
import time
import threading
import sys
sys.stdout.reconfigure(encoding='utf-8')

# dung  thu vien queue
# class Printer: enqueue print job, dequeue print job
class Printer:
    def __init__(self):
        self.__print_list = queue.Queue()
        self.__pause_flag = threading.Event()
        self.__stop_flag = threading.Event()
        self.__worker = None
        
    def enqueue_print_job(self, job):
        self.print_list.put(job)
    
    def dequeue_print_job(self):
        if not self.__print_list.empty:
            return self.__print_list.get()
        return None
    
    #override 
    def __str__(self):
        print("---- Danh sach in ----")
        for index, value in enumerate(list(self.__print_list.queue)):
            print(f"{index}. {value}")
    
    # pause --------------
    def __print_worker(self):
        while not self.__stop_flag.is_set():
            if self.__pause_flag.is_set():
                time.sleep(0.2)
                continue
            job = self.dequeue_print_job()
            if job:
                print(f"Dang in tac vu: {job}")
                time.sleep(2)
            else:
                time.sleep(0.5) # cho job moi
        
    def start(self):
        self.__stop_flag.clear()
        self.__pause_flag.clear()
        self.__worker = threading.Thread(target=self.__print_worker, daemon=True)
        self.__worker.start()
        
    def pause(self):
        self.__pause_flag.set()
        print("|| May tam dung ...")
        
    def reusume(self):
        self.__pause_flag.clear()
        print("|> May in tiep tuc ...")
        
    def stop (self):
        self.__stop_flag.set()
        print("May in da dung!")
        
# demo/ test drive
if __name__ == "__main__":
    printer = Printer()
    printer.enqueue_print_job("Văn bản 1")
    printer.enqueue_print_job("Văn bản 2")
    printer.enqueue_print_job("Văn bản 3")

    printer.__str__()
    
    printer.start()
    
    # pause 3s -> resume
    time.sleep(3)
    printer.pause()
    time.sleep(4)
    printer.reusume()
    # chay them 4s -> dung
    time.sleep(4)
    printer.stop()
    