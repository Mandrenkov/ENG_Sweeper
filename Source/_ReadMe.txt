ENG Sweeper Development Notes
=============================
  Contest: Winter 2014 Python Game Challenge
  Developer: Mikhail Andrenkov
  Submission Date: December 21, 2014

  ENG Sweeper Contact Support: ENGSweeper@gmail.com
      - Please see "Bug Report" before submitting a formal complaint

ReadMe Overview
--------------------------
 - Execute "_RunMe.py" to play ENG Sweeper

 - Ensure that the system requirements are satisfied
 - See "High Scores" for details regarding high score sharing and storage
 - See "Bug Report" for insight into known glitches and bugs
 
System Requirements
-------------------------------
  - Python 2.7.8 is recommended
      - Available at: https://www.python.org/downloads/release/python-278/
      - Other versions are not guaranteed to perform as intended

  - Graphics Module "graphics.py" by John M. Zelle, Fall 2010
      - Available at: http://mcsp.wartburg.edu/zelle/python/
      - A copy of the Graphics Module has been included for your convenience
  
  * Note: ENG Sweeper was developed and tested using a Windows 8.1 x64 computer.  The game was not tested on other platforms, and as such, its performance is not guaranteed.

High Scores
-----------------
  - High scores are calculated using a reciprocal exponential function of time that is multiplied by an attributed difficulty factor

  - The current high score is stored in "HS.txt"
      - If no such file exists, it will be automatically generated
      - If the file is corrupted, a new one will be automatically generated

  - To share your high score with another person, simply replace the contents of their HS.txt file with your own HS.txt file
  
  * Bonus Challenge:  Crack the HS.txt encryption/decryption algorithm (they're complimentary processes)
      - Be warned: corrupting the file may warrant automatic file replacement
      - Alternatively, you can locate the corresponding encryption/decryption code in the source files (I won't be mad, only slightly disappointed)

Bug Report
----------------
  The software architecture underlying the actual game mechanisms relies on multithreading, which, unfortunately, is not fully supported in the graphics.py module.  This results in two established glitches:

     A)  On occasion, the game will crash.  To my best knowledge, this event only occurs on the first grid click, and as such, is unlikely to interrupt a promising game.
     
     B)  Sometimes, the on-screen timer is dysfunctional or simply does not appear.  Fortunately, the internal game timer is not subjected to the same experience, and the final game score is correctly calculated.

  Correcting these bugs would require a complete overhaul of program structure and layout, as they cannot be eliminated or contained using try/except statements or the like.  Since these errors (and their sources) were discovered relatively late in the development process, they were not resolved.  Although this leaves room for improvement, the current build is still stable enough to support an enjoying experience.

Disclaimer
---------------
  I have previously created a Minesweeper application using LWJGL (including OpenGL) in Java.  Although no source code was transferred, the general overarching game principles are implemented into ENG Sweeper.