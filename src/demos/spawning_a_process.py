from multiprocessing import Process, current_process

def repeat_message(message : str, times : int) -> None :
    
    p = current_process()

    for _ in range(times):
        print(f'Process {p.pid}: {message}')
        
if __name__ == '__main__' :
    
    ''' 
        target : the code to run in a child process
        args   : arguments to pass to the target
        daemon : kill the process if the parent process dies
    '''
    my_process = Process(
        target = repeat_message, 
        args   = ('hello from a subprocess', 3),
        daemon = True
    )
    
    my_process.start()
    my_process.join()
    
    