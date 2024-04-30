from threading import Thread, current_thread

def repeat_message(message : str, times : int) -> None :
    
    t = current_thread()

    for _ in range(times):
        print(f'Thread {t.name}: {message}')
        
if __name__ == '__main__' :
    
    ''' 
        target : the code to run in a child process
        args   : arguments to pass to the target
        daemon : kill the process if the parent process dies
    '''
    my_thread = Thread(
        target = repeat_message, 
        args   = ('hello from a child thread', 3),
        daemon = True
    )
    
    my_thread.start()
    my_thread.join()
    
    