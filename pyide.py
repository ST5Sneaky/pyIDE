import tkinter as tk
import pymsgbox as pmb
import os

frame = tk.Tk()
frame.title("PyIDE")

def saveFile():
    directory = pmb.prompt("Please enter a directory/filename to save to.", "Save where?")
    with open(directory, "w") as file:
        coded = code.get("1.0", "end-1c")
        file.write(coded)

def loadFile():
    loaddir = pmb.prompt("Please enter the directory/filename of the file.", "Load which file?")
    with open(loaddir, "r") as file:
        lines = file.readlines()
        lc = 0
        for line in lines:
            lc += 1
            code.insert(str(lc) + ".0", line)

def start():
    rundir = pmb.prompt("Please enter the directory/filename of the file to run.", "Run which file?")
    os.system("start " + rundir) 
  
code = tk.Text(height = 12, width = 35)
code.pack()
  
save = tk.Button(frame, text = "Save", command = saveFile)
save.pack()

load = tk.Button(frame, text = "Load", command = loadFile)
load.pack()

run = tk.Button(frame, text = "Run", command = start)
run.pack()
                        
frame.mainloop()
