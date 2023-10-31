import psutil

def get_running_processes():
    """
    Retrieve details of all running processes.
    Returns:
        list: List of dictionaries containing details of each running process.
    """
    return [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]

def kill_process_by_name(process_name):
    """
    Terminate processes based on their name.
    
    Args:
        process_name (str): Name of the process to be terminated.
    """
    for p in psutil.process_iter(['pid', 'name', 'username']):
        if p.info['name'] == process_name:
            try:
                p.kill()
            except psutil.NoSuchProcess:
                continue

# Uncomment below lines to test the functions
processes = get_running_processes()
print(processes)
# kill_process_by_name('process_name_to_kill')
