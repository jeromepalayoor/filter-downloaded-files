import watchdog.observers
import watchdog.events
import shutil
import os
import time

watchpath = "<FOLDER NAME>"

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self,ignore_patterns=['*.tmp'],ignore_directories=False,case_sensitive=True)

    def on_created(self,event):
        if not event.is_directory:
            time.sleep(10)
            try:
                endpoint = event.src_path.rindex('.')
                end = event.src_path[endpoint+1:]
                namepoint = event.src_path.rindex('\\')
                name = event.src_path[namepoint+1:]
                path = watchpath + '\\folders\\' + end + ' files\\'
                if not os.path.exists(path):
                    os.makedirs(path)
                shutil.move(event.src_path,path + name)
            except:
                pass

    def on_deleted(self,event):
        pass

event_handler = Handler()
observer = watchdog.observers.Observer()
observer.schedule(event_handler,watchpath,recursive=False)
observer.start()
observer.join()
