import os
import sys
import numpy as np
import psychopy.visual
import psychopy.event
import psychopy.gui
from psychopy import core, monitors

# Getting subject's information
# ID and Initials

#gui = psychopy.gui.Dlg()
#gui.addField("Subject ID:")
#gui.addField("Subject Initials:")
#gui.show()

# store data from gui prompt in variables
# sub id has subject's id number
# sub initials has initials 

# sub_id = gui.data[0]
# sub_initials = gui.data[1]
scnWidth, scnHeight = (1920, 1080)
mon = monitors.Monitor('Acer', width=58.0, distance=70.0)
mon.setSizePix((scnWidth, scnHeight))
mon.save()
# win = visual.Window((scnWidth, scnHeight), fullscr=True, monitor=mon, color=[0,0,0], units='pix', allowStencil=True,autoLog=False)


dsgn1 = np.empty((0,2), int)
dsgn2 = np.empty((0,2), int)
dsgn3 = np.empty((0,2), int)

shape = np.array([1,2]) # 1 is circle, 2 is square
# order = np.array([1,2])
order = 1

for i in range(len(shape)):
    dsgn1 = np.append(dsgn1, [[shape[i],order]], axis = 0)
    dsgn2 = np.append(dsgn2, [[shape[i],order]], axis = 0)
    dsgn3 = np.append(dsgn3, [[shape[i],order]], axis = 0)
    # for j in range(len(order)):
        # dsgn = np.append(dsgn, [[shape[i],order[j]]], axis = 0)

dsgnmatrix = np.concatenate((dsgn1,dsgn2,dsgn3))
from numpy import random
np.random.shuffle(dsgnmatrix)
total_trials = dsgnmatrix.shape[0]
designOrder = np.linspace(1,total_trials,num=total_trials)
# keys = psychopy.event.waitKeys(keyList=["space"])

# open window 
win = psychopy.visual.Window(
    size=[400*2,400*2],
    units="pix",
    allowStencil=True,
    autoLog=False,
    fullscr=True,
    monitor=mon,
    color=[0, 0, 0],
    screen = 0,
)

# creating a fixation cross
fixation = psychopy.visual.ShapeStim(win, 
    vertices=((0, -0.5), (0, 0.5), (0,0), (-0.5,0), (0.5, 0)),
    lineWidth=20*2,
    closeShape=False,
    lineColor="black"
)

rect = psychopy.visual.Rect(
    win = win,
    units = "pix",
    width = 100*2,
    height = 100*2,
    fillColor = [1, 1, 1],
    lineColor = [-1,-1,-1]
 )
 
circle = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=60*2,
    fillColor=[1, 1, 1],
    lineColor=[-1, -1, -1],
    edges=128
)

ready = psychopy.visual.TextStim(win=win, text="Ready", color=[1,1,1])
set = psychopy.visual.TextStim(win=win, text="Set", color=[1,1,1])
go = psychopy.visual.TextStim(win=win, text="Go", color=[1,1,1])
spacebar_instruc = psychopy.visual.TextStim(win=win, text="Press spacebar to continue.", color=[1,1,1])


button = False
i = 0


while i < total_trials:
    trialDone = False 
    currentShape = dsgnmatrix[i,0]
    currentOrder = dsgnmatrix[i,1]
    if currentShape == 1 and currentOrder == 1:
        stim1 = circle 
        stim2 = rect
    elif currentShape == 2 and currentOrder == 1:
        stim1 = rect
        stim2 = circle
    print(currentShape,currentOrder)        
    while not trialDone: # ready, set, go 
           ready.draw()
           win.flip()
           core.wait(.5)
           set.draw()
           win.flip()
           core.wait(.5)
           go.draw()
           win.flip()
           core.wait(.5)
           #stimulus presentation
           stim1.draw()
           fixation.draw()
           win.flip()
           core.wait(1)
           stim2.draw()
           fixation.draw()
           win.flip()
           core.wait(1)
           win.flip() #clear window
           spacebar_instruc.draw()
           win.flip() #spacebar prompt
           psychopy.event.waitKeys(keyList=["space"])
           trialDone = True
    i+=1
win.close()

print(dsgnmatrix)
#print(key)

# fixation.pos = [10,0]

#from psychopy.tools.monitorunittools import posToPix
#posPix = posToPix(circle)

#from psychopy import monitors
#for mon in monitors.getAllMonitors():
#    print(win.monitor.name, win.monitor.getSizePix())

#print(posPix)







