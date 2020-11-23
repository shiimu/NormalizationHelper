from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from subprocess import check_output

root = Tk()
root.title("Video To FFv1_Flac Converter")
root.geometry("365x400")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Ask native filename and use it in command as input. location = yourfile.name
def getLocation():
    global inputFileLoc
    inputFileLoc = filedialog.askopenfilename()
    print(inputFileLoc)

def getSaveTo():
    global saveFileLoc
    saveFileLoc = filedialog.askdirectory()
    print(saveFileLoc)

def getNormFileName():
    global timeGetter
    global normNameGet
    normNameGet = normFileN.get()
    timeGetter = timeBar.get()
    print(normNameGet)
    print(timeGetter)

normalize = '' # for use to test scrit

#Checkbox widget
checkB1 = IntVar()
checkB2 = IntVar()
checkB3 = IntVar()
checkB4 = IntVar()
checkB1.get()
checkB2.get()
checkB2.get()

def getCodecs():
    print(checkB1.get())
    print(checkB2.get())
    print(checkB3.get())
    global video
    video = ' -c:v ffv1 -level 3 -g 1 -slicecrc 1 -context 1 '
    global noVideo
    noVideo = ' -vn '
    global audio
    audio = '-c:a flac '
    global noAudio
    noAudio = ' -an '
    global report
    report = ' -report'
    global noReport
    noReport = ''
    global codecVideo
    codecVideo = ''
    global codecAudio
    codecAudio = ''
    global saveLog
    saveLog = ''
    if checkB1.get() == 1:
        codecVideo = video
    else:
        codecVideo = noVideo
    if checkB2.get() == 1:
        codecAudio = audio
    else:
        codecAudio = noAudio
    if checkB3.get() == 1:
        saveLog = report
    else:
        saveLog = noReport

# Start the with inputs from getLocation, getSaveTo and logToFile.
def convertStartVideo():
    saveFileName = normNameGet + '.mkv'# use as saveas for now. '' + "_FFV1_FLAC" NEEDS A FILETYPE
    ffToMkv = "ffmpeg -i "+ inputFileLoc + codecVideo + codecAudio + saveFileLoc + '/' + saveFileName + saveLog
    normalize = check_output(ffToMkv, shell=True, universal_newlines=True)
    print(normalize)
    print("DONE!")
# FINISH THIS!!! Command for screen capture while loop for not overwriting the same imagefile over and over
def startScreenCap():
    fileEnding = ".png"
    startSC  = "ffmpeg -i " + inputFileLoc + " -ss " + timeGetter + " -frames 1 " + saveFileLoc + "/" + "Screen_Capture_%0d" + fileEnding
    takesnap = check_output(startSC, shell=True, universal_newlines=True)
    print(takesnap)
    print("DONE!")

#Videoconversion buttons
ttk.Button(mainframe, text="Choose Input", command=getLocation).grid(column=1, row=1)
ttk.Button(mainframe, text="Confirm Name", command=getNormFileName).grid(column=2, row=2)
ttk.Button(mainframe, text="Choose Output", command=getSaveTo).grid(column=3, row=1)
ttk.Button(mainframe, text="Convert", command=convertStartVideo).grid(column=2, row=5,pady=10)

# 3 Entries for HH:MM:SS
tvalue = StringVar(mainframe, value="00:00:00")
timeBar = ttk.Entry(mainframe, width=7, textvariable=tvalue)
timeBar.grid(column=2, row=9, padx=20,pady=20)
#Video Screen capture buttons
#Input, Outputloc, Output=inputname+Screen_Capture+%0.d.png have default time be 00:00:00 if else
ttk.Button(mainframe, text="Screen Capture", command=startScreenCap).grid(column=2, row=10,pady=10)

#Check button for audio or video conversion
ttk.Checkbutton(mainframe,text='Video Codec', variable=checkB1, onvalue=1, offvalue=0,command=getCodecs).grid(column=3, row=4, sticky=W)
ttk.Checkbutton(mainframe,text='Audio Codec', variable=checkB2, onvalue=1, offvalue=0,command=getCodecs).grid(column=3, row=5, sticky=W)
ttk.Checkbutton(mainframe,text='Enable Log', variable=checkB3, onvalue=1, offvalue=0,command=getCodecs).grid(column=3, row=6, sticky=W)

#Text entry widget for setting normalized filename
normFileN = ttk.Entry(mainframe)
normFileN.grid(column=2, row=1, padx=20,pady=20)

def exitProgram():
    root.destroy()
    pass

ttk.Button(mainframe, text="Exit", command=exitProgram).grid(column=2, row=15, sticky=S)


root.mainloop()
