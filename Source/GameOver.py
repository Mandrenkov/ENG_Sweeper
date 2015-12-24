# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# GameOver Module

import VarData
import Grid, Input, time, EndGame
from random import randint

# Manual Constructor
def GameOverMain(finalGameState):
	VarData.gameStarted = False
	VarData.gameOverAnimation = True

	if finalGameState == "Loss":
		Loss(True)
	elif finalGameState == "Time Loss":
		Loss(False)
	elif finalGameState == "Win":
		Win()

	VarData.gameOverAnimation = False

	# Close the Game Window
	Input.CloseWindow(VarData.gameWindow)

	# Game Over Window
	EndGame.EndGameMain(finalGameState)

# Game Loss
def Loss(mineClick):
	gridLossPattern = []

	for row in range(10):
		tempRow = []
		for col in range(15):
			if VarData.lGridContents[row][col] == "-1":
				tempRow.append("Y")
			else:
				tempRow.append("N")
		gridLossPattern.append(tempRow)

	if mineClick:
		FadeMine(VarData.lastRow, VarData.lastCol)
		FadeMines(VarData.lastRow, VarData.lastCol)
		DrawRestofMines(gridLossPattern)
	else:
		FadeMines()
		DrawRestofMines(gridLossPattern)

# Fade Specified Mine to Black
def FadeMine(row, col):
	for alpha in range(0, 255, 4):
		Grid.UpdateLossGridDrawing(row, col, 255 - alpha)
		time.sleep(0.01)
	time.sleep(0.1)
	
# Fade Other Mines
def FadeMines(rowExcept = -1, colExcept = -1):
	increment = 4
	if VarData.difficulty > 1:
		increment += 1
	for alpha in range(0, 255, increment):
		for row in range(10):
			for col in range(15):
				if row == rowExcept and col == colExcept:
					continue
				if VarData.lGridContents[row][col] == "-1":
					Grid.UpdateLossGridDrawing(row, col, 255 - alpha)

# Fade All Other Tiles to Black
def DrawRestofMines(gridLossPattern):
	for otherMines in range(150 - VarData.mineCount):
		row = col = 0
		while(gridLossPattern[row][col] == "Y"):
			row = randint(0,9)
			col = randint(0,14)
		gridLossPattern[row][col] = "Y"
		Grid.UpdateLossGridDrawing(row, col, 0)
		if otherMines % 2 == 0:
			time.sleep(0.001)
	time.sleep(0.4)

# Game Win
def Win():
	FinalTileFade()
	RingFade()

# Fade Final Tile White -> Blue -> White
def FinalTileFade():
	for alpha in range(255, 100, -4):
		Grid.UpdateWinGridDrawing(VarData.lastRow, VarData.lastCol, alpha, 255 - (255 - alpha)/3, 255)
		time.sleep(0.01)

	for alpha in range(100, 255, 4):
		Grid.UpdateWinGridDrawing(VarData.lastRow, VarData.lastCol, alpha, 255 - (255 - alpha)/3, 255)
		time.sleep(0.01)
	time.sleep(0.1)

# Fade all Tiles to White around Final Tile to White in Rings
def RingFade():
	xDiff = yDif = 0

	if VarData.lastCol < 8:
		xDiff = 14 - VarData.lastCol
	else:
		xDiff = VarData.lastCol

	if VarData.lastRow < 5:
		yDiff = 9 - VarData.lastRow
	else:
		yDiff = VarData.lastRow

	ringCount = 0

	if xDiff > yDiff:
		ringCount = xDiff
	else:
		ringCount = yDiff

	rings = []

	for element in range(1, ringCount+1):
		tempRing = []

		for iCell in range(-element, element + 1):
			hCell = VarData.lastCol + iCell

			if hCell < 0 or hCell > 14:
				continue
			if VarData.lastRow - element >= 0:
				tempRing.append([hCell, VarData.lastRow - element])
			if VarData.lastRow + element < 10:
				tempRing.append([hCell, VarData.lastRow + element])

		for iCell in range(-element + 1, element):
			vCell = VarData.lastRow + iCell

			if vCell < 0 or vCell > 9:
				continue
			if VarData.lastCol - element >= 0:
				tempRing.append([VarData.lastCol - element, vCell])
			if VarData.lastCol + element < 15:
				tempRing.append([VarData.lastCol + element, vCell])

		rings.append(tempRing)

	for currentRing in rings:
		for currentCells in currentRing:
			curRow, curCol = currentCells[1], currentCells[0]
			currentCell = VarData.lGridContents[curRow][curCol]
			Grid.UpdateLossGridDrawing(currentCells[1], currentCells[0], 255)
		time.sleep(0.02)

# Fade all Tiles to White around Final Tile to White in Rings
def RestartRingFade():
	xDiff = 14
	yDif = 9

	ringCount = 14

	rings = []

	for element in range(1, ringCount+1):
		tempRing = []

		for iCell in range(-element, element + 1):
			if iCell < 0 or iCell > 14:
				continue
			if -element >= 0:
				tempRing.append([iCell,-element])
			if element < 10:
				tempRing.append([iCell,element])

		for iCell in range(-element + 1, element):
			if iCell < 0 or iCell > 9:
				continue
			if -element >= 0:
				tempRing.append([-element, iCell])
			if element < 15:
				tempRing.append([element, iCell])

		rings.append(tempRing)

	for ringIndex in range(1, len(rings)):
		for currentCells in rings[ringIndex]:
			curRow, curCol = currentCells[1], currentCells[0]
			currentCell = VarData.lGridContents[curRow][curCol]
			Grid.UpdateLossGridDrawing(currentCells[1], currentCells[0], 240)
		for currentCells in rings[ringIndex - 1]:
			curRow, curCol = currentCells[1], currentCells[0]
			currentCell = VarData.lGridContents[curRow][curCol]
			Grid.UpdateLossGridDrawing(currentCells[1], currentCells[0], 255)
		time.sleep(0.005)

	for currentCells in rings[-1]:
		curRow, curCol = currentCells[1], currentCells[0]
		currentCell = VarData.lGridContents[curRow][curCol]
		Grid.UpdateLossGridDrawing(currentCells[1], currentCells[0], 255)

# Draw the Tile (Technically not "Clicked")
def DrawClickedSquare(gridRow, gridColumn, grid):
	if grid[gridRow][gridColumn] != "Y":
		time.sleep(0.01)
		grid[gridRow][gridColumn] = "Y"
        Grid.UpdateLossGridDrawing(gridRow, gridColumn)
        for nextRow in range(-1, 2):
            for nextColumn in range (-1, 2):
                # Current tile
                row = gridRow + nextRow
                column = gridColumn + nextColumn
                # Invalid row or column
                if (nextRow == 0 and nextColumn == 0) or row < 0 or row > 9 or column < 0 or column > 14 or grid[row][column] == "Y":
                    continue
                else:
                    DrawClickedSquare(row, column, grid)

# Reset VarData Variables
def ResetVarDataVars():
	del(VarData.displayedPercentages)
	VarData.displayedPercentages = []
	del(VarData.colourTuples)
	VarData.colourTuples = []
	del(VarData.originalCenterCube)