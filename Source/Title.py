# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# Title Module

import VarData

from graphics import *
import time

# Manual Constructor
def MainTitle():
    DrawDifficultySymbol()
    DrawActualTitle()

# Draw "ENG Sweeper" Title
def DrawActualTitle():
    wordENG = Text(Point(202, 46), "ENG")
    wordENG.setFace("courier")
    wordENG.setStyle("italic")
    wordENG.setSize(36)
    wordENG.setTextColor(color_rgb(155,20,0))

    wordSweeper = Text(Point(345, 46), "Sweeper")
    wordSweeper.setFace("helvetica")
    wordSweeper.setStyle("normal")
    wordSweeper.setSize(30)
    wordSweeper.setTextColor(color_rgb(140,0,0))
    
    wordENG.draw(VarData.gameWindow)
    wordSweeper.draw(VarData.gameWindow)

# Draw Difficulty Symbol
def DrawDifficultySymbol():
    symbolText = Text(Point(45, 45), "")
    symbolText.setStyle("italic")
    symbolText.setSize(36)

    if VarData.difficulty == 0:
        symbolText.setText(u'\u03C0')
    elif VarData.difficulty == 1:
        symbolText.setText(u'\u03C3')
        symbolText.setStyle("normal")
    elif VarData.difficulty == 2:
        symbolText.setText(u'\u03A9')
        symbolText.setStyle("normal")
    else:
        symbolText.setText(u'\u221A\u002D\u0031')
        symbolText.setStyle("normal")
        symbolText.setSize(30)

    symbolText.setFace("times roman")

    symbolText.setTextColor(color_rgb(180,180,180))
    symbolText.draw(VarData.gameWindow)

# Draw Timer
def DrawTimer():
    CoverTimer()
    DrawTime()

# Cover Time Limit Space
def CoverTimeLimit():
    rectangle = Rectangle(Point(610, 75), Point(700, 92))
    rectangle.setFill("white")
    rectangle.setOutline("white")

    if VarData.gameStarted:
        try:
            rectangle.draw(VarData.gameWindow)
        except GraphicsError, ValueError:
            pass
        except Exception as exception:
            pass

# Cover Timer Space
def CoverTimer():
    rectangle = Rectangle(Point(610, 0), Point(VarData.gameWindow.getWidth(), 40))
    rectangle.setFill("white")
    rectangle.setOutline("white")

    if VarData.gameStarted:
        try:
            rectangle.draw(VarData.gameWindow)
        except GraphicsError, ValueError:
            pass
        except Exception as exception:
            pass

# Draw Timer
def DrawTime():
    gTime = VarData.gameTime

    hours = gTime / 3600
    minutes = (gTime - hours * 3600) / 60
    seconds = gTime - hours * 3600 - minutes * 60
    strTime = "%.2d:%.2d:%.2d" % (hours, minutes, seconds)

    timer = Text(Point(700, 27), strTime)
    timer.setFace("arial")
    timer.setSize(28)

    if VarData.blueTimerFlash:
        timer.setTextColor("blue")
        VarData.blueTimerFlash = False
    elif VarData.redTimerFlash:
        timer.setTextColor("red")
        VarData.redTimerFlash = False
    else:
        timer.setTextColor(color_rgb(150,150,150))

    if VarData.gameTime + 10 >= VarData.allowedTime:
        CoverTimeLimit()
        DrawTimeLimit()
        if VarData.gameTime % 2 == 1:
            timer.setTextColor("red") 

    if VarData.gameStarted:
        try:
            timer.draw(VarData.gameWindow)
        except GraphicsError, ValueError:
            pass
        except Exception as exception:
            pass

# Draw "Time Limit" (get it?)
def DrawTimeLimit():

    DrawSeperatorBar()

    INIT_LIM_X = 670

    if VarData.difficulty != 0:
        INIT_LIM_X -= 5

    INIT_LIM_Y = 67

    lim = Text(Point(INIT_LIM_X, INIT_LIM_Y), u'\u2113'+ "im")
    lim.setFace("helvetica")
    lim.setSize(17)
    lim.setTextColor(color_rgb(220,220,220))

    maxTimeText, timeAppZeroDX = GetMaxTimeText(INIT_LIM_X, INIT_LIM_Y)

    timeAppEnd = Text(Point(INIT_LIM_X - 8, INIT_LIM_Y + 18), u'\u0394' + "t " + u'\u2192')
    timeAppEnd.setSize(10)
    timeAppEnd.setFace("arial")
    timeAppEnd.setTextColor(color_rgb(200,200,200))

    if VarData.gameTime + 10 >= VarData.allowedTime and VarData.gameTime % 2 == 1:
        timeAppEnd.setTextColor("red")
        maxTimeText.setTextColor("red")

    timeAppZero = Text(Point(INIT_LIM_X + timeAppZeroDX, INIT_LIM_Y + 7),  u'\u23F0\u0020\u21D2' + " 0")
    timeAppZero.setSize(16)
    timeAppZero.setFace("arial")
    timeAppZero.setTextColor(color_rgb(205,205, 205))

    lim.draw(VarData.gameWindow)
    if maxTimeText.getText() == u'\u221E':
        timeAppEnd.draw(VarData.gameWindow)
    maxTimeText.draw(VarData.gameWindow)
    timeAppZero.draw(VarData.gameWindow)

# Draw Seperator Line Between Timer and Time Limit
def DrawSeperatorBar():
    timeBar = Line(Point(610, 50), Point(790, 50))
    timeBar.setFill(color_rgb(230, 230, 230))
    timeBar.setWidth(2)
    timeBar.draw(VarData.gameWindow)

# Return Max Time Text Object and Corresponding X-Coordinate
def GetMaxTimeText(INIT_LIM_X, INIT_LIM_Y):
    maxTime = ""

    if VarData.difficulty == 0:
        timeAppEndInf= Text(Point(INIT_LIM_X + 14, INIT_LIM_Y + 20), u'\u221E')
        timeAppEndInf.setSize(16)
        timeAppEndInf.setFace("times roman")
        timeAppEndInf.setTextColor(color_rgb(200,200,200))

        return timeAppEndInf, 55

    elif VarData.difficulty == 1:
        timeAppEnd10 = Text(Point(INIT_LIM_X, INIT_LIM_Y + 20), u'\u0394' + "t " + u'\u2192' + ' 10 min')
        timeAppEnd10.setSize(10)
        timeAppEnd10.setFace("times roman")
        timeAppEnd10.setTextColor(color_rgb(200,200,200))

        return timeAppEnd10, 70

    elif VarData.difficulty == 2:
        timeAppEnd5 = Text(Point(INIT_LIM_X, INIT_LIM_Y + 20), u'\u0394' + "t " + u'\u2192' + ' 5 min')
        timeAppEnd5.setSize(10)
        timeAppEnd5.setFace("times roman")
        timeAppEnd5.setTextColor(color_rgb(200,200,200))

        return timeAppEnd5, 67

    else:
        timeAppEnd2 = Text(Point(INIT_LIM_X, INIT_LIM_Y + 20), u'\u0394' + "t " + u'\u2192' + ' 2 min')
        timeAppEnd2.setSize(10)
        timeAppEnd2.setFace("times roman")
        timeAppEnd2.setTextColor(color_rgb(200,200,200))

        return timeAppEnd2, 67