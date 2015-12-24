# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# Menu Module

from graphics import *
from math import cos, sin, pi

import VarData
import Input, OpeningScreen, Difficulty, Instructions, Game

# Manual Constructor
def MenuMain(displayOpeningScreen, newWindow):
    if newWindow:
        VarData.menuWindow = GraphWin("ENG Sweeper",600,400)
        VarData.menuWindow.setBackground("white")

    try:
        if OpeningScreen.OpeningScreenMain(displayOpeningScreen):
            return None

        TranslateScreen(displayOpeningScreen)
    
        DisplayMenu(displayOpeningScreen)

        OpeningScreen.WhiteBorder()
        
    except GraphicsError:
        return None

    uInput = Input.MenuClick()

    if uInput == 0:
        VarData.difficulty = Difficulty.DifficultyMain()

        if VarData.difficulty != None:
            Game.MainGame(True)
    elif uInput == 2:
        Instructions.InstructionsMain()

# Call to Draw Menu Lines and Labels
def DisplayMenu(displayOpeningScreen):
    DrawBars(displayOpeningScreen)
    DrawButtonLabels(displayOpeningScreen)

# Return Current High Score Saved in File
def FindHS():
    try: # HS File Exists
        hsFile = open("HS.txt", "r")
        hsFileText = hsFile.read()
        hsFile.close()

        if len(hsFileText) != 36:
            raise ValueError

        hs = hsFileText[6:-10]

        hsHalfByte = []

        for strIndex in range(0, 20, 4):
            hsHalfByte.append(hs[strIndex:strIndex + 4])

        hsList = []

        for hsDigit in range(5):
            curDigit = 0
            for hsBit in range(4):
                curDigit += eval(hsHalfByte[hsDigit][hsBit]) * 2**(3-hsBit)
            if curDigit > 9:
                raise ValueError
            hsList.append(str(curDigit))

        oldHSstr = ""
        oldHSstr = oldHSstr.join(hsList)
        return oldHSstr.rjust(5,'0')

    except: # No HS file exists / Error occurred while reading the file
        return "00000"

# Adjust Window Components to Post-Opening Position
def TranslateScreen(displayOpeningScreen):
    coverDevName = Rectangle(Point(430, 370),Point(597, 397))
    alphaClr = 170
    alpha = color_rgb(alphaClr,alphaClr,alphaClr)
    coverDevName.setFill(alpha)
    coverDevName.setOutline(alpha)
    coverDevName.draw(VarData.menuWindow)

    if not(displayOpeningScreen):
        coverContRect = Rectangle(Point(0, 330),Point(250, 400))
        coverContRect.setFill("white")
        coverContRect.setOutline("white")
        coverContRect.draw(VarData.menuWindow)

        VarData.oENG.move(0,-50)
        VarData.oSweeper.move(0,-50)
        VarData.oMsg1.move(0,-50)
        VarData.oMsg2.move(0,-50)

        VarData.oBotKoch.move(50,0)

        VarData.oENG.draw(VarData.menuWindow)
        VarData.oSweeper.draw(VarData.menuWindow)
        VarData.oMsg1.draw(VarData.menuWindow)
        VarData.oMsg2.draw(VarData.menuWindow)
        VarData.oBotRect.draw(VarData.menuWindow)
        VarData.oBotKoch.draw(VarData.menuWindow)
        return None

    for adj in range(50):
        VarData.oENG.move(0,-1)
        VarData.oSweeper.move(0,-1)
        VarData.oMsg1.move(0,-1)
        VarData.oMsg2.move(0,-1)

        VarData.oBotKoch.move(1,0)

        coverContRect = Rectangle(Point(250 - 5 *adj, 330),Point(250, 400))
        coverContRect.setFill("white")
        coverContRect.setOutline("white")
        coverContRect.draw(VarData.menuWindow)

# Draw Window Lines
def DrawBars(displayOpeningScreen):
    barClr = 200

    if not(displayOpeningScreen):
        horizBarA = Line(Point(10, 325),Point(300, 325))
        horizBarA.setFill(color_rgb(barClr, barClr, barClr))
        horizBarA.draw(VarData.menuWindow)

        horizBarB = Line(Point(10, 250),Point(300, 250))
        horizBarB.setFill(color_rgb(barClr, barClr, barClr))
        horizBarB.draw(VarData.menuWindow)

        vertBar = Line(Point(120, 325),Point(120, 400))
        vertBar.setFill(color_rgb(barClr, barClr, barClr))
        vertBar.draw(VarData.menuWindow)

        return None

    # Draw Horizontal Bars
    for xCoord in range(10, 300):
        VarData.menuWindow.plot(xCoord, 325, color_rgb(barClr, barClr, barClr))
        VarData.menuWindow.plot(xCoord, 250, color_rgb(barClr, barClr, barClr))

    # Draw Verical Bar
    for yCoord in range(400, 325, -1):
        VarData.menuWindow.plot(120, yCoord, color_rgb(barClr, barClr, barClr))

# Draw Tri-Button Text and Lines
def DrawButtonLabels(displayOpeningScreen):
    DiffSelLabel = Text(Point(150, 287), "Play ()")
    DiffSelLabel.setFace("times roman")
    DiffSelLabel.setStyle("normal")
    DiffSelLabel.setSize(16)
    
    QuitLabel = Text(Point(60, 365), "Quit")
    QuitLabel.setFace("times roman")
    QuitLabel.setStyle("normal")
    QuitLabel.setSize(16)
    
    instructLabel = Text(Point(210, 365), "Instructions")
    instructLabel.setFace("times roman")
    instructLabel.setStyle("normal")
    instructLabel.setSize(16)
    
    # Not technically a button label
    currentHS = Text(Point(565, 387), FindHS())
    currentHS.setFace("times roman")
    currentHS.setStyle("normal")
    currentHS.setSize(16)

    if not(displayOpeningScreen):
        DiffSelLabel.setTextColor(color_rgb(120,120,120))
        QuitLabel.setTextColor(color_rgb(120,120,120))
        instructLabel.setTextColor(color_rgb(120,120,120))
        currentHS.setTextColor("white")
    else:
        DiffSelLabel.setTextColor("white")
        QuitLabel.setTextColor("white")
        instructLabel.setTextColor("white")
        currentHS.setTextColor(color_rgb(170,170,170))

    DiffSelLabel.draw(VarData.menuWindow)
    QuitLabel.draw(VarData.menuWindow)
    instructLabel.draw(VarData.menuWindow)
    currentHS.draw(VarData.menuWindow)

    if not(displayOpeningScreen):
        return None

    for alpha in range(255, 120, -1):
        DiffSelLabel.setTextColor(color_rgb(alpha,alpha,alpha))
        QuitLabel.setTextColor(color_rgb(alpha,alpha,alpha))
        instructLabel.setTextColor(color_rgb(alpha,alpha,alpha))

        hsAlpha = 255 - alpha + 120

        if hsAlpha > 170:
            currentHS.setTextColor(color_rgb(hsAlpha,hsAlpha,hsAlpha))

# Transition Window Sweep
def ClearWindow(toTheRight):
    rectWidth = 10
    if toTheRight:
        for xCoord in range(0, VarData.menuWindow.getWidth(), rectWidth):
            clearRect = Rectangle(Point(xCoord,0),Point(xCoord + rectWidth,VarData.menuWindow.getHeight()))
            clearRect.setFill("white")
            clearRect.setOutline("white")
            clearRect.draw(VarData.menuWindow)
    else:
        for xCoord in range(VarData.menuWindow.getWidth(), 0, -rectWidth):
            clearRect = Rectangle(Point(xCoord-rectWidth,0),Point(xCoord,VarData.menuWindow.getHeight()))
            clearRect.setFill("white")
            clearRect.setOutline("white")
            clearRect.draw(VarData.menuWindow)