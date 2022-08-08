import os, shutil
 
dir = r"C:\Users\vbaptista\AppData\Local\Temp\\" 
for files in os.listdir(dir):
    path = os.path.join(dir, files)
    try:
        shutil.rmtree(path, ignore_errors=True)
    except OSError:
        os.remove(path)