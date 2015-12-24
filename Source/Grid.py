# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# Grid Module

import VarData

from graphics import *
from random import randrange

# Manual Constructor
def MainGrid():
	DrawInitGrid()

# Update Grid
def UpdateGrid(gridContents, row, column, newValue):
	gridContents[row][column] = newValue

# Initialize Visible Grid
def InitializeUpperGrid(default):
	gridContents = []
	for row in range(10):
		tempRow = []
		for column in range(15):
			tempRow.append(default)
		gridContents.append(tempRow)
		del(tempRow)
	return gridContents

# Initialize "Grid Data" Grid
def InitializeLowerGrid(gridX, gridY):
    gridContents = InitializeUpperGrid("0")

    mine = 0
    while (mine < VarData.mineCount):
        xMine = randrange(0, 15)
        yMine = randrange(0, 10)
        if xMine == gridX and yMine == gridY:
            continue
        if gridContents[yMine][xMine] == "0":
            gridContents[yMine][xMine] = "-1"
            mine += 1

    for row in range(10):
        for column in range(15):
            if gridContents[row][column] == "-1":
                UpdateSurroundingCells(gridContents, row, column)

    return gridContents

# Reveal Surrounding Tiles
def UpdateSurroundingCells(gridContents, mineRow, mineColumn):
    for xCheck in range(-1,2):
        for yCheck in range(-1,2):
            row = mineRow + yCheck
            column = mineColumn + xCheck
            if row < 0 or row > 9 or column < 0 or column > 14:
                continue
            if gridContents[row][column] != "-1":
                gridContents[row][column] = str(eval(gridContents[row][column]) + 1)
    
    return gridContents

# Draw Initial Grid
def DrawInitGrid():
    gridBoxAttributes = [17, 618, 111, 512, 40]
    # 1 => coordXi, 2 => coordXf, 3 => coordYi, 4 => coordYf, 5 => sideLength
    backgroundAlpha = 195

    DrawGridBorder(gridBoxAttributes, backgroundAlpha)

    for row in range(gridBoxAttributes[0], gridBoxAttributes[1] - gridBoxAttributes[4], gridBoxAttributes[4]):
        for column in range(gridBoxAttributes[2], gridBoxAttributes[3] - gridBoxAttributes[4], gridBoxAttributes[4]):
            gridBox = Rectangle(Point(row, column), Point(row + gridBoxAttributes[4], column + gridBoxAttributes[4]))

            gridBox.setFill("white")
            gridBox.setOutline(color_rgb(backgroundAlpha, backgroundAlpha, backgroundAlpha))
            gridBox.draw(VarData.gameWindow)

# Draw Grid with Visible Mines *Cheat Mode*
def DrawMineGrid():
    gridBoxAttributes = [17, 618, 111, 512, 40]
    # 1 => coordXi, 2 => coordXf, 3 => coordYi, 4 => coordYf, 5 => sideLength
    backgroundAlpha = 185

    DrawGridBorder(gridBoxAttributes, backgroundAlpha)

    for row in range(gridBoxAttributes[0], gridBoxAttributes[1] - gridBoxAttributes[4], gridBoxAttributes[4]):
        for column in range(gridBoxAttributes[2], gridBoxAttributes[3] - gridBoxAttributes[4], gridBoxAttributes[4]):
            gridBox = Rectangle(Point(row, column), Point(row + gridBoxAttributes[4], column + gridBoxAttributes[4]))

            rowIndex = (row - gridBoxAttributes[0])/gridBoxAttributes[4]
            columnIndex = (column - gridBoxAttributes[2])/gridBoxAttributes[4]

            if VarData.lGridContents[columnIndex][rowIndex] == "-1":
                gridBox.setFill("black")
            elif VarData.lGridContents[columnIndex][rowIndex] != "0":
                alpha = 255 - eval(VarData.lGridContents[columnIndex][rowIndex])*50
                gridBox.setFill(color_rgb(alpha, alpha, alpha))

            gridBox.setOutline(color_rgb(backgroundAlpha, backgroundAlpha, backgroundAlpha))
            gridBox.draw(VarData.gameWindow)

# Draw Border for Grid
def DrawGridBorder(gridBoxAttributes, backgroundAlpha):
    barWidth = 16   
    halfWidth = barWidth/2

    deltaBackgroundAlpha = 255 - backgroundAlpha

    #Top of Grid
    for bar in range(halfWidth):
        lPoint1 = Point(gridBoxAttributes[0], gridBoxAttributes[2] - barWidth/2 + bar)
        lPoint2 = Point(gridBoxAttributes[1], gridBoxAttributes[2] - barWidth/2 + bar)
        aLine = Line(lPoint1, lPoint2)
        alpha = 255 - deltaBackgroundAlpha/halfWidth * bar
        aLine.setFill(color_rgb(alpha, alpha, alpha))
        aLine.draw(VarData.gameWindow)

    #Bottom of Grid
    for bar in range(halfWidth):
        lPoint1 = Point(gridBoxAttributes[0], gridBoxAttributes[3] + bar)
        lPoint2 = Point(gridBoxAttributes[1], gridBoxAttributes[3] + bar)
        aLine = Line(lPoint1, lPoint2)
        alpha = backgroundAlpha + deltaBackgroundAlpha/halfWidth * bar
        aLine.setFill(color_rgb(alpha, alpha, alpha))
        aLine.draw(VarData.gameWindow)

    #Left of Grid
    for bar in range(halfWidth):
        lPoint1 = Point(gridBoxAttributes[0] - barWidth/2 + bar, gridBoxAttributes[2])
        lPoint2 = Point(gridBoxAttributes[0] - barWidth/2 + bar, gridBoxAttributes[3])
        aLine = Line(lPoint1, lPoint2)
        alpha = 255 - deltaBackgroundAlpha/halfWidth * bar
        aLine.setFill(color_rgb(alpha, alpha, alpha))
        aLine.draw(VarData.gameWindow)

    #Right of Grid
    for bar in range(halfWidth):
        lPoint1 = Point(gridBoxAttributes[1] + barWidth/2 - bar - 1 , gridBoxAttributes[2])
        lPoint2 = Point(gridBoxAttributes[1] + barWidth/2 - bar - 1, gridBoxAttributes[3])
        aLine = Line(lPoint1, lPoint2)
        alpha = 255 - deltaBackgroundAlpha/halfWidth * bar
        aLine.setFill(color_rgb(alpha, alpha, alpha))
        aLine.draw(VarData.gameWindow)

    #Corners
    for cornerX in range(-1,2,2):
        for cornerY in range(-1, 2, 2):
            for corner in range(halfWidth):
                rPoint1 = Point(gridBoxAttributes[int(bool(cornerX + 1))], gridBoxAttributes[int(bool(cornerY + 1)) + 2])
                rPoint2 = Point(gridBoxAttributes[int(bool(cornerX + 1))] + cornerX*(halfWidth - corner), gridBoxAttributes[int(bool(cornerY + 1)) + 2] + cornerY*(halfWidth - corner))
                aRect = Rectangle(rPoint1, rPoint2)
                alpha = 255 - deltaBackgroundAlpha/halfWidth * corner
                aRect.setOutline(color_rgb(alpha, alpha, alpha))
                aRect.draw(VarData.gameWindow)

# Update Grid Drawing
def UpdateGridDrawing(rowIndex, columnIndex, state):  
    clearCell = Rectangle(Point(18 + 40 * columnIndex, 112 + 40 * rowIndex), Point(56 + 40 * columnIndex, 150 + 40 * rowIndex))
    clearCell.setFill("white")
    clearCell.setOutline("white")
    clearCell.draw(VarData.gameWindow)

    if VarData.difficulty == 3 or state == "0":
        DeleteGridCell(rowIndex, columnIndex, state)
        return None

    alpha = VarData.colourTuples[eval(state)][0] - 85
    
    DrawTextBackground(rowIndex, columnIndex, state)

    if VarData.difficulty < 2:
        Number = Text(Point(37 + 40 * columnIndex, 131 + 40 * rowIndex), state)
        Number.setFace("arial")
        Number.setStyle("normal")
        Number.setSize(11)
        Number.setFill(color_rgb(alpha, alpha, alpha))
        Number.draw(VarData.gameWindow) 
        return None

    binNum = str(bin(eval(state)))[2:]

    Number = Text(Point(34 + 40 * columnIndex, 131 + 40 * rowIndex), binNum)
    Number.setFace("arial")
    Number.setStyle("normal")
    if state != "8":
        Number.setSize(11)
    else:
        Number.setSize(8)
    Number.setFill(color_rgb(alpha, alpha, alpha))
    Number.draw(VarData.gameWindow) 
    xBase = 0

    if eval(state) < 2:
        xBase = Number.getAnchor().getX() + 6
    elif eval(state) < 4:
        xBase = Number.getAnchor().getX() + 12
    elif eval(state) < 8:
        xBase = Number.getAnchor().getX() + 16
    else:
        xBase = Number.getAnchor().getX() + 15

    Base = Text(Point(xBase, 137 + 40 * rowIndex), "2")
    Base.setFace("arial")
    Base.setStyle("normal")
    Base.setSize(8)
    Base.setFill(color_rgb(alpha + 10, alpha + 10, alpha + 10))
    Base.draw(VarData.gameWindow)      

# Fade Tile to Black
def UpdateLossGridDrawing(gridRow, gridCol, alpha):
    lossCell = Rectangle(Point(17 + 40 * gridCol, 111 + 40 * gridRow), Point(57 + 40 * gridCol, 151 + 40 * gridRow))
    lossCell.setFill(color_rgb(alpha, alpha, alpha))
    lossCell.setOutline(color_rgb(195, 195, 195))
    try:
        lossCell.draw(VarData.gameWindow)
    except ValueError:
        pass
    except GraphicsError:
        pass

# Fade Tile to White
def UpdateWinGridDrawing(gridRow, gridCol, clrR, clrG, clrB):
    lossCell = Rectangle(Point(17 + 40 * gridCol, 111 + 40 * gridRow), Point(57 + 40 * gridCol, 151 + 40 * gridRow))
    lossCell.setFill(color_rgb(clrR, clrG, clrB))
    lossCell.setOutline(color_rgb(195, 195, 195))
    try:
        lossCell.draw(VarData.gameWindow)
    except ValueError:
        pass
    except GraphicsError:
        pass

# Draw Grid Flag
def UpdateGridFlags(rowIndex, columnIndex, state):
    emptyCell = Rectangle(Point(18 + 40 * columnIndex, 112 + 40 * rowIndex), Point(56 + 40 * columnIndex, 150 + 40 * rowIndex))
    emptyCell.setFill("white")
    emptyCell.setOutline("white")
    emptyCell.draw(VarData.gameWindow)

    if state == "NM":
        return None

    centerCellX = 37 + 40 * columnIndex
    centerCellY = 131 + 40 * rowIndex

    flag1 = Text(Point(centerCellX, centerCellY - 10), "1")
    flagBar = Text(Point(centerCellX + 1, centerCellY - 7), "__")
    flag0 = Text(Point(centerCellX, centerCellY + 10), "0")

    flag1.setFace("arial")
    flag1.setSize(10)

    flagBar.setFace("arial")
    flagBar.setSize(10)
    flagBar.setStyle("bold")

    flag0.setFace("arial")
    flag0.setSize(10)

    flag0.setFill(color_rgb(150, 150, 150))
    flagBar.setFill(color_rgb(150, 150, 150))
    flag1.setFill(color_rgb(150, 150, 150))

    flag1.draw(VarData.gameWindow)
    flagBar.draw(VarData.gameWindow)
    flag0.draw(VarData.gameWindow)

# Draw Tile Background
def DeleteGridCell(rowIndex, columnIndex, colourTupleIndex):
    emptyCell = Rectangle(Point(17 + 40 * columnIndex, 111 + 40 * rowIndex), Point(57 + 40 * columnIndex, 151 + 40 * rowIndex))
    colourTuple = VarData.colourTuples[eval(colourTupleIndex)]
    emptyCell.setFill(color_rgb(colourTuple[0], colourTuple[1], colourTuple[2]))
    emptyCell.setOutline(color_rgb(colourTuple[0] - 10, colourTuple[1] - 10, colourTuple[2] - 10))
    emptyCell.draw(VarData.gameWindow)

# Draw Tile Text and Border
def DrawTextBackground(rowIndex, columnIndex, colourTupleIndex):
    colourTupleAlpha = VarData.colourTuples[eval(colourTupleIndex)][0]
    for size in range(5):
        whiteSpace = Rectangle(Point(17 + 40 * columnIndex + size, 111 + 40 * rowIndex + size), Point(57 + 40 * columnIndex - size, 151 + 40 * rowIndex - size))
        whiteAlpha = colourTupleAlpha + size * (255. - colourTupleAlpha)/9.
        whiteSpace.setOutline(color_rgb(whiteAlpha, whiteAlpha, whiteAlpha))
        whiteSpace.draw(VarData.gameWindow)

# Layer Tile Borders
def UpdateCellBorders():
    for tileNum in range(1,9):
        for row in range(10):
            for col in range(15):
                if VarData.uGridContents[row][col] == 'Y' and VarData.lGridContents[row][col] == str(tileNum):
                    border = Rectangle(Point(17 + 40 * col, 111 + 40 * row), Point(57 + 40 * col, 151 + 40 * row))
                    colourTuple = VarData.colourTuples[tileNum]
                    border.setOutline(color_rgb(colourTuple[0] - 10, colourTuple[1] - 10, colourTuple[2] - 10))
                    border.draw(VarData.gameWindow)

# Reveal Safe Tile
def RevealSafeMine():
    if not(SafeTileExists()):
        return -1, -1

    while True:
        randX = randrange(0, 15)
        randY = randrange(0, 10)

        if VarData.uGridContents[randY][randX] == 'N' and VarData.lGridContents[randY][randX] != "-1":
            return randY, randX

# Checks if Safe Tile Exists
def SafeTileExists():
    for row in range(10):
        for col in range(15):
            if VarData.uGridContents[row][col] == 'N' and VarData.lGridContents[row][col]  != "-1":
                return True
    return False

# Reveal Mine
def RevealMine():
    if not(UnflagedMineExists()):
        return False

    rowList = range(10)
    colList = range(15)

    if len(VarData.currentFlags) % 4 == 1:
        rowList = range(9, -1, -1)
    elif len(VarData.currentFlags) % 4 == 2:
        rowList = range(9, -1, -1)
        colList = range(14, -1, -1)
    if len(VarData.currentFlags) % 4 == 3:
        colList = range(14, -1, -1)

    for row in rowList:
        for col in colList:
            if VarData.lGridContents[row][col] == '-1' and not(FlagIndexExists(row, col)):
                VarData.currentFlags.append([row, col])
                UpdateGridFlags(row, col, "M")
                return True

# Check if Unflagged Mine Exists (Typo Alert!)
def UnflagedMineExists():
    for row in range(10):
        for col in range(15):
            if VarData.lGridContents[row][col] == '-1' and not(FlagIndexExists(row, col)):
                return True
    return False

# Check if Flag Index Exists
def FlagIndexExists(row, col):
    for flag in VarData.currentFlags:
        if flag[0] == row and flag[1] == col:
            return True
    return False