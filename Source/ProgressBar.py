# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# ProgressBar Module

import VarData

from graphics import *
from math import sqrt, sin, pi

# Manual Constructor
def MainProgressBar():
	if VarData.difficulty != 3:
		DrawTitle()

	if VarData.difficulty == 2:
		VarData.originalCenterCube = Point(720 - sin(pi/3) * VarData.cubeSideLength/2, 170)
	else:
		VarData.originalCenterCube = Point(720, 170)

# Draw "Progress" Title
def DrawTitle():
	progressTitle = Text(Point(720, 125), "Progress")

	progressTitle.setFace("helvetica")
	progressTitle.setStyle("italic")
	progressTitle.setSize(19)
	progressTitle.setTextColor(color_rgb(100,100,100))

	progressTitle.draw(VarData.gameWindow)

# Draw Line Component of Neckercube Illusion
def DrawCubeComp():
	compOrder = []
	centerCube = 0
	sideL = VarData.cubeSideLength

	tilePercent = 100*VarData.tileCount/VarData.safeTiles
	yMult = tilePercent/10
	compIndex = tilePercent % 10

	if not(PercentageExists(yMult)):
		VarData.displayedPercentages.append(yMult)
		if VarData.difficulty < 2:
			DrawPercent(yMult)

	if tilePercent == 100:
		DrawWinningFireball()
		return None

	alpha = 200 - 2*tilePercent/3

	if yMult == 0: # First
		centerCube = VarData.originalCenterCube
		compOrder = [6, 1, 0, 4, 7, 5, 2, 3, 9, 10]
		if compIndex == 6:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 1))
			CubeFaceAlpha(cPolygon, 1)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 7:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 0))
			CubeFaceAlpha(cPolygon, 0)
			cPolygon.draw(VarData.gameWindow)
			pass
	elif yMult == 9: # Last
		centerCube = Point(VarData.originalCenterCube.getX() + sideL*sqrt(3)/2, VarData.originalCenterCube.getY() + yMult*sideL*1.5)
		compOrder = [3, 5, 8, 6, 1, 0, 4, 2, 7, 7, 7]
		if compIndex == 3:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 2))
			CubeFaceAlpha(cPolygon, 2)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 4:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 3))
			CubeFaceAlpha(cPolygon, 3)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 5:
			cPolygon = Polygon(CubeFaceCoords(CubeCenterToOldLeft(centerCube), 2))
			CubeFaceAlpha(cPolygon, 2)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 7:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 0))
			CubeFaceAlpha(cPolygon, 0)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 8:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 1))
			CubeFaceAlpha(cPolygon, 1)
			cPolygon.draw(VarData.gameWindow)
		pass
	elif yMult % 2 == 1: # Right
		centerCube = Point(VarData.originalCenterCube.getX() + sideL*sqrt(3)/2, VarData.originalCenterCube.getY() + yMult*sideL*1.5)
		compOrder = [3, 5, 8, 6, 1, 0, 4, 2, 11, 12]
		if compIndex == 3:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 2))
			CubeFaceAlpha(cPolygon, 2)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 4:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 3))
			CubeFaceAlpha(cPolygon, 3)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 5:
			cPolygon = Polygon(CubeFaceCoords(CubeCenterToOldLeft(centerCube), 2))
			CubeFaceAlpha(cPolygon, 2)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 7:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 0))
			CubeFaceAlpha(cPolygon, 0)
			cPolygon.draw(VarData.gameWindow)
		pass
	elif yMult % 2 == 0: # Left
		centerCube = Point(VarData.originalCenterCube.getX(), VarData.originalCenterCube.getY() + yMult*sideL* 1.5)
		compOrder = [2, 5, 7, 4, 0, 1, 6, 3, 9, 10]
		if compIndex == 3:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 1))
			CubeFaceAlpha(cPolygon, 1)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 4:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 4))
			CubeFaceAlpha(cPolygon, 4)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 5:
			cPolygon = Polygon(CubeFaceCoords(CubeCenterToOldRight(centerCube), 1))
			CubeFaceAlpha(cPolygon, 1)
			cPolygon.draw(VarData.gameWindow)
		elif compIndex == 7:
			cPolygon = Polygon(CubeFaceCoords(centerCube, 0))
			CubeFaceAlpha(cPolygon, 0)
			cPolygon.draw(VarData.gameWindow)
		pass

	pointA, pointB = ComponentCoords(centerCube, compOrder[compIndex])
	DrawComponent(alpha, pointA, pointB)

# Draw Line for Component
def DrawComponent(alpha, pointA, pointB):
	cLine = Line(pointA, pointB)
	cLine.setWidth(VarData.cubeSideWidth)
	cLine.setOutline(color_rgb(alpha, alpha, alpha))
	cLine.draw(VarData.gameWindow)

# Relative Line Coordinates Retrieval
def ComponentCoords(centerCube, component):
	xC = centerCube.getX()
	yC = centerCube.getY()
	sideL = VarData.cubeSideLength

	topPoint = Point(xC, yC - sideL)
	topLeftPoint = Point(xC - sideL*sqrt(3)/2, yC - sideL/2.)
	topRightPoint = Point(xC + sideL*sqrt(3)/2, yC - sideL/2.)

	botPoint = Point(xC, yC + sideL)
	botLeftPoint = Point(xC - sideL*sqrt(3)/2, yC + sideL/2.)
	botRightPoint = Point(xC + sideL*sqrt(3)/2, yC + sideL/2.)

	rightTop = Point(xC + sideL*sqrt(3), yC)
	rightBot = Point(xC + sideL*sqrt(3), yC + sideL)

	leftTop = Point(xC - sideL*sqrt(3), yC)
	leftBot = Point(xC - sideL*sqrt(3), yC + sideL)

	if component == 0:
		pointA, pointB = topPoint, topLeftPoint
	elif component == 1:
		pointA, pointB = topPoint, topRightPoint
	elif component == 2:
		pointA, pointB = topLeftPoint, centerCube
	elif component == 3:
		pointA, pointB = topRightPoint, centerCube
	elif component == 4:
		pointA, pointB = topLeftPoint, botLeftPoint
	elif component == 5:
		pointA, pointB = centerCube, botPoint
	elif component == 6:
		pointA, pointB = topRightPoint, botRightPoint
	elif component == 7:
		pointA, pointB = botLeftPoint, botPoint	
	elif component == 8:
		pointA, pointB = botRightPoint, botPoint
	elif component == 9:
		pointA, pointB = topRightPoint, rightTop
	elif component == 10:
		pointA, pointB = rightTop, rightBot
	elif component == 11:
		pointA, pointB = topLeftPoint, leftTop
	elif component == 12:
		pointA, pointB = leftTop, leftBot

	return pointA, pointB

# Relative Cube Face List
def CubeFaceCoords(centerCube, face):
	faceList = []
	if face == 0:
		faceList.append(CubeComponentA(centerCube, 0))
		faceList.append(CubeComponentB(centerCube, 0))
		faceList.append(centerCube)
		faceList.append(CubeComponentB(centerCube, 1))
	elif face == 1:
		faceList.append(CubeComponentA(centerCube, 2))
		faceList.append(centerCube)
		faceList.append(CubeComponentB(centerCube, 7))
		faceList.append(CubeComponentA(centerCube, 7))
	elif face == 2:
		faceList.append(CubeComponentA(centerCube, 3))
		faceList.append(centerCube)
		faceList.append(CubeComponentB(centerCube, 8))
		faceList.append(CubeComponentA(centerCube, 8))
	elif face == 3:
		faceList.append(CubeComponentB(centerCube, 1))
		faceList.append(CubeComponentA(centerCube, 1))
		oldCenter = CubeCenterToOldLeft(centerCube)
		faceList.append(CubeComponentA(oldCenter, 9))
		faceList.append(CubeComponentB(oldCenter, 9))
	elif face == 4:
		faceList.append(CubeComponentB(centerCube, 0))
		faceList.append(CubeComponentA(centerCube, 0))
		oldCenter = CubeCenterToOldRight(centerCube)
		faceList.append(CubeComponentA(oldCenter, 11))
		faceList.append(CubeComponentB(oldCenter, 11))
	return faceList

# Return Point A
def CubeComponentA(centerCube, component):
	pointA, pointB = ComponentCoords(centerCube, component)
	return pointA

# Return Point B
def CubeComponentB(centerCube, component):
	pointA, pointB = ComponentCoords(centerCube, component)
	return pointB

# Return Cube Center (to the left)
def CubeCenterToOldLeft(centerCube):
	return Point(VarData.originalCenterCube.getX(), centerCube.getY() - VarData.cubeSideLength*1.5)

# Return Cube Center (to the right)
def CubeCenterToOldRight(centerCube):
	return Point(VarData.originalCenterCube.getX() + VarData.cubeSideLength*sqrt(3)/2, centerCube.getY() - VarData.cubeSideLength*1.5)

# Draw Cube Face
def CubeFaceAlpha(polygonFace, face):
	cubeFaceAlpha = VarData.cubeFaceStartAlpha - face * VarData.cubeFaceDAlpha
	polygonFace.setFill(color_rgb(cubeFaceAlpha, cubeFaceAlpha, cubeFaceAlpha))
	polygonFace.setOutline(color_rgb(cubeFaceAlpha, cubeFaceAlpha, cubeFaceAlpha))
	polygonFace.setOutline(color_rgb(cubeFaceAlpha, cubeFaceAlpha, cubeFaceAlpha))

# Check if Percentage Exists
def PercentageExists(percentage):
	for index in VarData.displayedPercentages:
		if percentage == index:
			return True
	return False

# Draw Percentage
def DrawPercent(yMult):
	if yMult != 10:
		percentText = Text(Point(675, VarData.originalCenterCube.getY() + yMult * (VarData.cubeSideLength * 14 / 10)), str(yMult * 10) + "%")
		percentText.setFace("helvetica")
		percentText.setSize(9)
		percentText.setFill(color_rgb(150, 150, 150))
		percentText.draw(VarData.gameWindow)
	else:
		percentText = Text(Point(677, VarData.originalCenterCube.getY() + VarData.cubeSideLength * 16), "100%")
		percentText.setFace("helvetica")
		percentText.setSize(14)
		percentText.setStyle("bold")
		percentText.setFill(color_rgb(120, 120, 120))
		percentText.draw(VarData.gameWindow)

# Draw Greyscale Fireball
def DrawWinningFireball():
	fireX = VarData.originalCenterCube.getX() + sin(pi/3)*VarData.cubeSideLength
	fireY = VarData.originalCenterCube.getY() + VarData.cubeSideLength * 16
	fireballImg = Image(Point(fireX, fireY), "Mac Eng Fireball.ppm")
	fireballImg.draw(VarData.gameWindow)

# Button Progress Meter Constructor
def DrawPlaceholder():
	DrawPlaceholderBars()
	DrawPlaceholderBackground()
	DrawPlaceholderText()
	DrawPlaceholderBorder()

# Draw Progress Meter Placeholder Lines
def DrawPlaceholderBars():
	for coords in range(-100, 530, 75):
		botX = topX = 0
		botY = topY = 0

		if coords + 250 > 520:
			botY = 520
		else:
			botY = coords+250

		if coords < 110:
			topY = 110
		else:
			topY = coords

		if botY == 520:
			botX = -(520 - coords)*14./25 + 790
		else:
			botX = 650

		if topY == 110:
			topX = -(110 - coords)*14./25 + 790
		else:
			topX = 790

		diagonalBar = Line(Point(botX, botY), Point(topX, topY))
		diagonalBar.setFill(color_rgb(230, 230, 230))
		diagonalBar.setWidth(8)
        
		diagonalBar.draw(VarData.gameWindow)

# Draw Progress Meter Placeholder White Background
def DrawPlaceholderBackground():
	whiteBackground = Rectangle(Point(695,190), Point(745,440))
	whiteBackground.setFill("white")
	whiteBackground.draw(VarData.gameWindow)

# Draw Progress Meter Placeholder "Locked" Text
def DrawPlaceholderText():
	placeholderText = "Locked"

	for textIndex in range(6):
		lockText = Text(Point(720, 215 + textIndex * 40), placeholderText[textIndex])
		lockText.setFace("helvetica")
		lockText.setStyle("italic")
		lockText.setSize(28)
		lockText.setTextColor(color_rgb(160,160,160))
		lockText.draw(VarData.gameWindow)

# Draw Progress Meter Placeholder "Locked" Border
def DrawPlaceholderBorder():
	for width in range(6):
		backgroundBorder = Rectangle(Point(695+width,190+width), Point(745-width,440-width))
		alphaBackground = 255 - 10 * width
		backgroundBorder.setOutline(color_rgb(alphaBackground,alphaBackground,alphaBackground))
		backgroundBorder.draw(VarData.gameWindow)