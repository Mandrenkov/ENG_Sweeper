# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# FlagMines Module

import VarData

from graphics import *

# Manual Constructor
def MainFlagMines():
	DrawMineButton()
	DrawToggleFalse()

# Draw Flag Toggle on Game Window
def DrawMineButton():
	height = 40

	flagButton = Text(Point(702, 570), 'Flag Toggle:')
	flagButton.setFace("helvetica")
	flagButton.setStyle("normal")
	flagButton.setSize(12)
	flagButton.setTextColor(color_rgb(150,150,150))

	try:
		flagButton.draw(VarData.gameWindow)
	except GraphicsError:
		return None

# Update Toggle State
def UpdateToggle():
	if VarData.flagState:
		DrawToggleTrue()
	else:
		DrawToggleFalse()

# Draw "True" Toggle
def DrawToggleTrue():
	toggleTrue = Image(Point(772, 572), "Toggle True.ppm")
	toggleTrue.draw(VarData.gameWindow)

# Draw "False" Toggle
def DrawToggleFalse():
	toggleFalse = Image(Point(772, 572), "Toggle False.ppm")
	toggleFalse.draw(VarData.gameWindow)

# Check if Tile is already Revealed
def AlreadyKnown(currentRow, currentColumn):
	if VarData.uGridContents[currentRow][currentColumn] == "Y":
		return True
	return False

# Check if Flag is already Exists
def FlagExists(currentRow, currentColumn):
	for coordPair in VarData.currentFlags:
		if coordPair == [currentRow, currentColumn]:
			return True
	return False

# Removes a Specified Flag Index
def RemoveFlagIndex(currentRow, currentColumn):
	for index in range(len(VarData.currentFlags)):
		if VarData.currentFlags[index] == [currentRow, currentColumn]:
			del VarData.currentFlags[index]
			break

# FlagMines Placeholder Constructor
def DrawPlaceholder():
	DrawPlaceholderBars()
	DrawPlaceholderBackground()
	DrawPlaceholderText()
	DrawPlaceholderBorder()

# Draw FlagMines Placeholder Lines
def DrawPlaceholderBars():
	for coords in range(650, 790, 25):
		diagonalBar = Line(Point(coords, 590), Point(coords + 15, 550))
		diagonalBar.setFill(color_rgb(230, 230, 230))
		diagonalBar.setWidth(4)
        
		diagonalBar.draw(VarData.gameWindow)

# Draw FlagMines Placeholder White Background
def DrawPlaceholderBackground():
	whiteBackground = Rectangle(Point(670,555), Point(770,585))
	whiteBackground.setFill("white")
	whiteBackground.setOutline("white")
	whiteBackground.draw(VarData.gameWindow)

# Draw FlagMines Placeholder "Locked" Text
def DrawPlaceholderText():
	lockText = Text(Point(720, 570), "Locked")
	lockText.setFace("helvetica")
	lockText.setStyle("italic")
	lockText.setSize(16)
	lockText.setTextColor(color_rgb(160,160,160))
	lockText.draw(VarData.gameWindow)

# Draw FlagMines Placeholder "Locked" Border
def DrawPlaceholderBorder():
	for width in range(4):
		backgroundBorder = Rectangle(Point(670+width,555+width), Point(770-width,585-width))
		alphaBackground = 255 - 10 * width
		backgroundBorder.setOutline(color_rgb(alphaBackground,alphaBackground,alphaBackground))
		backgroundBorder.draw(VarData.gameWindow)