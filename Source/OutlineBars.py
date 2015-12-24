# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# OutlineBars Module

import VarData

from graphics import *

# Manual Constructor
def MainOutlineBars():
    DrawTitleBar()
    DrawProgressBar()
    DrawButtonBar()
    DrawIconBar()
    DrawTimeBar()
    DrawMineBar()

# Draw Title Barrier
def DrawTitleBar():
    barY = 95
    barWidth = 4
    halfWidth = barWidth/2
    for bar in range(halfWidth):
        lPoint1 = Point(10, barY - barWidth/2 + bar)
        lPoint2 = Point(790, barY - barWidth/2 + bar)
        aLine = Line(lPoint1, lPoint2)
        alpha = 255 - 55/halfWidth * bar
        aLine.setFill(color_rgb(alpha, alpha, alpha))
        aLine.draw(VarData.gameWindow)

    for bar in range(halfWidth):
        lPoint1 = Point(10, barY + bar)
        lPoint2 = Point(790, barY + bar)
        aLine = Line(lPoint1, lPoint2)
        alpha = 200 + 55/halfWidth * bar
        aLine.setFill(color_rgb(alpha, alpha, alpha))

        aLine.draw(VarData.gameWindow)

# Draw Progress Barrier
def DrawProgressBar():
    barX = 640
    barWidth = 4
    halfWidth = barWidth/2
    for bar in range(halfWidth):
        lPoint1 = Point(barX - barWidth/2 + bar, 115)
        lPoint2 = Point(barX - barWidth/2 + bar, 590)
        aLine = Line(lPoint1, lPoint2)
        alpha = 255 - 55/halfWidth * bar
        aLine.setFill(color_rgb(alpha, alpha, alpha))

        aLine.draw(VarData.gameWindow)

    for bar in range(halfWidth):
        lPoint1 = Point(barX + bar, 115)
        lPoint2 = Point(barX + bar, 590)
        aLine = Line(lPoint1, lPoint2)
        alpha = 200 + 55/halfWidth * bar
        aLine.setFill(color_rgb(alpha, alpha, alpha))

        aLine.draw(VarData.gameWindow)

# Draw Button Barrier
def DrawButtonBar():
    barY = 530
    barWidth = 4
    halfWidth = barWidth/2
    for bar in range(halfWidth):
        lPoint1 = Point(18, barY - barWidth/2 + bar)
        lPoint2 = Point(618, barY - barWidth/2 + bar)
        aLine = Line(lPoint1, lPoint2)
        alpha = 255 - 55/halfWidth * bar
        aLine.setFill(color_rgb(alpha, alpha, alpha))

        aLine.draw(VarData.gameWindow)

    for bar in range(halfWidth):
        lPoint1 = Point(18, barY + bar)
        lPoint2 = Point(618, barY + bar)
        aLine = Line(lPoint1, lPoint2)
        alpha = 200 + 55/halfWidth * bar
        aLine.setFill(color_rgb(alpha, alpha, alpha))

        aLine.draw(VarData.gameWindow)

# Draw Icon Barrier
def DrawIconBar():
    barX = 90
    iconBar = Line(Point(barX, 10), Point(barX, 80))
    iconBar.setWidth(2)
    iconBar.setFill(color_rgb(218, 218, 218))
    iconBar.draw(VarData.gameWindow)

# Draw Time Barrier
def DrawTimeBar():
    barX = 600
    timeBar = Line(Point(barX, 10), Point(barX, 80))
    timeBar.setWidth(2)
    timeBar.setFill(color_rgb(218, 218, 218))
    timeBar.draw(VarData.gameWindow)

# Draw Mine Barrier
def DrawMineBar():
    barY = 540
    timeBar = Line(Point(650, barY), Point(790, barY))
    timeBar.setWidth(2)
    timeBar.setFill(color_rgb(218, 218, 218))
    timeBar.draw(VarData.gameWindow)