from multiprocessing import Process, current_process
from threading import Thread, current_thread

class Printer:
    
    def __init__(self, name : str) -> None :
        self.name = name
    
    def __repr__(self) -> str :
        return f'Printer(name={self.name}, memory_address={id(self)})'

def use_printer(worker_name : str) -> None :
    global printer
    t = current_thread()
    print(f'\t{worker_name} (Thread Name: {t.name}) is using the printer')

def create_office() -> None :
    
    global printer
    
    print('-'*50)
    print('Opening Dunder Mifflin office in process', current_process().name)
    
    printer = Printer("Main Office Printer")

    print('\tThe office\'s printer:', printer)
    
    mike = Thread(target=use_printer, args = ('Michael Scott', ), daemon=True)
    pam = Thread(target=use_printer, args = ('Pam Beesly', ), daemon=True)

    mike.start()
    mike.join()
    
    pam.start()
    pam.join()
    print('-'*50, end='\n'*2)
    
    
if __name__ == '__main__' :
    
    print('Running the office in our main process')
    create_office()
    
    print('Running the office in a child process')
    other_office = Process(target=create_office, daemon=True)
    
    other_office.start()
    other_office.join()
    
    
    