from tkinter import *
from tkinter import ttk
import winsound

no = 0

root = Tk()
root.title("Video To FFv1_Flac Converter")
root.geometry("380x400")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def inc_No():
    global no
    no = no + 1
    winsound.PlaySound('SystemDefault', winsound.MB_OK)
    print(no)
    


ttk.Button(mainframe, text="5.Convert", command=inc_No).grid(column=2, row=5,pady=10)

root.mainloop()
