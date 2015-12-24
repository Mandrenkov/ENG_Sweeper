# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# Difficulty Module

from graphics import *

import VarData
import Input, Menu

# Manual Constructor
def DifficultyMain():
    VarData.diffWindow = GraphWin("Difficulty Selection", 350, 410)
    VarData.diffWindow.setBackground("white")

    DrawTitle()
    DrawButtonBars()
    DrawButtonMultipliers()
    DrawImplyArrows()
    DrawButtons()

    uInput = Input.CloseDiff()

    if uInput == 4:
        return None
    elif uInput == 5:
        Menu.MenuMain(False, True) 
        return None
    else:
        return uInput

# Draw "Title" Elements Above Top Bar
def DrawTitle():
    titleUnderline = Line(Point(VarData.diffWindow.getWidth()/4 + 3, 360/8 + 18), Point(VarData.diffWindow.getWidth() - 20, 360/8 + 18))
    titleUnderline.setFill(color_rgb(225, 225, 225))
    titleUnderline.setWidth(1)
    titleUnderline.draw(VarData.diffWindow)

    title = Text(Point(VarData.diffWindow.getWidth()/4.*2.4, 360/8), "Difficulty Selection")
    title.setFace("helvetica")
    title.setStyle("italic")
    title.setSize(22)
    title.setTextColor(color_rgb(90, 0, 0))
    title.draw(VarData.diffWindow)

    product = Text(Point(VarData.diffWindow.getWidth()/8, 360/8-3), u"\u220F")
    product.setFace("helvetica")
    product.setStyle("italic")
    product.setSize(22)
    product.setTextColor(color_rgb(50,0, 0))
    product.draw(VarData.diffWindow)

    producti = Text(Point(VarData.diffWindow.getWidth()/8 - 11, 360/8+23), "k")
    producti.setFace("helvetica")
    producti.setStyle("italic")
    producti.setSize(12)
    producti.setTextColor(color_rgb(100, 0, 0))
    producti.draw(VarData.diffWindow)

    producteq = Text(Point(VarData.diffWindow.getWidth()/8 + 8, 360/8+24), "= 1")
    producteq.setFace("helvetica")
    producteq.setStyle("normal")
    producteq.setSize(12)
    producteq.setTextColor(color_rgb(100, 0, 0))
    producteq.draw(VarData.diffWindow)

    productn = Text(Point(VarData.diffWindow.getWidth()/8 + 1, 360/8-25), u"\u2116")
    productn.setFace("arial")
    productn.setStyle("normal")
    productn.setSize(12)
    productn.setTextColor(color_rgb(100, 100, 100))
    productn.draw(VarData.diffWindow)

# Draw Grey Lines
def DrawButtonBars():
    height = 360/16.*3

    for a in range (0,4):
        if a == 0:
            line = Line(Point(10, 360/4), Point(VarData.diffWindow.getWidth() - 10, 360/4))
        else:
            line = Line(Point(VarData.diffWindow.getWidth()/3, a * height + 360/4), Point(VarData.diffWindow.getWidth() - 10, a * height + 360/4))
        line.setFill(color_rgb(220, 210, 210))
        line.setWidth(2)
        line.draw(VarData.diffWindow)

        if a > 0:
            smallLine = Line(Point(15, a * height + 360/4 - 1), Point(83, a * height + 360/4 - 1))
            smallLine.setFill(color_rgb(230, 220, 220))
            smallLine.draw(VarData.diffWindow)

    topTransitionBar = Line(Point(10, 360), Point(VarData.diffWindow.getWidth() - 10, 4 * height + 360/4))
    topTransitionBar.setFill(color_rgb(230,230,230))
    topTransitionBar.setWidth(2)
    topTransitionBar.draw(VarData.diffWindow)

    middleTransitionBar = Line(Point(VarData.diffWindow.getWidth()/2, 360 + 5), Point(VarData.diffWindow.getWidth()/2, VarData.diffWindow.getHeight()-5))
    middleTransitionBar.setFill(color_rgb(220,220,220))
    middleTransitionBar.setWidth(1)
    middleTransitionBar.draw(VarData.diffWindow)

# Supplies Information to Draw Multipiers
def DrawButtonMultipliers():
    DrawMultiplier(360/32 * 3 + 360/4, u"\u2070")
    DrawMultiplier(360/32 * 9 + 360/4, u"\u00B9")
    DrawMultiplier(360/32 * 15 + 360/4 + 2, u"\u00B2")
    DrawMultiplier(360/32 * 21 + 360/4 + 6, u"\u00B3")

# Draw Multipliers
def DrawMultiplier(yPos, text):
    multiplier = Text(Point(VarData.diffWindow.getWidth()/7, yPos), "2" + text)
    multiplier.setFace("arial")
    multiplier.setStyle("normal")
    multiplier.setSize(20)
    multiplier.setTextColor(color_rgb(130, 130, 130))
    multiplier.draw(VarData.diffWindow)

# Draw Right Arrows (Technically not "Imply Arrows")
def DrawImplyArrows():
    height = 360
    for yArrow in range(height/32 * 3 + height/4, height, height/32 * 6):
        if yArrow == 360/32 * 15 + 360/4:
            yArrow += 2
        elif yArrow == 360/32 * 21 + 360/4:
            yArrow += 8
        implyArrow = Text(Point(360/3, yArrow), u"\u279F")
        implyArrow.setSize(30)
        implyArrow.setTextColor(color_rgb(220, 200, 200))
        implyArrow.draw(VarData.diffWindow)

# Supply Information to Draw Difficulty Buttons
def DrawButtons():
    DrawButton(360/32 * 3 + 360/4, "Easy as " + u'\u03C0')
    DrawButton(360/32 * 9 + 360/4, "Within " + u'\u03C3')
    DrawButton(360/32 * 15 + 360/4 + 2, "Some " + u'\u03A9')
    DrawButton(360/32 * 21 + 360/4 + 8, u'\u221A\u002D\u0031')

    DrawTransitionButtons()

# Draw Difficulty Buttons
def DrawButton(yPos, text):
    button = Text(Point(VarData.diffWindow.getWidth()/3 * 2, yPos), text)
    button.setFace("times roman")
    button.setStyle("normal")
    button.setSize(18)
    button.setTextColor(color_rgb(60, 60, 60))
    button.draw(VarData.diffWindow)

# Draw Menu / Quit Buttons
def DrawTransitionButtons():
    transButton = Text(Point(VarData.diffWindow.getWidth()/4, (360 + VarData.diffWindow.getHeight())/2 + 3), "Quit")
    transButton.setFace("helvetica")
    transButton.setSize(13)
    transButton.setTextColor(color_rgb(150,150,150))
    transButton.draw(VarData.diffWindow)

    transButtonMenu = transButton.clone()
    transButtonMenu.setText("Menu")
    transButtonMenu.move(VarData.diffWindow.getWidth()/2,0)
    transButtonMenu.draw(VarData.diffWindow)