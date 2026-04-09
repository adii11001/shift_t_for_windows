import subprocess # os.system can be used but it is blocks the script until a command returns unlike subprocess.Popen
import re
import psutil
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "processes.txt")

restoration_focus = ["Spotify.exe", "chrome.exe", "Notepad.exe", "Code.exe", "WhatsApp.Root.exe"]
open_apps = set()

for i in psutil.pids():
    p = psutil.Process(i)
    if p.name() in restoration_focus:
        if p.name() not in open_apps:
            open_apps.add(p.name())

with open(file_path, "r") as f:
    for i in f:
        app = re.split(": ", i)
        file_path = app[1][:-1]
        print(app[0])
        if app[0] not in open_apps:
            if app[0] == "chrome.exe":
                subprocess.Popen([file_path, '--restore-last-session'])
            elif app[0] == "Spotify.exe":
                subprocess.Popen(['spotify'])
            elif app[0] == "WhatsApp.Root.exe":
                subprocess.Popen(f'"{file_path}"', shell=True)
            else:
                subprocess.Popen([file_path])
                      