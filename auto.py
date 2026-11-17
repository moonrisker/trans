import os
import time
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 确保这里是你真实的文件夹路径
WATCH_FOLDER = r"C:\Users\kun\Pictures\Screenshots"

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        filename = event.src_path
        if filename.lower().endswith(('.png', '.bmp', '.webp', '.tif', '.tiff')):
            time.sleep(0.1)
            try:
                img = Image.open(filename).convert('RGB')
                new_name = os.path.splitext(filename)[0] + '.jpg'
                img.save(new_name, 'JPEG')
                img.close()
                os.remove(filename) 
            except Exception as e:
                pass

if __name__ == "__main__":
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()