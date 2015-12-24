# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# Instructions Module

from graphics import *

import VarData
import Input, Menu
from time import sleep

# Manual Constructor
def InstructionsMain():
    VarData.currentPanel = 0

    uInput = 4

    while uInput > 0:
        if uInput == 2:
            if VarData.currentPanel == 0:
                VarData.currentPanel = 3
            else:
                VarData.currentPanel -= 1

        if uInput == 3:
            if VarData.currentPanel == 3:
                VarData.currentPanel = 0
            else:
                VarData.currentPanel += 1

        if uInput == 2:
            CycleInstructions(False)
        else:
            CycleInstructions(True) 

        uInput = Input.InstructionsClick()

        if uInput == 0:
            break

        if uInput == 1:
            VarData.currentPanel = 0
            Menu.ClearWindow(False)
            Menu.MenuMain(False, False)
            return None

    Input.CloseWindow(VarData.menuWindow)

# Call to Appropriate Instructions Panel 
def CycleInstructions(toTheRight):
    if VarData.currentPanel == 0:
        Panel0(toTheRight)
    elif VarData.currentPanel == 1:
        Panel1(toTheRight)
    elif VarData.currentPanel == 2:
        Panel2(toTheRight)
    else:
        Panel3(toTheRight)

# Draw Panel Base
def PanelBase(panelTitle, toTheRight):
    Menu.ClearWindow(toTheRight)

    height = VarData.menuWindow.getHeight()
    width = VarData.menuWindow.getWidth()

    titleBar = Line(Point(10, 60),Point(width/3-10, 60))
    MonoAlphaColour(255, titleBar.setOutline)
    titleBar.setWidth(2)
    if VarData.currentPanel != 2:
        titleBar.draw(VarData.menuWindow)

    topButtonBar = Line(Point(10, 350),Point(width-10, 350))
    MonoAlphaColour(255, topButtonBar.setOutline)
    topButtonBar.setWidth(2)
    topButtonBar.draw(VarData.menuWindow)

    integralSeperator = Text(Point(width/4,377),u"\u222B")
    integralSeperator.setSize(30)
    integralSeperator.setFace("arial")
    MonoAlphaColour(255, integralSeperator.setTextColor)
    integralSeperator.draw(VarData.menuWindow)

    integralSeperator2 = integralSeperator.clone()
    integralSeperator2.move(width/4,0)
    integralSeperator2.draw(VarData.menuWindow)

    integralSeperator3 = integralSeperator2.clone()
    integralSeperator3.move(width/4,0)
    integralSeperator3.draw(VarData.menuWindow)

    quitText = Text(Point(width/8,377),"Quit")
    quitText.setSize(16)
    quitText.setFace("helvetica")
    MonoAlphaColour(255, quitText.setTextColor)
    quitText.draw(VarData.menuWindow)

    menuText = quitText.clone()
    menuText.move(width/4,0)
    menuText.setText("Menu")
    menuText.draw(VarData.menuWindow)

    leftText = menuText.clone()
    leftText.move(width/4,0)
    leftText.setText(u"\u21A9")
    leftText.setSize(32)
    leftText.draw(VarData.menuWindow)

    rightText = leftText.clone()
    rightText.move(width/4,0)
    rightText.setText(u"\u21AA")
    rightText.draw(VarData.menuWindow)

    titleText = Text(Point(width/6,30), panelTitle)
    titleText.setSize(20)
    titleText.setFace("helvetica")
    titleText.setStyle("italic")
    titleText.setTextColor(color_rgb(255, 255, 255))
    if VarData.currentPanel != 2:
        titleText.draw(VarData.menuWindow)

    for alpha in range(250, 20, -10):
        if alpha < 100:
            titleText.setFill(color_rgb(100,alpha,alpha))
            sleep(0.003)

        if alpha >= 100:
            titleText.setFill(color_rgb(alpha,alpha,alpha))
            sleep(0.003)

        if 140 <= alpha < 170:
            titleBar.setFill(color_rgb(alpha,alpha,alpha))
            sleep(0.003)

        if alpha >= 170:
            titleBar.setFill(color_rgb(alpha,alpha,alpha))
            topButtonBar.setFill(color_rgb(alpha,alpha,alpha))
            integralSeperator.setFill(color_rgb(alpha,alpha,alpha))
            integralSeperator2.setFill(color_rgb(alpha,alpha,alpha))
            integralSeperator3.setFill(color_rgb(alpha,alpha,alpha))
            quitText.setFill(color_rgb(alpha,alpha,alpha))
            menuText.setFill(color_rgb(alpha,alpha,alpha))
            leftText.setFill(color_rgb(alpha,alpha,alpha))
            rightText.setFill(color_rgb(alpha,alpha,alpha))

    sleep(0.2)

# Initialize Text List for Sliding
def InitPanelMoveList():
    VarData.panelMoveList = []

    for emptyList in range(11):
        VarData.panelMoveList.append([])

# Slide Buffered Text
def MoveText():
    for line in VarData.panelMoveList:
        if line == []:
            break
        for xCoord in range(10):
            for graphicsText in line:
                graphicsText.move(60,0)
        sleep(VarData.iSleepDelay)
    del(VarData.panelMoveList)

# Change Graphics Object to Monotomne Alpha Value
def MonoAlphaColour(alphaValue, functionAndObject):
    functionAndObject(color_rgb(alphaValue,alphaValue,alphaValue))

# Draw Text Object and Append to Buffer List
def DrawText(lineIndex, textPoint, textString, textSize, textFace, textStyle, textColor):
    strText = Text(textPoint, textString)
    strText.setSize(textSize)
    strText.setFace(textFace)
    strText.setStyle(textStyle)
    strText.setTextColor(textColor)

    if lineIndex != -1:
        strText.move(-600,0)

    strText.draw(VarData.menuWindow)

    VarData.panelMoveList[lineIndex].append(strText)

# Draw Objectives Panel
def Panel0(toTheRight): 
    PanelBase("Objectives",toTheRight)

    InitPanelMoveList()

    DrawText(0, Point(25, 95), ">>>", 11, "courier", "normal", color_rgb(80,20,20))
    DrawText(0, Point(82, 95), "goal = ", 12, "courier", "normal", color_rgb(40,40,120))
    DrawText(0, Point(342, 94), "Reveal all non-mine tiles before time expires", 12, "courier", "normal", color_rgb(200,100,0))

    DrawText(1, Point(25, 135), ">>>", 11, "courier", "normal", color_rgb(80,20,20))
    DrawText(1, Point(107, 135), "tileInput = ", 12, "courier", "normal", color_rgb(40,40,120))
    DrawText(1, Point(222, 135), "Mouse click", 12, "courier", "normal", color_rgb(200,100,0))
    DrawText(1, Point(360, 135), "# Reveals tile", 12, "courier", "normal", color_rgb(200,0,0))

    DrawText(2, Point(25, 175), ">>>", 11, "courier", "normal", color_rgb(80,20,20))
    DrawText(2, Point(155, 175), "if (                ):", 12, "courier", "normal", color_rgb(40,120,40))
    DrawText(2, Point(165, 175), "Mine is revealed", 12, "courier", "normal", color_rgb(0,50,0))

    DrawText(3, Point(110, 215), "loss =", 12, "courier", "normal", color_rgb(40,40,120))
    DrawText(3, Point(170, 215), "True", 12, "courier", "normal", color_rgb(100,0,204))

    DrawText(4, Point(25, 255), ">>>", 11, "courier", "normal", color_rgb(80,20,20))
    DrawText(4, Point(243, 255), "elif (                               ):", 12, "courier", "normal", color_rgb(40,120,40))
    DrawText(4, Point(263, 255), "All non-mine tiles are revealed", 12, "courier", "normal", color_rgb(0,50,0))

    DrawText(5, Point(108, 295), "win =", 12, "courier", "normal", color_rgb(40,40,120))
    DrawText(5, Point(167, 295), "True", 12, "courier", "normal", color_rgb(100,0,204))

    MoveText()

# Draw Mechanics Panel
def Panel1(toTheRight): 
    PanelBase("Mechanics",toTheRight)

    InitPanelMoveList()

    textRange = range(85, 330, 30)

    DrawText(0, Point(25, textRange[0]), ">>>", 11, "courier", "normal", color_rgb(80,20,20))
    DrawText(0, Point(240, textRange[0]), "if (                                ):", 12, "courier", "normal", color_rgb(40,120,40))
    DrawText(0, Point(250, textRange[0]), "Clicked tile has adjacent mines", 12, "courier", "normal", color_rgb(0,50,0))

    DrawText(1, Point(214, textRange[1]), "Show number of adjacent mines", 12, "courier", "normal", color_rgb(200,100,0))

    DrawText(2, Point(25, textRange[2]), ">>>", 11, "courier", "normal", color_rgb(80,20,20))
    DrawText(2, Point(76, textRange[2]), "else:", 12, "courier", "normal", color_rgb(40,120,40))

    DrawText(3, Point(190, textRange[3]), "Reveal surrounding tiles", 12, "courier", "normal", color_rgb(200,100,0))

    DrawText(4, Point(25, textRange[4]), ">>>", 11, "courier", "normal", color_rgb(80,20,20))
    DrawText(4, Point(112, textRange[4]), "gameLayout =", 12, "courier", "normal", color_rgb(40,40,120))
    DrawText(4, Point(187, textRange[4]), "{", 12, "courier", "normal", color_rgb(0,102,0))
    DrawText(4, Point(555, textRange[4]), "\\", 12, "courier", "normal", color_rgb(0,102,0))

    DrawText(5, Point(150, textRange[5]), '"Progress Meter"', 12, "courier", "normal", color_rgb(204,0,102))
    DrawText(5, Point(235, textRange[5]), ':', 12, "courier", "normal", "black")
    DrawText(5, Point(353, textRange[5]), 'Revealed tile progess', 12, "courier", "normal", color_rgb(153,0,0))
    DrawText(5, Point(555, textRange[5]), "\\", 12, "courier", "normal", color_rgb(0,102,0))

    DrawText(6, Point(185, textRange[6]), '"Cost-Benefit Tradeoff"', 12, "courier", "normal", color_rgb(204,0,102))
    DrawText(6, Point(305, textRange[6]), ':', 12, "courier", "normal", "black")
    DrawText(6, Point(427, textRange[6]), 'Reveal tiles for time', 12, "courier", "normal", color_rgb(153,0,0))
    DrawText(6, Point(555, textRange[6]), "\\", 12, "courier", "normal", color_rgb(0,102,0))

    DrawText(7, Point(100, textRange[7]), '"Flag"', 12, "courier", "normal", color_rgb(204,0,102))
    DrawText(7, Point(137, textRange[7]), ':', 12, "courier", "normal", "black")
    DrawText(7, Point(269, textRange[7]), 'Marked tile (visual aid)', 12, "courier", "normal", color_rgb(153,0,0))
    DrawText(7, Point(402, textRange[7]), "}", 12, "courier", "normal", color_rgb(0,102,0))

    DrawText(8, Point(25, textRange[8]), ">>>", 11, "courier", "normal", color_rgb(80,20,20))
    DrawText(8, Point(105, textRange[8]), "# Score " + u"\u221D" + " 2", 12, "courier", "normal", color_rgb(200,0,0))
    DrawText(8, Point(205, textRange[8]-5), "Difficulty", 10, "courier", "normal", color_rgb(200,0,0))

    MoveText()

# Draw Game Outline Panel
def Panel2(toTheRight):
    width = VarData.menuWindow.getWidth()
    height = VarData.menuWindow.getHeight()

    PanelBase(" ",toTheRight)

    InitPanelMoveList()

    clearRect = Rectangle(Point(0,0),Point(width,100))
    MonoAlphaColour(255, clearRect.setFill)
    MonoAlphaColour(255, clearRect.setOutline)
    clearRect.draw(VarData.menuWindow)

    outlineBackground = Image(Point(width/2+70,height/5*2+15), "Game Outline.ppm")
    outlineBackground.draw(VarData.menuWindow)
    del (outlineBackground)

    for yCoord in range(15, 350, 31):
        DrawText(yCoord/31,Point(20, yCoord), ">>>", 9, "courier", "normal", color_rgb(80,20,20))
    
    textRange = range(16, 350, 31)
    
    DrawText(0, Point(86, textRange[0]), "Change Difficulty", 9, "times roman", "normal", color_rgb(136,32,32))
    DrawText(1, Point(79, textRange[1]), "Restart Game", 9, "times roman", "normal", color_rgb(0,159,44))
    DrawText(2, Point(79, textRange[2]), "Time Elapsed", 9, "times roman", "normal", color_rgb(255,184,0))
    DrawText(3, Point(72, textRange[3]), "Time 'Limit'", 9, "times roman", "normal", color_rgb(212,136,136))
    DrawText(4, Point(67, textRange[4]), "Progress", 9, "times roman", "normal", color_rgb(51,101,153))
    DrawText(5, Point(74, textRange[5]), "Flag Toggle", 9, "times roman", "normal", color_rgb(224,94,0))
    DrawText(6, Point(79, textRange[6]), "Time Tradeoff", 9, "times roman", "normal", color_rgb(108,138,46))
    DrawText(7, Point(72, textRange[7]), "Quit Button", 9, "times roman", "normal", color_rgb(187,0,0))
    DrawText(8, Point(53, textRange[8]), "Grid", 9, "times roman", "normal", color_rgb(251,62,224))
    DrawText(9, Point(84, textRange[9]), "Revealed Tiles", 9, "times roman", "normal", color_rgb(90,156,174))
    DrawText(10, Point(55, textRange[10]), "Flag", 9, "times roman", "normal", color_rgb(117,99,140))

    MoveText()

# Draw Difficulties Panel
def Panel3(toTheRight):
    width = VarData.menuWindow.getWidth()

    PanelBase("Difficulties",toTheRight)

    InitPanelMoveList()

    # Vertical Grid Bars
    for xCoord in range(width/3, width-1, width/6):
        vertLine = Line(Point(xCoord, 10), Point(xCoord, 340))
        MonoAlphaColour(230, vertLine.setFill)
        if xCoord == width/3:
            MonoAlphaColour(200, vertLine.setFill)
        vertLine.draw(VarData.menuWindow)

    # Horizontal Grid Bars
    for yCoord in range(80, 330, 38):
        horizLine = Line(Point(10, yCoord), Point(width - 10, yCoord))
        MonoAlphaColour(230, horizLine.setFill)
        if yCoord == 80:
            MonoAlphaColour(200, horizLine.setFill)
        elif yCoord == 156:
            MonoAlphaColour(220, horizLine.setFill)
        horizLine.draw(VarData.menuWindow)

    symbolHeader = u'\u03C0' + "     " + u'\u03C3' + "     " + u'\u03A9' + "     " + u'\u221A\u002D\u0031'
    DrawText(-1, Point(width/3 + width/12, 39), u'\u03C0', 30, "times roman", "italic", color_rgb(170,170,170))
    DrawText(-1, Point(width/3 + width/4, 39), u'\u03C3', 30, "times roman", "normal", color_rgb(170,170,170))
    DrawText(-1, Point(width/3 + width/12*5, 42), u'\u03A9', 24, "times roman", "normal", color_rgb(170,170,170))
    DrawText(-1, Point(width/3 + width/12*7, 43), u'\u221A\u002D\u0031', 19, "times roman", "normal", color_rgb(170,170,170))

    textRange = range(99, 330, 38)

    horizAlpha = 100
    horizHeaderClr = color_rgb(horizAlpha,horizAlpha,horizAlpha)

    DrawText(-1, Point(width/6, textRange[0]), "Score Multiplier", 11, "helvetica", "normal", horizHeaderClr)
    DrawText(-1, Point(width/6, textRange[1]), "Time Limit", 11, "helvetica", "normal", horizHeaderClr)
    DrawText(-1, Point(width/6, textRange[2]), "Time Tradeoff", 11, "helvetica", "normal", horizHeaderClr)
    DrawText(-1, Point(width/6, textRange[3]), "Numbered Tiles", 11, "helvetica", "normal", horizHeaderClr)
    DrawText(-1, Point(width/6, textRange[4]), "Flag Toggle", 11, "helvetica", "normal", horizHeaderClr)
    DrawText(-1, Point(width/6, textRange[5]), "Progress Meter", 11, "helvetica", "normal", horizHeaderClr)
    DrawText(-1, Point(width/6, textRange[6]), "Colour Semantics", 11, "helvetica", "normal", horizHeaderClr)

    # Difficulty Multiplier Row
    DrawText(-1, Point(width/3 + width/12, textRange[0]), "2" + u"\u2070", 12, "times roman", "normal", color_rgb(200, 0, 0))
    DrawText(-1, Point(width/3 + width/4, textRange[0]), "2" + u"\u00B9", 12, "times roman", "normal", color_rgb(230, 100, 0))
    DrawText(-1, Point(width/3 + width/12*5, textRange[0]), "2" + u"\u00B2", 12, "times roman", "normal", color_rgb(26, 146, 238))
    DrawText(-1, Point(width/3 + width/12*7, textRange[0]), "2" + u"\u00B3", 12, "times roman", "normal", color_rgb(0, 153, 0))

    # Time Limit Row
    DrawText(-1, Point(width/3 + width/12, textRange[1]), u"\u221E", 16, "times roman", "normal", color_rgb(0, 153, 0))
    DrawText(-1, Point(width/3 + width/4, textRange[1]), "10 min", 10, "times roman", "normal", color_rgb(26, 146, 238))
    DrawText(-1, Point(width/3 + width/12*5, textRange[1]), "5 min", 10, "times roman", "normal", color_rgb(230, 100, 0))
    DrawText(-1, Point(width/3 + width/12*7, textRange[1]), "2 min", 10, "times roman", "normal", color_rgb(200, 0, 0))

    # Draw Check Marks

    diffTrue = Image(Point(width/3 + width/12,textRange[0]), "Difficulties Table True.ppm")
    diffModifiedTrue = Image(Point(width/3 + width/12,textRange[0]), "Difficulties Table Modified True.ppm")
    diffFalse = Image(Point(width/3 + width/12,textRange[0]), "Difficulties Table False.ppm")


    # -1 = False, 0 = Modified True, 1 = True

    diffValueList = [ \
    [None],    \
    [None],    \
    [1,0,-1,-1],      \
    [1,1,0,-1],       \
    [1,1,1,-1],       \
    [1,1,0,-1],       \
    [1,1,1,0],      ]

    for row in range(2,7):
        for col in range(4):
            diffMark = None

            if diffValueList[row][col] == -1:
                diffMark = diffFalse.clone()
            elif diffValueList[row][col] == 1:
                diffMark = diffTrue.clone()
            else:
                diffMark = diffModifiedTrue.clone()

            diffMark.move(col*width/6,row*38)
            diffMark.draw(VarData.menuWindow)