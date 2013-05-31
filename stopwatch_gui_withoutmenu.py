##STOPWATCH 1.0
##
##CREATED BY SIDDHARTH KANNAN
##
##WRITTEN ON PYTHON 2.7 AND TKINTER 8.5
##
##OS:LINUX MINT 14


##     This program is free software. It comes without any warranty, to
##     the extent permitted by applicable law. You can redistribute it
##     and/or modify it under the terms of the Do What The Fuck You Want
##     To Public License, Version 2, as published by Sam Hocevar. See
##     http://www.wtfpl.net/ for more details.



from Tkinter  import *
from time import *
from tkFont import *
import tkMessageBox
import datetime
now = datetime.datetime.now()

FRAME_WIDTH,FRAME_HEIGHT = 600,700    

class stopwatch(object):
    def __init__(self):
        self.window = Tk()  ##The main window instance
        self.window.title("STOPWATCH")

        ##Some fonts for use inside
        self.small = Font(family='Helvetica',size=11)
        self.medium = Font(family='Helvetica',size=15)
        #self.big = Font(family='Helvetica',size=24)
        
        self.initFrame()        

    def initFrame(self):
        self.frame = Frame(self.window,width=FRAME_WIDTH,height=FRAME_HEIGHT)  ##The frame instance
        self.frame.pack_propagate(0)  ##Making sure that the window does not shrink
        
        self.frame.pack(fill=None)
        self.initVariables()
        self.initBindings()
        self.initUI()

    def initVariables(self,event=None):

        ##VARIABLES:
        
        self.start = None
        self.stop = None
        self.timeConsumed = None
        self.laps = []
        self.startOfLap = None
        self.endOfLap = None
        self.counterOfLaps = 1

    def initBindings(self,event=None):

        w = self.window

        w.bind('s',self.startrunning)
        w.bind('e',self.stoprunning)
        w.bind('r',self.reset)
        w.bind('l',self.endlap)
        w.bind('<Escape>',self.quitwin)
        
    def initUI(self):

        f = self.frame

        info = Message(f,text="You can use the buttons below or \
you can use the following keyboard shortcuts to work with the stopwatch\
                            \n\nPress \'s\' to start running. \
                            \nPress \'e\' to stop running. \
                            \nPress \'r\' to reset the stopwatch. \
                            \nPress \'l\' to end a lap. \
                            \n\nPress escape button to quit this stopwatch\
                            Please note that all the times generated are \
                            being stored in a file \'timings.txt\' from \
                            which you can see the timings later.\n",\
                            font=self.medium)
        info.pack()        

        start = Button(f,text='START',command=self.startrunning)
        start.pack(side="top")

        stop =Button(f,text='STOP',command=self.stoprunning)
        stop.pack(side="top")

        lap = Button(f,text='LAP',command=self.endlap)
        lap.pack(side='top')

        reset = Button(f,text="RESET",command = self.reset)
        reset.pack(side="top")

        close = Button(f,text="QUIT",bg="black",fg = "red",command=self.quitwin)
        close.pack(side="top")

        ##Changing the font to increase the size of the buttons

        buttons = [start,stop,close,reset,lap]

        for i in buttons:
            i.config(font=self.medium)

    def startrunning(self,event=None):

        self.reset()            
        r = Frame(self.frame)
        r.pack()
        self.start = time()
        self.startOfLap = time()

        start = Label(r,text="\nStarted running")
        start.pack()
        

    def stoprunning(self,event=None):
        
        r = Frame(self.frame)
        r.pack()
        self.stop = time()
        self.timeConsumed = self.stop - self.start

        Label(r,text='\nstopped running').pack()
        end = Label(r,text="\nTime consumed is: %0.2f seconds" %self.timeConsumed)
        end.pack(side = "bottom")

        tkMessageBox.showinfo('Summary of this run','The run was completed in %0.2f seconds' %self.timeConsumed)

        self.writeDataToFile()
        self.initVariables()

    def writeDataToFile(self,event=None):

        inputFile = open('timings.txt','a')

        for i in range(60):
            inputFile.write('-')

        dateNow = 'Date:' + str(now.day) + '-' + str(now.month) + '-' \
                  + str(now.year) \
                  + ', ' + 'Time:' + str(now.hour) + ':' + str(now.minute) \
                  + ':' + str(now.second)

        inputFile.write('\n\n' + dateNow + '\n\n')

        for i in range(len(self.laps)):
            inputFile.write('Lap ' + str(i+1) + ': ' + str('%0.2f' %self.laps[i]) + ' seconds\n')

        if len(self.laps) == 0:
            inputFile.write('No laps recorded')

        inputFile.write('\nSummary of this run:'+str(' %0.2f' %self.timeConsumed) + ' seconds' + '\n')

    def reset(self,event=None):
        self.frame.destroy()

        self.initFrame()

    def endlap(self,event=None):
        self.endOfLap = time()
        timeTakenForOneLap = self.endOfLap - self.startOfLap

        self.laps.append(timeTakenForOneLap)

        r = Label(self.frame,text="Lap " + str(self.counterOfLaps) +" was completed in %0.2f" %timeTakenForOneLap)
        r.pack()
        self.counterOfLaps += 1

        self.startOfLap = time()

        if self.counterOfLaps % 9 == 0:
            self.frame.pack_propagate(1)

    def quitwin(self,event=None):

        self.window.destroy()

        self.window = Tk()
        self.window.title('License and Credits')
        
        self.frame =Frame(self.window)
        self.frame.pack()

        r = Frame(self.frame)
        r.pack()

        self.big = Font(family='Helvetica',size=24)

        m = Message(r,text="Created by Siddharth Kannan\
                          \nWritten on Python 2.7 and Tkinter 8.5\
                          \nOS: Linux Mint 14\
                          \nThis software is licensed under the WTFPL license.\
                          \nSee the copying file for more details.\
                          \nPress the quit button below to quit the application\
                          ",font=self.big)

        m.pack()

        b = Button(r,text='QUIT',fg='red',bg='black',command=self.window.destroy,font=self.big)
        b.pack(side='bottom')  
		

stopwatch()
mainloop()
