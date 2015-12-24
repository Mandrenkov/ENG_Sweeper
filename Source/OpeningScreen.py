# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# OpeningScreen Module

from graphics import *
from math import cos, sin, pi

import VarData
import Input

# Manual Constructor
def OpeningScreenMain(displayOpeningScreen):
    TopKoch()
    BotKoch(displayOpeningScreen)
    TopRingAndKoch()
    DrawCoverRects(displayOpeningScreen)
    ENGSweeperTitle(displayOpeningScreen)
    OtherTitleText(displayOpeningScreen)
    if displayOpeningScreen:
        WhiteBorder()    

    if displayOpeningScreen:
        try:
            VarData.menuWindow.getMouse()
        except GraphicsError:
            return True

# Draw Top-Right Koch Snowflake and Ring 
def TopRingAndKoch():
    winHeight = VarData.menuWindow.getHeight()
    winWidth = VarData.menuWindow.getWidth()

    topRing = Circle(Point(595,-50), 260)
    topRing.setWidth(6)
    topRing.setFill(color_rgb(250, 250, 250))
    topRing.setOutline(color_rgb(138, 138, 138))
    topRing.draw(VarData.menuWindow)

    t = Turtle(VarData.menuWindow, 0, winHeight/3*2)
    Koch(t, 800, 5, True)
    tempPolygon = [Point(600, 0)] + t.kochPolygon()

    polyRangeAdj = 0
    for pointIndex in range(len(tempPolygon)):
        if tempPolygon[pointIndex - polyRangeAdj].getX() < 300:
            del(tempPolygon[pointIndex - polyRangeAdj]),
            polyRangeAdj += 1

    kPolygon = Polygon(tempPolygon)
    alphaClr = 200
    alpha = color_rgb(alphaClr,alphaClr,alphaClr)
    kPolygon.setFill(alpha)
    kPolygon.setOutline(alpha)
    kPolygon.draw(VarData.menuWindow)

# Draw Top-Left Koch Snowflake
def TopKoch():
    winHeight = VarData.menuWindow.getHeight()
    winWidth = VarData.menuWindow.getWidth()

    topKochRect = Rectangle(Point(0,0), Point(winWidth,winHeight/3))
    alphaClr = 210
    alpha = color_rgb(alphaClr,alphaClr,alphaClr)
    topKochRect.setFill(alpha)
    topKochRect.setOutline(alpha)
    topKochRect.draw(VarData.menuWindow)

    t = Turtle(VarData.menuWindow, 0, winHeight/3*2)
    Koch(t, 800, 5, True)
    kPolygon = Polygon(t.kochPolygon())
    kPolygon.setFill("white")
    kPolygon.setOutline("white")
    kPolygon.draw(VarData.menuWindow)

# Draw Bottom-Right Koch Snowflake
def BotKoch(displayOpeningScreen):
    winHeight = VarData.menuWindow.getHeight()
    winWidth = VarData.menuWindow.getWidth()

    VarData.oBotRect = Rectangle(Point(winWidth/2,winHeight/3*2-15), Point(winWidth,winHeight))
    alphaClr = 170
    alpha = color_rgb(alphaClr,alphaClr,alphaClr)
    VarData.oBotRect.setFill(alpha)
    VarData.oBotRect.setOutline(alpha)
    if displayOpeningScreen:
        VarData.oBotRect.draw(VarData.menuWindow)

    t = Turtle(VarData.menuWindow, -80, winHeight/3*2-15)
    Koch(t, 1000, 5, False)
    VarData.oBotKoch = Polygon(t.kochPolygon())
    VarData.oBotKoch.setFill("white")
    VarData.oBotKoch.setOutline("white")
    if displayOpeningScreen:
        VarData.oBotKoch.draw(VarData.menuWindow)

# "Turtle" Class - Polarized Coordinate Line Drawing Interface
# Note: Lowercase Function Names!
class Turtle:

    # Turtle Constructor
    def __init__(self, window, startWidth, startHeight):
        self.location = Point(startWidth, startHeight)
        self.direction = 0
        self.window = window
        self.polygon = []

    # Draw Line
    def draw(self, length, flip):
        newX = self.location.getX() + cos(self.direction) * length
        newY = self.location.getY() + sin(self.direction) * length
        self.location = Point(newX, newY)

        if flip == True:
            self.polygon.append(Point(newX, self.window.getHeight()-newY))
        else:
            self.polygon.append(Point(self.window.getWidth()-newX, newY))

    # Turn Turtle
    def turn(self, dAngle):
        self.direction += dAngle

    # Turn Turtle
    def kochPolygon(self):
        return self.polygon
        
# Recursive Function for Drawing Koch Snowflake     
def Koch(Turtle, length, degree, flip):
    if degree == 0:
        Turtle.draw(length, flip)
    else:
        length1 = length / 3
        degree1 = degree -1
        Koch(Turtle, length1, degree1, flip)
        Turtle.turn(pi/3)
        Koch(Turtle, length1, degree1, flip)
        Turtle.turn(-2 * pi/3)
        Koch(Turtle, length1, degree1, flip)
        Turtle.turn(pi/3)
        Koch(Turtle, length1, degree1, flip)

# Draw Various Rectangles
def DrawCoverRects(displayOpeningScreen):
    winHeight = VarData.menuWindow.getHeight()
    winWidth = VarData.menuWindow.getWidth()

    coverRect = Rectangle(Point(0,winHeight/2), Point(winWidth/3, winHeight))
    coverRect.setFill("white")
    coverRect.setOutline("white")
    coverRect.draw(VarData.menuWindow)

    if not(displayOpeningScreen):
        return None

    clickContRect = Rectangle(Point(0,winHeight/7*6), Point(winWidth/5*2, winHeight + 20))
    clickContRect.setWidth(3)
    clickContRect.setOutline(color_rgb(220,220,220))
    clickContRect.setFill(color_rgb(250,250,250))
    clickContRect.draw(VarData.menuWindow)

# Draw "ENG Sweeper" Title
def ENGSweeperTitle(displayOpeningScreen):
    VarData.oENG = Text(Point(95, 225), "ENG")
    VarData.oENG.setFace("courier")
    VarData.oENG.setStyle("italic")
    VarData.oENG.setSize(36)
    VarData.oENG.setTextColor(color_rgb(155,20,0))

    VarData.oSweeper = Text(Point(235, 225), "Sweeper")
    VarData.oSweeper.setFace("helvetica")
    VarData.oSweeper.setStyle("normal")
    VarData.oSweeper.setSize(30)
    VarData.oSweeper.setTextColor(color_rgb(190,50,0))
    
    if displayOpeningScreen:
        VarData.oENG.draw(VarData.menuWindow)
        VarData.oSweeper.draw(VarData.menuWindow)

# Draw Author, Prompt Text, and *Secret-ish* Binary Message
def OtherTitleText(displayOpeningScreen):
    devName = Text(Point(512, 385), "Mikhail Andrenkov")
    devName.setFace("times roman")
    devName.setStyle("italic")
    devName.setSize(14)
    devName.setTextColor("white")

    clickCont = Text(Point(118, 375), "< Click to Continue >")
    clickCont.setFace("courier")
    clickCont.setStyle("bold")
    clickCont.setSize(12)
    clickCont.setTextColor(color_rgb(120,120,120))

    secretMessage = "01010000011110010111010001101000011011110110111001000111011000010110110101100101010000110110100001100001011011000110110001100101011011100110011101100101"

    VarData.oMsg1 = Text(Point(160, 254), secretMessage[:len(secretMessage)/2])
    VarData.oMsg1.setSize(5)
    VarData.oMsg1.setTextColor(color_rgb(200, 200, 200))

    VarData.oMsg2 = Text(Point(160, 262), secretMessage[len(secretMessage)/2:])
    VarData.oMsg2.setSize(5)
    VarData.oMsg2.setTextColor(color_rgb(200, 200, 200))

    if displayOpeningScreen:
        devName.draw(VarData.menuWindow)
        clickCont.draw(VarData.menuWindow)
        VarData.oMsg1.draw(VarData.menuWindow)
        VarData.oMsg2.draw(VarData.menuWindow)

# Draw White Border around Window
def WhiteBorder():
    border = Rectangle(Point(2,2), Point(VarData.menuWindow.getWidth()+2, VarData.menuWindow.getHeight()+2))
    border.setWidth(4)
    border.setOutline("white")
    border.draw(VarData.menuWindow)