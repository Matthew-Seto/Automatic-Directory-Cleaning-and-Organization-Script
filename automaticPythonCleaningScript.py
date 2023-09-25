import os
import shutil

DownloadsPath = "D:\\Downloads"

dir_list = os.listdir(DownloadsPath)
extensions = set()

for item in dir_list:
    paths = os.path.join(DownloadsPath,item)
    if (os.path.isfile(paths) == True):
        extensions.add(item.split(".")[-1])

for extension in extensions:
    if not (os.path.exists(os.path.join(DownloadsPath,extension))):
        os.mkdir(os.path.join(DownloadsPath,extension))

for item in dir_list:
    paths = os.path.join(DownloadsPath,item)
    if (os.path.isfile(paths) == True):
        filename = item.split(".")[-1]
        shutil.move(paths, os.path.join(DownloadsPath,filename))


# Clean up the desktop shortcuts
DesktopPath = "D:\\Desktop"

desktopListDir = os.listdir(DesktopPath)

shortcuts = {"lnk", "url"}

for item in desktopListDir:
    if (os.path.isfile(os.path.join(DesktopPath,item)) == True):
        if (item.split(".")[-1] in shortcuts):
            os.remove(os.path.join(DesktopPath,item))