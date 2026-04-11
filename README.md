# 🔄 Shift+T for Windows

Shift+T restores the last session in chrome so does this program in windows.

It restores previously running apps like:

* Spotify
* WhatsApp
* Notepad
* VS Code

Feel free to add your application of choice.

---

## Requirements

* `psutil` → process detection
* `subprocess` → non-blocking execution
* `os` → path handling
* `re` → parsing (thought it was cool)


---

## How to Use

1. Open task scheduler
2. Click create basic task
3. Add name and description (optional)
4. Trigger shall be "When I log on"
5. Action "Start a program"
6. Program/script: add pythonw.exe [To not open console window while executing]; Add arguments: "path_to_extractor.py"
7. Search for the task in the task scheduler library right click, select properties.
8. Go to the triggers pane and edit the trigger
9. Check Repeat task every and set it to 5 minutes and for a duration of shall be indefinitely
10. Create a shortcut for the opener.py file. Open properties set shortcut key.

## How It Works

* `extraction.py` runs every 5 minutes
* Saves active apps to `processes.txt`
* `opener.py` reads the file
* Launches apps that aren't running


Voila! You have setup Shift T for windows! Is it needed? no! Is it cool? Hell yeah! 
