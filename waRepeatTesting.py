import time

import area.dreamZan
import loadGame
import logs
import memory.main
import reset
import screen
import xbox

FFXC = xbox.controllerHandle()

selfAuto = True
print("Looping section: Bevelle Trials")

memory.main.start()

attempts = 0
success = 0
while attempts < 20:
    attempts += 1

    area.dreamZan.NewGame('Luca')
    loadGame.loadOffset(1)

    print("Game start screen")
    screen.clearMouse(0)

    startTime = logs.timeStamp()
    print("Timer starts now.")
    # ---------This is the actual movement/code/logic/etc---------------
    import area.luca as luca
    import blitz

    luca.blitzStart()
    blitzWin = blitz.blitzMain(False)
    if blitzWin:
        success += 1

    # ---------End of the actual movement/code/logic/etc---------------
    endTime = logs.timeStamp()
    print("Duration:", endTime - startTime)

    if attempts < 20:
        print("------------------------------")
        print("------------------------------")
        print("Test number", attempts, "is complete.")
        print("Blitzball wins:", success)
        print("------------------------------")
        print("------------------------------")
        time.sleep(5)

        print("Resetting.")

        reset.resetToMainMenu()
    else:
        print("------------------------------")
        print("------------------------------")
        print("Testing is complete.")
        print("Attempts:", attempts)
        print("Success count:", success)
        print("------------------------------")
        print("------------------------------")

time.sleep(5)

memory.main.end()

time.sleep(5)
print("--------------------------")
print("Program - end")
print("--------------------------")
