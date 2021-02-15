from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from subprocess import check_output
import winsound
# To get the filename
import os

root = Tk()
root.title("Normalization Helper")
root.geometry("380x400")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Ask native filename and use it in command as input. location = yourfile.name
# Wrap it with "" to get input with spaces
def getLocation():
    global inputFileLoc
    global scFileNo
    global inputFLSC
    global inputFLSCName
    inputFileLoc = filedialog.askopenfilename()
    # Badly named getting into only filename
    inputFLSC = os.path.basename(inputFileLoc)
    inputFLSCName = os.path.splitext(inputFLSC)[0]
    print(inputFileLoc)
    print(inputFLSC)
    #set scFileNo back to 0 so it will not go up endlessly
    scFileNo = 0
    
def getSaveTo():
    global saveFileLoc
    saveFileLoc = '"' + filedialog.askdirectory() + '"'
    print(saveFileLoc)

def getNormFileName():
    global timeGetter
    global normNameGet
    normNameGet = normFileN.get()
    timeGetter = timeBar.get()
    print(normNameGet)
    print(timeGetter)

normalize = '' # for use to test scrit
# Screen Capture file number. To make multiple screenshots without overwriting.
scFileNo = 0

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
    report = ' 2> '
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
        saveLog = report + inputFileLoc + '_LOG.txt'
    else:
        saveLog = noReport

# Start the with inputs from getLocation, getSaveTo and logToFile.
def convertStartVideo():
    saveFileName = normNameGet + '.mkv'# use as saveas for now. '' + "_FFV1_FLAC" NEEDS A FILETYPE
    ffToMkv = "ffmpeg -i "+ '"' + inputFileLoc + '"' + codecVideo + codecAudio + saveFileLoc + '/' + saveFileName + saveLog
    normalize = check_output(ffToMkv, shell=True, universal_newlines=True)
    print(normalize)
    print("DONE!")
    winsound.PlaySound('SystemDefault', winsound.MB_OK)
# FINISH THIS!!! Command for screen capture while loop for not overwriting the same imagefile over and over
def startScreenCap():
    global scFileNo
    scFileNo = scFileNo + 1
    # If name is entered use that if not use original filename
    if normNameGet != '':
        scFileName = normNameGet + "_" + str(scFileNo)
    else:
        scFileName = inputFLSCName + "_" + str(scFileNo)
    fileEnding = ".png"
    startSC  = "ffmpeg -i " + '"' + inputFileLoc + '"' + " -ss " + timeGetter + " -frames 1 " + saveFileLoc + "/" + scFileName + fileEnding
    takesnap = check_output(startSC, shell=True, universal_newlines=True)
    print(takesnap)
    print("DONE!")
    winsound.PlaySound('SystemDefault', winsound.MB_OK)

#Videoconversion buttons
ttk.Button(mainframe, text="1.Choose Input", command=getLocation).grid(column=1, row=1)
ttk.Button(mainframe, text="3.Confirm Name", command=getNormFileName).grid(column=2, row=2)
ttk.Button(mainframe, text="2.Choose Output", command=getSaveTo).grid(column=3, row=1)
ttk.Button(mainframe, text="5.Convert", command=convertStartVideo).grid(column=2, row=5,pady=10)

# 3 Entries for HH:MM:SS
tvalue = StringVar(mainframe, value="00:00:00")
timeBar = ttk.Entry(mainframe, width=7, textvariable=tvalue)
timeBar.grid(column=2, row=9, padx=20,pady=10)
#Video Screen capture buttons
#Input, Outputloc, Output=inputname+Screen_Capture+%0.d.png have default time be 00:00:00 if else
ttk.Button(mainframe, text="3.Confirm Time", command=getNormFileName).grid(column=2, row=10, pady=10)
ttk.Button(mainframe, text="5.Screen Capture", command=startScreenCap).grid(column=2, row=11, pady=20)

#Check button for audio or video conversion
ttk.Checkbutton(mainframe,text='4.Video Codec', variable=checkB1, onvalue=1, offvalue=0,command=getCodecs).grid(column=3, row=4, sticky=W)
ttk.Checkbutton(mainframe,text='4.Audio Codec', variable=checkB2, onvalue=1, offvalue=0,command=getCodecs).grid(column=3, row=5, sticky=W)
ttk.Checkbutton(mainframe,text='4.Enable Log', variable=checkB3, onvalue=1, offvalue=0,command=getCodecs).grid(column=3, row=6, sticky=W)

#Text entry widget for setting normalized filename
normFileN = ttk.Entry(mainframe)
normFileN.grid(column=2, row=1, padx=20,pady=20)

def exitProgram():
    root.destroy()
    pass

ttk.Button(mainframe, text="Exit", command=exitProgram).grid(column=2, row=15, sticky=S, pady=10)


root.mainloop()
