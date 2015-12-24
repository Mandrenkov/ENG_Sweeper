# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# GameBackground Module

import VarData

from graphics import *

# Manual Constructor (Should be Called "BackgroundMain")
def MainBackground():
    DrawDiagonalBars()
    DrawWhiteRectangles()
    DrawFireball(515, 45)

# Supply Information to Drawing Methods
def DrawWhiteRectangles():
    lRect = Rectangle(Point(0, 0), Point(100, 600))
    bRect = Rectangle(Point(0, 85), Point(800, 600))
    rRect = Rectangle(Point(590, 0), Point(800, 600))
    mRect = Rectangle(Point(143, 15), Point(441, 74))
    fRect = Rectangle(Point(477, 10), Point(553, 80))

    DrawRectangle(lRect)
    DrawRectangle(bRect)
    DrawRectangle(rRect)
    DrawRectangle(mRect)
    DrawRectangle(fRect)

    DrawFadedRectangle(2, 148, 17, 436, 76)
    DrawFadedRectangle(2, 477, 10, 553, 80)

# Draw White Rectangle
def DrawRectangle(whiteRect):
    whiteRect.setFill("white")
    whiteRect.setOutline("white")
    whiteRect.draw(VarData.gameWindow)

# Draw White Rectangle with Faded Borders
def DrawFadedRectangle(width, initX, initY, sizeW, sizeH):
    for size in range(width):
        alpha = 255 - size * 10
        fadeRect = Rectangle(Point(initX-width + size, initY-width + size), Point(sizeW+width - size, sizeH+width - size))
        fadeRect.setFill(color_rgb(alpha, alpha, alpha))
        fadeRect.setOutline(color_rgb(alpha, alpha, alpha))

        fadeRect.draw(VarData.gameWindow)

    for size in range(width):
        alpha = (255 - (width - 1) * 10) + size * 10
        fadeRect = Rectangle(Point(initX+width + size, initY+width + size), Point(sizeW-width - size, sizeH-width - size))
        fadeRect.setFill(color_rgb(alpha, alpha, alpha))
        fadeRect.setOutline(color_rgb(alpha, alpha, alpha))

        fadeRect.draw(VarData.gameWindow)
    
# Draw Diagonal Bars
def DrawDiagonalBars():
    for coords in range(0, 800, 60):
        diagonalBar = Line(Point(0, coords), Point(coords, 0))
        diagonalBar.setFill(color_rgb(240, 240, 240))
        diagonalBar.setWidth(7)
        
        diagonalBar.draw(VarData.gameWindow)

# Draw Maroon Fireball
def DrawFireball(fireX, fireY):
    fireball = Image(Point(fireX, fireY), "Fireball.ppm")
    fireball.draw(VarData.gameWindow)