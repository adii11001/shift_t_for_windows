import psutil
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "processes.txt")

processes_pids = psutil.pids()

restoration_focus = ["Spotify.exe", "chrome.exe", "Notepad.exe", "Code.exe", "WhatsApp.Root.exe"]
apps = set()
with open(file_path , "w+") as f:
    for i in psutil.pids():
        p = psutil.Process(i)
        if p.name() in restoration_focus:
            if p.name() not in apps:
                f.write(f'{p.name()}: {p.exe()}\n')
                apps.add(p.name())
