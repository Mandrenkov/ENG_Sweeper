# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# Game Module

from graphics import *
from time import *
from thread import *

import VarData
import Difficulty, Input, OutlineBars, GameBackground, Title, Grid, ProgressBar, Buttons, FlagMines, GameOver
from random import choice

# Manual Constructor
def MainGame(initGameWindow):
    GameOver.ResetVarDataVars()

    if initGameWindow:
        InitializeGameWindow()

    # Timer Thread
    start_new_thread(UpdateTimer,(False, False))

    # Initialize Mine Info
    VarData.mineCount, VarData.tileCount = 15 + 3 * VarData.difficulty, 0
    VarData.safeTiles = 150 - VarData.mineCount

    if initGameWindow:
        # Draw Initial Graphics
        DrawGraphics()
    else:
        CoverAllAreas()
        ProgressBar.MainProgressBar()
    
    # Pre-Game Loop
    VarData.uGridContents, VarData.lGridContents = [], []
    cellContents = PreGameLoop()

    finalGameState = "Quit"

    # Game Loop
    try:
        if VarData.uGridContents[0] != 0 and VarData.lGridContents[0] != 0 and cellContents != -1:
            VarData.gameWinUsed = True
            VarData.gameStarted = True
            finalGameState = GameLoop()
            if finalGameState == "X Loss" or finalGameState == "Quit":
                return None
            VarData.gameStarted = False
    except:
        return None
        pass

    if finalGameState == "X Loss" or finalGameState == "Quit":
        return None

    GameOver.GameOverMain(finalGameState)

    # Wait until game over animation is over
    while(VarData.gameOverAnimation == True):
        sleep(0.5)

# Initialize Game Window
def InitializeGameWindow(): 
    VarData.gameWindow = GraphWin("ENG Sweeper", 800, 600)
    VarData.gameWindow.setBackground("white")

# Before First Click
def PreGameLoop():   
    cellContents = 0

    if VarData.difficulty == 3:
        colourIndex = range(8)
        for index in range(8):
            randMult = choice(colourIndex)
            colour = 245 - randMult * 20
            VarData.colourTuples.append((colour,colour,colour))
            colourIndex.remove(randMult)
    else:
        for colour in range(245, 84, -20):
            VarData.colourTuples.append((colour,colour,colour))

    for colour in range(245, 84, -20):
        VarData.colourTuples.append((colour,colour,colour))

    while True:
        # Get Mouse Input
        try: 
            mouseX, mouseY = Input.GetMouseInput(VarData.gameWindow)
        except GraphicsError:
            return [0],[0],-1

        # User Clicks "Quit"
        if mouseX < 100 and mouseY > 530: 
            return [0],[0],-1

        # Difficulty Click
        if mouseX <= 90 and mouseY <= 95:
            Input.CloseWindow(VarData.gameWindow)

            VarData.difficulty = Difficulty.DifficultyMain()

            if VarData.difficulty != None:
                MainGame(True)

            return "X Loss"

        # Check which grid tile was clicked
        gridX, gridY = Input.GridClick(mouseX, mouseY)

        # A valid grid tile was clicked
        if gridX != -1 and gridY != -1:
            # Initialize Grid Contents
            VarData.uGridContents = Grid.InitializeUpperGrid("N")
            VarData.lGridContents = Grid.InitializeLowerGrid(gridX, gridY)
            cellContents = VarData.lGridContents[gridY][gridX]
            break

    # Draw Tiles to Grid
    if DrawClickedSquare(gridY, gridX, cellContents) == "Zero Mine":
        Grid.UpdateCellBorders()

    #Grid.DrawMineGrid() #Draw (cheating) mine grid

    # Update Grid Drawing
    for row in range(10):
        for column in range(15):
            if VarData.uGridContents[row][column] == "Y":
                Grid.UpdateGridDrawing(row, column, VarData.lGridContents[row][column])

    # Draw Power Buttons
    if VarData.difficulty == 0:
        Buttons.DrawPowerButtons()
    elif VarData.difficulty == 1:
        Buttons.DrawSingleButton()
    else:
        Buttons.DrawPlaceholder()

    # Update the cell borders
    Grid.UpdateCellBorders()

    return cellContents

# Main Game Loop (After First Click)
def GameLoop():
    mouseX = mouseY = 0
    VarData.currentFlags = []

    if VarData.difficulty != 3:
        FlagMines.MainFlagMines()
    else:
        FlagMines.DrawPlaceholder()
        ProgressBar.DrawPlaceholder()

    # Loop while the user does not click "Quit"
    while not(mouseX < 100 and mouseY > 530):
        gridX = -1
        gridY = -1

        # Get Mouse Input
        try:
            VarData.gameWinUsed = False
            mouseX, mouseY = Input.GetMouseInput(VarData.gameWindow)  
            VarData.gameWinUsed = True         
        except GraphicsError:
            VarData.gameWinUsed = False
            return "X Loss"

        if VarData.gameStarted == False: # Time Expired
            return "X Loss"

        if mouseX < 100 and mouseY > 530: # Quit Click
            return "Quit"

        # Difficulty Click
        if mouseX <= 90 and mouseY <= 95:
            VarData.gameStarted = False
            VarData.gameWinUsed = False

            sleep(0.15)

            Input.CloseWindow(VarData.gameWindow)

            VarData.difficulty = Difficulty.DifficultyMain()

            if VarData.difficulty != None:
                MainGame(True)

            return "X Loss"

        # Restart Click
        if 447 <= mouseX <= 553 and 10 <= mouseY <= 80:
            VarData.gameStarted = False
            VarData.gameWinUsed = False

            sleep(0.15)
            
            Grid.UpdateWinGridDrawing(0, 0, 255, 255, 255)
            GameOver.RestartRingFade()
            MainGame(False)

            return "X Loss"

        if mouseX < 640 and 95 < mouseY < 530:
            # Check which grid tile was clicked
            gridX, gridY = Input.GridClick(mouseX, mouseY)

        elif VarData.difficulty != 3 and mouseX > 640 and mouseY > 540:
            # Flag toggle
            VarData.flagState = not(VarData.flagState)
            FlagMines.UpdateToggle()

        if VarData.difficulty == 1 and 102 < mouseX < 640 and mouseY > 530:
            # Reveal Safe Mine Button
            if VarData.gameTime + 5 >= VarData.allowedTime:
                VarData.redTimerFlash = True  
                Title.DrawTimer()
            else:
                gridY, gridX = Grid.RevealSafeMine()
                VarData.flagState = False
                FlagMines.UpdateToggle()

                if gridX != -1 and gridY != -1:
                    VarData.initialTime -= 5

                VarData.blueTimerFlash = True  

        elif VarData.difficulty == 0 and 102 < mouseX < 372 and mouseY > 530:
            # Reveal Safe Mine Button       
            if VarData.gameTime + 5 >= VarData.allowedTime:
                VarData.redTimerFlash = True  
                Title.DrawTimer()
            else:
                gridY, gridX = Grid.RevealSafeMine()
                VarData.flagState = False
                FlagMines.UpdateToggle()

                if gridX != -1 and gridY != -1:
                    VarData.initialTime -= 5

                VarData.blueTimerFlash = True  

        elif VarData.difficulty == 0 and 372 < mouseX < 640 and mouseY > 530:
            # Reveal Mine Button          
            if VarData.gameTime + 20 >= VarData.allowedTime:
                VarData.redTimerFlash = True
                Title.DrawTimer()
            else:
                mineRevealed = Grid.RevealMine()
                if mineRevealed: 
                    VarData.initialTime -= 20
                VarData.blueTimerFlash = True  

        # Valid tile was clicked
        if gridX != -1 and gridY != -1:
            if VarData.flagState == False:
                cellContents = VarData.lGridContents[gridY][gridX]
                winState = DrawClickedSquare(gridY, gridX, cellContents)
                
                # Cell was clicked with no adjacent mines
                if winState == "Zero Mine":
                    Grid.UpdateCellBorders()

                # User clicked on mine
                if winState == "Loss":
                    VarData.lastRow = gridY
                    VarData.lastCol = gridX
                    return "Loss"

                # User revealed all of the safe tiles
                if VarData.tileCount == VarData.safeTiles:
                    VarData.lastRow = gridY
                    VarData.lastCol = gridX
                    return "Win" 

            else: #Flag toggle click
                if not(FlagMines.AlreadyKnown(gridY, gridX)) and not(FlagMines.FlagExists(gridY, gridX)):
                    Grid.UpdateGridFlags(gridY, gridX, "M")
                    VarData.currentFlags.append([gridY, gridX])

                elif FlagMines.FlagExists(gridY, gridX):
                    FlagMines.RemoveFlagIndex(gridY, gridX)
                    Grid.UpdateGridFlags(gridY, gridX, "NM")

# Draw and Update a Tile Input
def DrawClickedSquare(gridRow, gridColumn, cellContents):
    # User did not click on a mine
    if cellContents != "-1":
        updateBorders = False

        # Current tile has not yet been revealed
        if VarData.uGridContents[gridRow][gridColumn] != "Y":
            VarData.tileCount += 1
            if cellContents == "0":
                updateBorders = True

        # Update progress bar and grid, and indicate that the tile has been revealed
        if VarData.difficulty != 3:
            ProgressBar.DrawCubeComp()
        VarData.uGridContents[gridRow][gridColumn] = "Y"
        Grid.UpdateGridDrawing(gridRow, gridColumn, cellContents)

        # Empty cell
        if cellContents == "0":
            # Cycle through the adjacent rows
            for nextRow in range(-1, 2):
                # Cycle through the adjacent columns
                for nextColumn in range (-1, 2):
                    # Current tile
                    row = gridRow + nextRow
                    column = gridColumn + nextColumn
                    # Invalid row or column
                    if (nextRow == 0 and nextColumn == 0) or row < 0 or row > 9 or column < 0 or column > 14 or VarData.uGridContents[row][column] == "Y":
                        continue
                    # Reveal the adjacent tile
                    else:
                        DrawClickedSquare(row, column, VarData.lGridContents[row][column])
            if updateBorders:
                return "Zero Mine"
    else: # User clicked on a mine
        return "Loss"

# Draw Initial "Background" Graphics
def DrawGraphics():
    GameBackground.MainBackground() 
    ProgressBar.MainProgressBar()   
    OutlineBars.MainOutlineBars()
    Title.MainTitle()
    Grid.MainGrid()
    Buttons.MainButtons()
    
# Check How Many Tiles have Been Revealed
def UpdateTileCount(uGridContents):
    tileCount = 0
    for row in range(10):
        for column in range(15):
            if uGridContents[row][column] == "Y": tileCount += 1
    return tileCount

# Timer Thread
def UpdateTimer(placeHolderA, placeHolderB):
    startTimer = False

    VarData.blueTimerFlash = False
    VarData.redTimerFlash = False

    if VarData.difficulty == 0:
        VarData.allowedTime = 1E8 # Infinity (Wink Wink)
    elif VarData.difficulty == 1:
        VarData.allowedTime = 600
    elif VarData.difficulty == 2:
        VarData.allowedTime = 300
    elif VarData.difficulty == 3:
        VarData.allowedTime = 120

    while startTimer == False:
        startTimer = VarData.gameStarted

    VarData.gameTime = 0

    Title.DrawTimer()
    Title.DrawTimeLimit()

    VarData.initialTime = long(time())

    currentTime = VarData.initialTime

    finalTime = currentTime + VarData.allowedTime

    lastGameTime = -1

    while currentTime < finalTime and VarData.gameStarted:
        currentTime = long(time())
        VarData.gameTime = currentTime - VarData.initialTime

        while VarData.gameWinUsed:
            sleep(0.01)

        if lastGameTime != VarData.gameTime:
            lastGameTime = VarData.gameTime
            try:
                Title.DrawTimer()
            except GraphicsError:
                print "Time Error"
                break

            if VarData.gameTime >= VarData.allowedTime:
                VarData.gameStarted = False              
                GameOver.GameOverMain("Time Loss")
                break

        sleep(.1)

# Cover Areas (for Restart)
def CoverAllAreas():
    # Cover Progress Bar
    progCover = Rectangle(Point(645, 100), Point(VarData.gameWindow.getWidth(), 535))
    progCover.setFill("white")
    progCover.setOutline("white")
    progCover.draw(VarData.gameWindow)

    # Cover Buttons
    buttonCover = Rectangle(Point(105, 535), Point(635, VarData.gameWindow.getHeight()))
    buttonCover.setFill("white")
    buttonCover.setOutline("white")
    buttonCover.draw(VarData.gameWindow)

    # Cover Flag Toggle
    flagCover = Rectangle(Point(645, 545), Point(VarData.gameWindow.getWidth(), VarData.gameWindow.getHeight()))
    flagCover.setFill("white")
    flagCover.setOutline("white")
    flagCover.draw(VarData.gameWindow)

    # Cover Timer
    timeCover = Rectangle(Point(605, 0), Point(VarData.gameWindow.getWidth(), 90))
    timeCover.setFill("white")
    timeCover.setOutline("white")
    timeCover.draw(VarData.gameWindow)