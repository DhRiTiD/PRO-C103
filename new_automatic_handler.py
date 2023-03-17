# a project that foucuses on observing the events inside the 'downloads' folder and moving any downloaded items there to the Desktop

# watchdog package's Observer class for observing any changes
# watchdog package's FileSystemEventHandler to handle any moving process

import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Dell/Downloads"              # Add the path of you "Downloads" folder.
to_dir = "C:/Users/Dell/OneDrive/Desktop" #Create "Document_Files" folder in your Desktop and update the path accordingly.


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Handler Class

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
        print(name, extension)
        
        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path) # returns the file name with ext
                
                print("Downloaded " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Directory Exists...")
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True) # which event, from where(path), repeat itself

# Start the Observer
observer.start()

#to handle runtime exceptions | to stop observer
try:
    while True:
        time.sleep(2)
        print("running...", end ='\r')
        print('.')
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
