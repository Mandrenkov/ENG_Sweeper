# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# Input Module

import VarData
from graphics import *

# Return X and Y Coordinates of a Mouse Click
def GetMouseInput(window):
    inputClick = window.getMouse()
    return inputClick.getX(), inputClick.getY()

# Return the Tile Position from Game Window Coordinates
def GridClick(mouseX, mouseY):
    gridX = gridY = -1
    for x in range(17, 610, 40):
        for y in range(111, 500, 40):
            if x < mouseX < x + 40 and y < mouseY < y + 40:
                gridX = (x - 17)/40
                gridY = (y - 111)/40
                break
    return gridX, gridY

# Handle Difficulty Window Input
def CloseDiff():
    diffHeight = 360
    winWidth = VarData.diffWindow.getWidth()

    try:
        closeClick = Point(0,0)

        while (closeClick.getY() < diffHeight/4):
            closeClick = VarData.diffWindow.getMouse()

        closeClickY, closeClickX = closeClick.getY(), closeClick.getX()

        VarData.diffWindow.close()

        if diffHeight/4 <= closeClickY < diffHeight/4 + 3*diffHeight/16:
            return 0
        elif diffHeight/4 + 3*diffHeight/16 <= closeClickY < diffHeight/4 + 6*diffHeight/16:
            return 1
        elif diffHeight/4 + 6*diffHeight/16 <= closeClickY < diffHeight/4 + 9*diffHeight/16:
            return 2
        elif diffHeight/4 + 9*diffHeight/16 <= closeClickY < diffHeight/4 + 12*diffHeight/16:
            return 3
        elif closeClickX < winWidth/2:
            return 4
        else:
            return 5
    except GraphicsError:
        return None

# Handle End Window Input
def CloseEnd():
    diffHeight = VarData.endWindow.getHeight()

    try:
        closeClick = Point(0,0)

        while (closeClick.getY() < diffHeight/5 or closeClick.getX() > VarData.endWindow.getWidth()/3):
            closeClick = VarData.endWindow.getMouse()

        closeClick = closeClick.getY()

        VarData.endWindow.close()

        if diffHeight/5 <= closeClick < diffHeight/5*2:
            return 0
        elif diffHeight/5*2 <= closeClick < diffHeight/5*3:
            return 1
        elif diffHeight/5*3 <= closeClick < diffHeight/5*4:
            return 2
        else:
            return 3
        
    except GraphicsError:
        return None

# Handle "Main" Menu Window Input
def MenuClick():
    try:
        closeClick = Point(0,0)

        while (closeClick.getY() < 250 or closeClick.getX() > 300):
            closeClick = VarData.menuWindow.getMouse()

        if closeClick.getY() <= 325:
            VarData.menuWindow.close()
            return 0
        elif closeClick.getX() <= 120:
            VarData.menuWindow.close()
            return 1
        else:
            return 2
        
    except GraphicsError:
        return 1

# Handle Instructions Input
def InstructionsClick():
    try:
        width = VarData.menuWindow.getWidth()

        closeClick = Point(0,0)

        while closeClick.getY() < 350:
            closeClick = VarData.menuWindow.getMouse()

        if closeClick.getX() <= width/4:
            return 0
        elif closeClick.getX() <= width/2:
            return 1
        elif closeClick.getX() <= width/4*3:
            return 2
        else:
            return 3
    except GraphicsError:
        return 0

# Close a Given Window
def CloseWindow(window):
    try:
        window.close()
    except GraphicsError:
        print "Closing Window Error"
        pass