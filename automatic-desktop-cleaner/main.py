from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'hello':
                new_name = filename
                split_name = filename.split('.')
                file_exists = os.path.isfile(folder_destination + '/' + new_name)
                while file_exists:
                    i+=1
                    new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str(i) 
                    file_exists = os.path.isfile(folder_destination + '/' + new_name)



                src = folder_to_track + "/" + filename
                new_name = folder_destination + "/" + new_name
                os.rename(src, new_name)


folder_to_track = '/Users/promise/Desktop'
folder_destination = '/Users/promise/hello'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()