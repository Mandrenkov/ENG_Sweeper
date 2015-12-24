# Mikhail Andrenkov
# Winter 2014 McMaster Python Game Challenge
# VarData Module

from graphics import GraphWin, Point

# Stores Cross-Module / Global Variables and Objects

# Title and Menu Winow (menuWindow) - VarData
# Difficulty Selection Window (diffWindow)
# Game Window (gameWindow)
# Game Over Window (endWindow)

# Lower and Upper Grid Contents (lGridContents, uGridContents)
# Amount of Mines (mineCount)
# Current Amount of Tiles (tileCount)
# Amount of Safe Tiles (safeTiles)

# Initial System Time (initialTime)
# Allowed Time (allowedTime)
# Game Time (gameTime)
# Game Over Animation (gameOverAnimation)

# Timer Text Object (timer)
# Time limit where delta t -> x (timeAppEnd) and (maxTimeText)

# Game Window currently being used for Grid Drawing (gameWinUsed)

# User clicks on first grid cell
gameStarted = False

# State of flag toggle
flagState = False
# Current Flag Coords (currentFlags)

# Grid cell colours
colourTuples = []

# Progress Bar Variables
cubeSideLength = 21
cubeSideWidth = 1
cubeFaceStartAlpha = 200
cubeFaceDAlpha = 35
originalCenterCube = Point(720, 170)

displayedPercentages = []

iSleepDelay = 0.05

# Current High Score (currentHighScore)

# Opening Screen "ENG" (oENG)
# Opening Screen "Sweeper" (oSweeper)
# Opening Screen msgLine1 (oMsg1)
# Opening Screen msgLine2 (oMsg2)
# Opening Screen botKochPoly (oBotKoch)
# Opening Screen botKochRect (oBotRect)

# Current Instructions (currentPanel)