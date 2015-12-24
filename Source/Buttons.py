# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# Buttons Module

import VarData

from graphics import *

# Manual Constructor
def MainButtons():
	DrawExitButton()

# Draw Quit Button on Game Window
def DrawExitButton():
	height = 40
	barStart = (VarData.gameWindow.getHeight() - 540)/2 - height/2 + 540

	exitLine = Line(Point(102, 541), Point(102, 595))
	exitLine.setFill(color_rgb(220, 210, 210))
	exitLine.setWidth(2)
	exitLine.draw(VarData.gameWindow)

	drawQuit = Text(Point(51, 565), u'\u01EA' + "ui" + u'\u03EF')
	drawQuit.setFace("arial")
	drawQuit.setStyle("normal")
	drawQuit.setSize(20)
	drawQuit.setTextColor(color_rgb(170,170,170))
	drawQuit.draw(VarData.gameWindow)

# Draw Only 1 Buttons for Difficulty 1
def DrawSingleButton():
	safeTileTop = Text(Point(370, 558), "Reveal Safe Tile")
	safeTileTop.setFace("times roman")
	safeTileTop.setStyle("normal")
	safeTileTop.setSize(14)
	safeTileTop.setTextColor(color_rgb(130,130,130))
	safeTileTop.draw(VarData.gameWindow)

	safeTileBot = Text(Point(370, 578), "Cost: 5 seconds")
	safeTileBot.setFace("arial")
	safeTileBot.setStyle("normal")
	safeTileBot.setSize(10)
	safeTileBot.setTextColor(color_rgb(160,160,160))
	safeTileBot.draw(VarData.gameWindow)

# Draw Both Buttons for Difficulty 0
def DrawPowerButtons():
	height = 40
	barStart = (VarData.gameWindow.getHeight() - 540)/2 - height/2 + 540

	powerLine = Line(Point(372, 546), Point(372, 590))
	powerLine.setFill(color_rgb(210, 200, 200))
	powerLine.setWidth(1)
	powerLine.draw(VarData.gameWindow)

	DrawSafeTileButton()
	DrawMineButton()

# Draw "Reveal Safe Tile" Button
def DrawSafeTileButton():
	safeTileTop = Text(Point(230, 558), "Reveal Safe Tile")
	safeTileTop.setFace("times roman")
	safeTileTop.setStyle("normal")
	safeTileTop.setSize(14)
	safeTileTop.setTextColor(color_rgb(130,130,130))
	safeTileTop.draw(VarData.gameWindow)

	safeTileBot = Text(Point(230, 578), "Cost: 5 seconds")
	safeTileBot.setFace("arial")
	safeTileBot.setStyle("normal")
	safeTileBot.setSize(10)
	safeTileBot.setTextColor(color_rgb(160,160,160))
	safeTileBot.draw(VarData.gameWindow)

# Draw "Flag Mine" Button
def DrawMineButton():
	mineTop = Text(Point(510, 558), "Flag Mine")
	mineTop.setFace("times roman")
	mineTop.setStyle("normal")
	mineTop.setSize(14)
	mineTop.setTextColor(color_rgb(130,130,130))
	mineTop.draw(VarData.gameWindow)

	mineBot = Text(Point(510, 578), "Cost: 20 seconds")
	mineBot.setFace("arial")
	mineBot.setStyle("normal")
	mineBot.setSize(10)
	mineBot.setTextColor(color_rgb(160,160,160))
	mineBot.draw(VarData.gameWindow)

# Draw Light Shaded Background (Deprecated)
def DrawButtonBackground(height, dAlpha, barStart, xStart, xEnd):
	barStart = (VarData.gameWindow.getHeight() - 540)/2 - height/2 + 540
	for dHeight in range(height):
		mLine = Line(Point(xStart, barStart + dHeight), Point(xEnd, barStart + dHeight))
		alpha = 255
		if (dHeight < height/2):
			alpha -= dHeight * dAlpha
		else:
			alpha = (255 - (height/2)*dAlpha) + (dHeight - height/2) * dAlpha
		mLine.setFill(color_rgb(alpha, alpha, alpha))
		
		mLine.draw(VarData.gameWindow)	

# Button Placeholder Constructor
def DrawPlaceholder():
	DrawPlaceholderBars()
	DrawPlaceholderBackground()
	DrawPlaceholderText()
	DrawPlaceholderBorder()

# Draw Button Placeholder Lines
def DrawPlaceholderBars():
	for coords in range(130, 610, 35):
		diagonalBar = Line(Point(coords, 590), Point(coords + 20, 540))
		diagonalBar.setFill(color_rgb(230, 230, 230))
		diagonalBar.setWidth(6)
        
		diagonalBar.draw(VarData.gameWindow)

# Draw Button Placeholder White Background
def DrawPlaceholderBackground():
	whiteBackground = Rectangle(Point(300,545), Point(440,585))
	whiteBackground.setFill("white")
	whiteBackground.draw(VarData.gameWindow)

# Draw Button Placeholder "Locked" Text
def DrawPlaceholderText():
	lockText = Text(Point(370, 565), "Locked")
	lockText.setFace("helvetica")
	lockText.setStyle("italic")
	lockText.setSize(22)
	lockText.setTextColor(color_rgb(160,160,160))
	lockText.draw(VarData.gameWindow)

# Draw Button Placeholder "Locked" Border
def DrawPlaceholderBorder():
	for width in range(6):
		backgroundBorder = Rectangle(Point(300+width,545+width), Point(440-width,585-width))
		alphaBackground = 255 - 10 * width
		backgroundBorder.setOutline(color_rgb(alphaBackground,alphaBackground,alphaBackground))
		backgroundBorder.draw(VarData.gameWindow)