import tkinter as tk
import pyautogui
import uuid

win = tk.Tk()
win.title("LoopGlitch Screenshoter")

def callback():
    try:
        filename = f"C:\Users\Ibarv\.vscode\screenshots_python\mySSpy_{uuid.uuid4()}.jpg"
        mySS = pyautogui.screenshot()
        mySS.save(filename)
    except Exception as e:
        print(f"Error al tomar la captura de pantalla: {e}")

button = tk.Button(win, text="Screenshot This!", command=callback)
button.grid(row=0, column=0, padx=10, pady=10) 

win.mainloop()