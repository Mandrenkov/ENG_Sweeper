# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# EndGame Module

from graphics import *

import VarData
import Input, Game, Difficulty, Menu
from math import e

# Manual constructor
def EndGameMain(finalGameState):
    VarData.endWindow = GraphWin("Game Summary", 350, 360)
    VarData.endWindow.setBackground("white")

    currentScore, newHS = HighScore()

    DrawTitle(finalGameState)
    DrawBars()
    DrawButtons()
    DrawText(currentScore, newHS)
    DrawCalcRatBox()

    userInput = Input.CloseEnd()

    if userInput == 0: # Call to Game with Present Difficulty
        Game.MainGame(True)
    elif userInput == 1: # Call to Difficulty Selection
        VarData.difficulty = Difficulty.DifficultyMain()
        if VarData.difficulty != None:
            Game.MainGame(True)
    elif userInput == 2: # Call to Main Menu
        Menu.MenuMain(False, True)

    # userInput = 4 -> Exit

# Read and Interpret High Score
def HighScore():
    # Secret "Calculus Ratiocinator" Calculation
    currentScore = int(5000. * e**(-VarData.gameTime/100.)) * 2 ** VarData.difficulty

    if VarData.safeTiles - VarData.tileCount != 0:
        currentScore = 0

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

        oldHS = eval(oldHSstr.lstrip("0"))

        if oldHS < currentScore:
            WriteScore(currentScore)
            VarData.currentHighScore = currentScore
            return currentScore, True
        else:
            VarData.currentHighScore = oldHS
            return currentScore, False
    except: # No HS file exists / HS file is corrupted
        WriteScore(currentScore)
        VarData.currentHighScore = currentScore
        return currentScore, True

# Write Current High Score to the HS File
def WriteScore(score):
    hsFile = open("HS.txt", "w")

    hsFile.write("101001")

    currentScoreStr = str(score).rjust(5, '0')
            
    for curDig in range(5):
        curHalfByte = str(bin(eval(currentScoreStr[curDig])))[2:].rjust(4,'0')
        hsFile.write(curHalfByte)

    hsFile.write("1010010001")

    hsFile.close()

# Draw Title of "End Game" Window
def DrawTitle(finalGameState):
    titleUnderline = Line(Point(VarData.endWindow.getWidth()/5 + 13, VarData.endWindow.getHeight()/6), Point(VarData.endWindow.getWidth() - 17, VarData.endWindow.getHeight()/6))
    titleUnderline.setFill(color_rgb(225, 225, 225))
    titleUnderline.setWidth(1)
    titleUnderline.draw(VarData.endWindow)

    title = Text(Point(VarData.endWindow.getWidth()/4.*2.3 + 5, VarData.endWindow.getHeight()/10), "Game Summary")
    title.setFace("helvetica")
    title.setStyle("italic")
    title.setSize(26)
    title.setTextColor(color_rgb(90, 0, 0))
    title.draw(VarData.endWindow)

    picName = ""

    if finalGameState == "Win":
        picName = "Balloons.gif"
    else:
        picName = "Image not Found.ppm"

    titlePic = Image(Point(VarData.endWindow.getWidth()/10 + 3, VarData.endWindow.getHeight()/10), picName)
    titlePic.draw(VarData.endWindow)

# Draw Grey Lines
def DrawBars():
    endHeight = VarData.endWindow.getHeight()
    endWidth = VarData.endWindow.getWidth()

    titleLine = Line(Point(10, endHeight/5), Point(endWidth- 10, endHeight/5))
    titleLine.setFill(color_rgb(220, 210, 210))
    titleLine.setWidth(2)
    titleLine.draw(VarData.endWindow)

    middleLine = Line(Point(endWidth/5*2, endHeight/5 + 10), Point(endWidth/5*2, endHeight - 10))
    middleLine.setFill(color_rgb(220, 210, 210))
    middleLine.setWidth(2)
    middleLine.draw(VarData.endWindow)

    # Button Bars
    for yBar in range(endHeight/5*2, endHeight, endHeight/5):
        middleLine = Line(Point(10, yBar), Point(endWidth/5*2 - 10, yBar))
        middleLine.setFill(color_rgb(220, 210, 210))
        middleLine.setWidth(1)
        middleLine.draw(VarData.endWindow)

    # Score Bar
    scoreLine = Line(Point(endWidth/5*2 + 10, endHeight/5*4-13), Point(endWidth-10, endHeight/5*4-13))
    scoreLine.setFill(color_rgb(220, 210, 210))
    scoreLine.setWidth(1)
    scoreLine.draw(VarData.endWindow)

# Supply Information to Buttons
def DrawButtons():
    endHeight = VarData.endWindow.getHeight()

    DrawButton(endHeight/5 + endHeight/10, "Retry")
    DrawButton(endHeight/5*2 + endHeight/10, u'\u0394' + " Difficulty")
    DrawButton(endHeight/5*3 + endHeight/10, "Menu")
    DrawButton(endHeight/5*4 + endHeight/10, "Quit")
    
# Draw Transition Buttons
def DrawButton(yPos, text):
    button = Text(Point(VarData.endWindow.getWidth()/5, yPos), text)
    button.setFace("times roman")
    button.setSize(12)
    button.setTextColor(color_rgb(120, 120, 120))
    button.draw(VarData.endWindow)

# Draw Game Summary
def DrawText(currentScore, newHS):
    endHeight = VarData.endWindow.getHeight()
    endWidth = VarData.endWindow.getWidth()

    # Label Values
    difficultyLabel = Text(Point(endWidth/3*2, endHeight/4 + 10), "Difficulty:")
    difficultyLabel.setFace("courier")
    difficultyLabel.setSize(12)
    difficultyLabel.setTextColor(color_rgb(80, 80, 80))
    difficultyLabel.draw(VarData.endWindow)

    timeLabel = Text(Point(endWidth/3*2-10, endHeight/4 + 40), "Time Elapsed:")
    timeLabel.setFace("courier")
    timeLabel.setSize(12)
    timeLabel.setTextColor(color_rgb(80, 80, 80))
    timeLabel.draw(VarData.endWindow)

    minesLabel = Text(Point(endWidth/3*2 - 15, endHeight/4 + 70), "Unswept Tiles:")
    minesLabel.setFace("courier")
    minesLabel.setSize(12)
    minesLabel.setTextColor(color_rgb(80, 80, 80))
    minesLabel.draw(VarData.endWindow)

    # Attribute Values
    difficultyValue = Text(Point(endWidth/10*9, endHeight/4 + 10), str(2**VarData.difficulty) + "x")
    difficultyValue.setFace("times roman")
    difficultyValue.setSize(12)
    difficultyValue.setTextColor(color_rgb(250, 50, 50))
    difficultyValue.draw(VarData.endWindow)

    timeValue = 0
    try:
        timeValue = Text(Point(endWidth/10*9, endHeight/4 + 40), str(VarData.gameTime) + "s")
    except AttributeError:
        timeValue = Text(Point(endWidth/10*9, endHeight/4 + 40), "0s")
    timeValue.setFace("times roman")
    timeValue.setSize(12)
    timeValue.setTextColor(color_rgb(50, 150, 50))
    timeValue.draw(VarData.endWindow)

    minesValue = 0
    try:
        minesValue = Text(Point(endWidth/10*9, endHeight/4 + 70), str(VarData.safeTiles - VarData.tileCount))
    except AttributeError:
        minesValue = Text(Point(endWidth/10*9, endHeight/4 + 70), "150")
    minesValue.setFace("times roman")
    minesValue.setSize(12)
    minesValue.setTextColor("blue")
    minesValue.draw(VarData.endWindow)

    # Arrows and Calculus Ratiocinator
    firstArrow = Text(Point(endWidth/10*7, endHeight/2 + 2), u"\u21E3")
    firstArrow.setFace("arial")
    firstArrow.setSize(20)
    firstArrow.setTextColor(color_rgb(150, 150, 150))
    firstArrow.draw(VarData.endWindow)

    algText = Text(Point(endWidth/10*7, endHeight/3*2-31), "Calculus Ratiocinator")
    algText.setFace("helvetica")
    algText.setStyle("italic")
    algText.setSize(12)
    algText.setTextColor(color_rgb(100, 100, 100))
    algText.draw(VarData.endWindow)

    secondArrow = Text(Point(endWidth/10*7, endHeight/3*2-3), u"\u21E3")
    secondArrow.setFace("arial")
    secondArrow.setSize(22)
    secondArrow.setTextColor(color_rgb(150, 150, 150))
    secondArrow.draw(VarData.endWindow)

    # Calculated Score
    currentScore = Text(Point(endWidth/10*7, endHeight/4*3 - 12), "Final Score = " + str(currentScore))
    currentScore.setFace("courier")
    currentScore.setSize(12)
    currentScore.setTextColor(color_rgb(204, 102, 0))
    currentScore.draw(VarData.endWindow)

    # Current High Score
    highScorePrimer = Text(Point(endWidth/7*4 + 5, endHeight/5*4), "Current High Score:")
    highScorePrimer.setFace("arial")
    highScorePrimer.setSize(10)
    highScorePrimer.setTextColor(color_rgb(200, 200, 200))
    highScorePrimer.draw(VarData.endWindow)    

    highScore = Text(Point(endWidth/10*7, endHeight/10*9), str(VarData.currentHighScore))
    highScore.setFace("times roman")
    highScore.setSize(28)
    highScore.setTextColor(color_rgb(200, 50, 50))
    if newHS == True:
        highScore.setTextColor(color_rgb(100, 200, 100))
    highScore.draw(VarData.endWindow)   

# Draw "Calculus Rationcinator" Background
def DrawCalcRatBox():
    endHeight = VarData.endWindow.getHeight()
    endWidth = VarData.endWindow.getWidth()

    calcRatBox = Rectangle(Point(endWidth/2 - 12, endHeight/3*2-18), Point(endWidth/10*9 + 14, endHeight/3*2-43))
    calcRatBox.setWidth(2)
    calcRatBox.setOutline(color_rgb(220, 220, 220))
    calcRatBox.draw(VarData.endWindow)