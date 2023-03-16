#
import os
import shutil
import time

#watchdog - package, observers- module, Observer - class
from watchdog.observers import Observer #observe any changes in the given path
from watchdog.events import FileSystemEventHandler 

from_dir ="C:/Users/Dell/Downloads"

print('Hi there! I\'m your personal event tracker. I will track any changes at the location: ', from_dir, 'and let you know without delay')
print(input('ARE YOU READY?'))


class FileSystemEventTracker(FileSystemEventHandler):
    def on_created(self, event):
        print('Hey! New file was downloaded at: ', event.src_path)
    def on_deleted(self, event):
        print('Oh No! file at:', event.src_path, 'was deleted!' )
    def on_modified(self, event):
        print('Just to let you know.. the file:', event.src_path, 'was modified.')
    def on_moved(self, event):
        print('I see that the file: ', event.src_path, 'was moved to a diffrent loacation')
    def on_opened(self, event):
        print('You opened: ', event.src_path)
    

# Initialize Event Handler Class
event_tracker = FileSystemEventTracker()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_tracker, from_dir, recursive=True) # which event, from where(path), repeat itself

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...") 
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
