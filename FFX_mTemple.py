import time
import FFX_Xbox
import FFX_Screen
import FFX_Battle
import FFX_menu
import FFX_Logs
import FFX_memory
import FFX_targetPathing

FFXC = FFX_Xbox.FFXC

def approach():
    print("------------------------------------------Affection array:")
    print(FFX_memory.affectionArray())
    print("------------------------------------------")
    FFX_memory.clickToControl()
    print("Approaching Macalania Temple")
    
    checkpoint = 0
    while FFX_memory.getMap() != 106:
        if FFX_memory.userControl():
            #Map changes
            if checkpoint < 2 and FFX_memory.getMap() == 153:
                checkpoint = 2
            
            #General pathing
            elif FFX_targetPathing.setMovement(FFX_targetPathing.mTempleApproach(checkpoint)) == True:
                checkpoint += 1
                print("Checkpoint reached: ", checkpoint)
        else:
            FFXC.set_value('AxisLx', 0)
            FFXC.set_value('AxisLy', 0)
            if FFX_memory.diagSkipPossible():
                FFX_Xbox.tapB()
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 0)

def arrival(blitzWin):
    print("Starting Macalania Temple section")
    FFX_memory.awaitControl()
    #if FFX_memory.getPower() < 26:
    #    FFX_memory.setPower(26) #Need 34 total from here forward. 2 from Wendigo and 6 from bombs. 26 needed here.
    FFX_menu.macTemple(blitzWin)
    
    #Movement:
    checkpoint = 0
    skipStatus = True
    while FFX_memory.getMap() != 80:
        if FFX_memory.userControl():
            #Main events
            if checkpoint == 1:
                FFXC.set_value('AxisLy', 0)
                FFXC.set_value('AxisLx', 0)
                time.sleep(0.2)
                FFX_Xbox.touchSaveSphere()
                checkpoint += 1
            elif checkpoint == 4: #Talking to Trommell
                FFX_memory.clickToEventTemple(6)
                if FFX_memory.getCoords()[0] < 23.5:
                    time.sleep(0.07)
                    FFXC.set_value('AxisLx', 1)
                    time.sleep(0.035)
                    FFXC.set_value('AxisLx', 0)
                    time.sleep(0.4)
                checkpoint += 1
            elif checkpoint == 5: #Skip
                print("Lining up for skip.")
                FFXC.set_value('AxisLy', -1)
                FFXC.set_value('AxisLx', -1)
                time.sleep(0.25)
                FFXC.set_value('AxisLy', 0)
                FFXC.set_value('AxisLx', 0)
                time.sleep(0.3)
                FFXC.set_value('AxisLx', 1)
                time.sleep(0.085) #Shifting right
                FFXC.set_value('AxisLx', 0)
                time.sleep(0.2)
                FFXC.set_value('AxisLx', -1)
                time.sleep(0.04)
                FFXC.set_value('AxisLx', 0)
                time.sleep(0.3)
                
                print("Now lined up. Here we go.")
                FFXC.set_value('AxisLx', 1)
                time.sleep(0.08)
                FFXC.set_value('BtnB', 1)
                time.sleep(0.1)
                FFXC.set_value('BtnB', 0)
                time.sleep(1.5)
                FFXC.set_value('AxisLx', 0)
                print("Did it work? You decide!!!")
                checkpoint += 1
                FFX_memory.clickToControl3()
            elif checkpoint == 8: #Open chest
                FFX_memory.clickToEventTemple(7)
                checkpoint += 1
                
            elif checkpoint == 11:
                print("Check if skip is online")
                if FFX_memory.getStoryProgress() < 1505:
                    checkpoint += 1
                else:
                    checkpoint = 20
                    skipStatus = False
            elif checkpoint == 14: #Pause so we don't mess up the skip
                if skipStatus == True:
                    FFXC.set_value('AxisLy', 0)
                    FFXC.set_value('AxisLx', 0)
                    FFX_Xbox.SkipDialog(1.5)
                checkpoint += 1
            elif checkpoint < 16 and FFX_memory.getMap() == 239:
                checkpoint = 16
            
            #Recovery items
            elif checkpoint == 23: #Door, Jyscal room
                FFX_memory.clickToEventTemple(0)
                checkpoint += 1
            elif checkpoint == 24: #Back to the main room
                FFX_memory.clickToEventTemple(5)
                checkpoint += 1
            elif checkpoint == 27:
                checkpoint = 12
            
            
            #General pathing
            elif FFX_targetPathing.setMovement(FFX_targetPathing.templeFoyer(checkpoint)) == True:
                checkpoint += 1
                print("Checkpoint reached: ", checkpoint)
        else:
            FFXC.set_value('AxisLx', 0)
            FFXC.set_value('AxisLy', 0)
            if FFX_memory.diagSkipPossible():
                FFX_Xbox.tapB()

def startSeymourFight():
    FFX_memory.clickToControl()
    while FFX_targetPathing.setMovement([9, -53]) == False:
        doNothing = True #Allows us to move to the Seymour fight.
    FFXC.set_value('AxisLx', 1)
    FFXC.set_value('AxisLy', 0)
    FFX_memory.awaitEvent()
    FFXC.set_value('AxisLx', 0)
    FFXC.set_value('AxisLy', 0)
    
def oldSkipMovements():
    FFX_memory.awaitControl()
    FFXC.set_value('AxisLy', -1)
    time.sleep(1.3)
    FFXC.set_value('AxisLx', -1)
    time.sleep(0.3)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 0)
    time.sleep(0.3)
    FFXC.set_value('AxisLx', 1)
    time.sleep(0.085) #Shifting right
    FFXC.set_value('AxisLx', 0)
    time.sleep(0.2)
    FFXC.set_value('AxisLx', -1)
    time.sleep(0.04)
    FFXC.set_value('AxisLx', 0)
    time.sleep(0.2)
    FFX_Xbox.menuB()
    
    FFX_Screen.clickToPixel(666,439,(223, 223, 223))
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(0.8)
    
    success = 0
    reportSkip = 0
    while success == 0:
        #Engage the skip (at least try)
        FFXC.set_value('AxisLx', 1)
        time.sleep(0.08)
        FFXC.set_value('BtnB', 1)
        time.sleep(0.1)
        FFXC.set_value('AxisLx', 0)
        FFXC.set_value('BtnB', 0)
        time.sleep(1.5)
        if FFX_Screen.PixelTest(577,809,(23, 23, 23)):
            reportSkip = 1
            print("Jyscal Skip successful.")
            success = 1
            FFX_Xbox.menuB() #Skip dialog (first)
            time.sleep(1.5)
            FFX_Xbox.menuB() #Skip dialog (second)
            time.sleep(0.5)
            FFXC.set_value('AxisLy', 1)
            FFXC.set_value('AxisLx', -1)
            time.sleep(0.6)
            FFXC.set_value('AxisLx', 0)
            time.sleep(1)
            FFXC.set_value('AxisLx', -1)
            time.sleep(1)
            FFXC.set_value('AxisLy', 0)
            time.sleep(1)
            FFXC.set_value('AxisLx', 0)
            FFX_Xbox.menuB()
            time.sleep(2.5)
            FFX_Xbox.menuB()
            time.sleep(0.3)
            FFXC.set_value('AxisLx', -1)
            time.sleep(1.5)
            FFXC.set_value('AxisLx', 0)
            FFXC.set_value('AxisLy', -1)
            time.sleep(2.5)
            FFXC.set_value('AxisLy', 0)
            
            FFX_Xbox.SkipDialog(2)
            FFXC.set_value('AxisLy', -1)
            time.sleep(3.5)
            FFXC.set_value('AxisLy', 0) # Through the door
        else:
            print("Jyscal Skip failed. Going to try again.")
            FFX_Xbox.menuB() #Skip dialog (first)
            FFX_Screen.awaitMap1()
    
    #After the skip
    while not FFX_Screen.PixelTestTol(658,9,(100, 105, 97),5):
        if FFX_Screen.Minimap1():
            reportSkip = 2
            print("Jyscal Skip failed. Backup strats.")
            FFXC.set_value('AxisLx', -1)
            FFXC.set_value('AxisLy', 1)
            time.sleep(1.5)
            FFX_memory.clickToEvent()
            time.sleep(0.5)
            FFX_memory.clickToControl()
            FFXC.set_value('AxisLx', 1)
            FFXC.set_value('AxisLy', -1)
            time.sleep(1)
            FFXC.set_value('AxisLy', 0)
            time.sleep(3)
            FFXC.set_value('AxisLx', 0)
            FFXC.set_value('AxisLy', 0)
            FFX_memory.awaitControl() #A sphere in Lady Yuna's belongings?
            FFXC.set_value('AxisLx', 1)
            time.sleep(2)
            FFXC.set_value('AxisLx', 0)
            FFXC.set_value('AxisLy', 1)
            time.sleep(3)
            FFXC.set_value('AxisLy', 0)
            FFX_Screen.clickToPixel(215,224,(64, 193, 64)) #Jyscal scene
            FFXC.set_value('AxisLy', -1)
            time.sleep(1)
            FFXC.set_value('AxisLy', 0)
            FFX_Screen.awaitMap1()
            FFXC.set_value('AxisLy', -1)
            time.sleep(2.3)
            FFXC.set_value('AxisLy', 1)
            time.sleep(5)
            FFXC.set_value('AxisLy', 0)
        else:
            FFX_Xbox.menuB()
    
    FFX_Logs.writeStats("Jyscal skip:")
    if reportSkip == 1:
        FFX_Logs.writeStats("Yes")
    elif reportSkip == 2:
        FFX_Logs.writeStats("No")

def seymourFight():
    
    FFX_Battle.seymourGuado()
    
    time.sleep(1)
    FFX_Xbox.menuB()
    time.sleep(0.2)
    FFX_Xbox.menuUp()
    FFX_Xbox.menuB() #Confirm name for Shiva
    FFX_memory.awaitControl()
    FFXC.set_value('AxisLy', -1)
    FFXC.set_value('AxisLx', -1)
    time.sleep(0.4)
    FFXC.set_value('AxisLy', 0)
    time.sleep(4.5)
    FFXC.set_value('AxisLx', 0)

def trials():
    FFX_memory.awaitControl()
    
    checkpoint = 0
    while FFX_memory.getMap() != 153:
        if FFX_memory.userControl():
            #Map changes
            if checkpoint < 2 and FFX_memory.getMap() == 239:
                checkpoint = 2
            
            #Spheres and Pedestols
            elif checkpoint == 2:
                FFX_memory.awaitControl()
                print("Activate the trials")
                FFX_memory.clickToEventTemple(0)
                checkpoint += 1
            elif checkpoint == 9: #Push pedestol - 1
                FFXC.set_value('AxisLx', 1)
                FFXC.set_value('AxisLy', 0)
                FFX_memory.awaitEvent()
                FFXC.set_value('AxisLx', 0)
                FFXC.set_value('AxisLy', 0)
                time.sleep(1)
                checkpoint += 1
            elif checkpoint == 13: # Grab first Mac Sphere
                FFX_memory.clickToEventTemple(1)
                checkpoint += 1
            elif checkpoint == 17: # Place first Mac Sphere
                FFX_memory.clickToEventTemple(2)
                checkpoint += 1
            elif checkpoint == 20: # Grab glyph sphere
                FFX_memory.clickToEventTemple(2)
                checkpoint += 1
            elif checkpoint == 24: #Push pedestol - 2
                FFX_memory.clickToEventTemple(0)
                checkpoint += 1
            elif checkpoint == 29: #Push pedestol - 3
                FFXC.set_value('AxisLx', 1)
                FFXC.set_value('AxisLy', 0)
                FFX_memory.awaitEvent()
                FFXC.set_value('AxisLx', 0)
                FFXC.set_value('AxisLy', 0)
                time.sleep(1)
                checkpoint += 1
            elif checkpoint == 32: # Place Glyph sphere
                FFX_memory.clickToEventTemple(7)
                checkpoint += 1
            elif checkpoint == 39: # Grab second Mac sphere
                FFX_memory.clickToEventTemple(7)
                checkpoint += 1
            elif checkpoint == 46: # Place second Mac sphere
                FFX_memory.clickToEventTemple(0)
                checkpoint += 1
            elif checkpoint == 51: # Grab third Mac sphere
                FFX_memory.clickToEventTemple(1)
                checkpoint += 1
            elif checkpoint == 53: # Place third Mac sphere
                FFX_memory.clickToEventTemple(2)
                checkpoint += 1
            elif checkpoint == 58: # End of trials
                FFX_memory.clickToEventTemple(0)
                FFX_memory.awaitControl()
                FFX_memory.clickToEventTemple(4) #Just to start the next set of dialog.
            
            #General pathing
            elif FFX_targetPathing.setMovement(FFX_targetPathing.mTempleTrials(checkpoint)) == True:
                checkpoint += 1
                print("Checkpoint reached: ", checkpoint)
            

def trials_old():
    FFX_memory.awaitControl()
    FFXC.set_value('AxisLy', 1)
    time.sleep(8)
    FFXC.set_value('AxisLy', 0)
    
    FFX_memory.awaitControl()
    FFXC.set_value('AxisLy', -1)
    FFXC.set_value('AxisLx', -1)
    time.sleep(1)
    FFXC.set_value('AxisLy', 1)
    time.sleep(1)
    FFXC.set_value('AxisLx', 0)
    time.sleep(1.8)
    FFXC.set_value('AxisLy', -1)
    time.sleep(1.68) #Lining up with pedestol
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 1)
    time.sleep(2)
    FFXC.set_value('AxisLx', 0) #Push the first pedestol
    
    FFX_memory.awaitControl()
    FFXC.set_value('AxisLy', -1)
    FFXC.set_value('AxisLx', 1)
    time.sleep(0.3)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.55)
    FFXC.set_value('AxisLy', 1)
    FFXC.set_value('AxisLx', 0)
    time.sleep(1.5)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 0)
    FFX_memory.awaitControl()
    
    FFXC.set_value('AxisLy', 1)
    FFXC.set_value('AxisLx', 1)
    time.sleep(1)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.2)
    FFXC.set_value('AxisLx', 0)
    FFX_Screen.clickToPixel(930,830,(234, 140, 0)) #Removed Macalania sphere
    time.sleep(0.1)
    FFX_Xbox.menuB()
    FFX_memory.awaitControl()
    FFXC.set_value('AxisLx', -1)
    time.sleep(0.5)
    FFXC.set_value('AxisLy', 1)
    time.sleep(0.5)
    FFXC.set_value('AxisLx', 0)
    time.sleep(0.7)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', -1)
    time.sleep(1.3)
    FFXC.set_value('AxisLx', 0)
    FFXC.set_value('AxisLy', -1)
    time.sleep(1.5)
    FFXC.set_value('AxisLx', 1)
    time.sleep(0.2)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.1)
    FFXC.set_value('AxisLx', 0) #Pedestol, lower level
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(1.5)
    FFX_Xbox.menuB()
    FFX_memory.awaitControl()
    
    
    FFXC.set_value('AxisLx', 1) #Push pedestol on lower level
    time.sleep(0.8)
    FFXC.set_value('AxisLx', 0)
    FFX_memory.awaitControl()
    FFXC.set_value('AxisLy', 1)
    time.sleep(1.5)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 1)
    time.sleep(1.2)
    FFXC.set_value('AxisLx', -1)
    FFXC.set_value('AxisLy', -1)
    time.sleep(1.9)
    FFXC.set_value('AxisLx', 1)
    time.sleep(0.3)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.3)
    FFXC.set_value('AxisLx', 0)
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(1.5)
    FFX_Xbox.menuB() # Pick up glyph sphere
    FFX_memory.awaitControl()
    
    FFXC.set_value('AxisLy', 1)
    time.sleep(0.3)
    FFXC.set_value('AxisLx', 1)
    time.sleep(1.6)
    FFXC.set_value('AxisLx', 0)
    time.sleep(0.3)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', -1)
    time.sleep(1.3)
    FFXC.set_value('AxisLx', 0)
    FFXC.set_value('AxisLy', -1)
    time.sleep(1.5)
    FFXC.set_value('AxisLx', -1)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.2)
    FFXC.set_value('AxisLy', 1)
    time.sleep(0.2)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.6)
    FFXC.set_value('AxisLy', 1)
    time.sleep(0.1)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 0)
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(1.5)
    FFX_Xbox.menuB() #Insert glyph sphere
    FFX_memory.awaitControl()
    
    FFXC.set_value('AxisLx', 1)
    time.sleep(1.4)
    FFXC.set_value('AxisLx', 0)
    FFXC.set_value('AxisLy', 1)
    time.sleep(1.5)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 1)
    time.sleep(1.2)
    FFXC.set_value('AxisLx', -1)
    FFXC.set_value('AxisLy', -1)
    time.sleep(1.9)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.5)
    FFXC.set_value('AxisLx', 0)
    FFXC.set_value('AxisLy', -1)
    time.sleep(0.3)
    FFXC.set_value('AxisLx', -1)
    FFXC.set_value('AxisLy', 1)
    time.sleep(0.4)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 0)
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(1.5)
    FFX_Xbox.menuB() # Pick up Macalania sphere
    FFX_memory.awaitControl()
    
    FFXC.set_value('AxisLx', 1)
    FFXC.set_value('AxisLy', 1)
    time.sleep(2.5)
    FFXC.set_value('AxisLx', -1)
    time.sleep(1)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.5)
    FFXC.set_value('AxisLy', -1)
    FFXC.set_value('AxisLx', 0)
    time.sleep(1.5)
    FFXC.set_value('AxisLx', -1)
    time.sleep(0.7)
    FFXC.set_value('AxisLy', 1)
    FFXC.set_value('AxisLx', 0)
    time.sleep(0.3)
    FFXC.set_value('AxisLy', 0)
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(1.5)
    FFX_Xbox.menuB() #Insert Macalania sphere
    FFX_memory.awaitControl()
    
    FFXC.set_value('AxisLx', 1)
    FFXC.set_value('AxisLy', 1)
    time.sleep(1.5)
    FFXC.set_value('AxisLx', 0)
    time.sleep(1)
    FFXC.set_value('AxisLx', 1)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.5)
    FFXC.set_value('AxisLy', 1)
    time.sleep(0.5)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 0)
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(1.5)
    FFX_Xbox.menuB() # Pick up Macalania sphere
    FFX_memory.awaitControl()
    
    FFXC.set_value('AxisLx', 1)
    time.sleep(0.4)
    FFXC.set_value('AxisLy', -1)
    FFXC.set_value('AxisLx', -1)
    time.sleep(1.9)
    FFXC.set_value('AxisLx', 1)
    time.sleep(0.3)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.5)
    FFXC.set_value('AxisLx', 0)
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(0.5)
    FFX_Xbox.menuB()
    time.sleep(1.5)
    FFX_Xbox.menuB() #Insert Macalania sphere
    FFX_memory.awaitControl()
    
    FFXC.set_value('AxisLy', 1) #Let's get out of here.
    time.sleep(0.7)
    FFXC.set_value('AxisLx', -1)
    time.sleep(0.6)
    FFXC.set_value('AxisLy', 0)
    time.sleep(1)
    FFXC.set_value('AxisLy', -1)
    FFXC.set_value('AxisLx', 0)
    time.sleep(0.5)
    FFXC.set_value('AxisLx', 1)
    time.sleep(0.5)
    FFXC.set_value('AxisLy', 0)
    time.sleep(0.2)
    FFXC.set_value('AxisLy', -1)
    time.sleep(0.6)
    FFXC.set_value('AxisLx', 0)
    FFXC.set_value('AxisLy', 1)
    time.sleep(7)
    FFXC.set_value('AxisLy', 0)
    
    FFX_Screen.awaitMap1() #Back into the main room.
    FFXC.set_value('AxisLy', -1)
    time.sleep(3)
    FFXC.set_value('AxisLy', 0)

def escape():
    FFX_memory.clickToControl()
    print("First, some menuing")
    FFX_menu.afterSeymour()
    FFX_memory.fullPartyFormat('macalaniaescape')
    
    print("Now to escape the Guado")
    
    checkpoint = 0
    while FFX_memory.getBattleNum() != 195:
        if FFX_memory.userControl():
            #Events
            if checkpoint == 2:
                FFX_Xbox.touchSaveSphere()
                checkpoint += 1
                print("Touching save sphere. Update checkpoint: ", checkpoint)
            
            #Map changes
            elif checkpoint < 19 and FFX_memory.getMap() == 192:
                checkpoint = 19
                print("Map change. Update checkpoint: ", checkpoint)
            
            #General pathing
            elif FFX_targetPathing.setMovement(FFX_targetPathing.mTempleEscape(checkpoint)) == True:
                checkpoint += 1
                print("Checkpoint reached: ", checkpoint)
        else:
            FFXC.set_value('AxisLx', 0)
            FFXC.set_value('AxisLy', 0)
            if FFX_memory.battleActive():
                FFX_Screen.awaitTurn()
                if FFX_memory.getBattleNum() == 195:
                    break
                else:
                    FFX_Battle.fleeAll()
            elif FFX_memory.menuOpen():
                FFX_Xbox.tapB()
            elif FFX_memory.diagSkipPossible():
                FFX_Xbox.tapB()
    
    print("Done pathing. Now for the Wendigo fight.")
    FFX_Battle.wendigo()
    print("Wendigo fight over")

def escape_old(): #Old method, to be replaced.
    FFX_memory.clickToControl()
    FFX_menu.afterSeymour()
    FFXC.set_value('AxisLy', -1)
    time.sleep(1)
    FFXC.set_value('AxisLx', -1)
    time.sleep(2)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 0)
    FFX_Xbox.touchSaveSphere()
    
    FFX_memory.awaitControl()
    FFX_memory.fullPartyFormat('macalaniaescape')
    checkpoint = 0
    lastCP = 0
    while checkpoint != 1000:
        pos = FFX_memory.getCoords()
        #print("Checkpoint: ", checkpoint)
        if lastCP != checkpoint:
            print("Checkpoint reached: ", checkpoint)
            lastCP = checkpoint
        if FFX_memory.userControl():
            if checkpoint == 0:
                #print("Movement ", checkpoint)
                if pos[1] > -25:
                    checkpoint = 10
                else:
                    FFXC.set_value('AxisLy', -1)
                    if pos[0] > 811:
                        FFXC.set_value('AxisLx', 1)
                    elif pos[0] < 800:
                        FFXC.set_value('AxisLx', -1)
                    else:
                        FFXC.set_value('AxisLx', 0)
            elif checkpoint == 10:
                #print("Movement ", checkpoint)
                if pos[1] > 130:
                    checkpoint = 20
                else:
                    FFXC.set_value('AxisLy', -1)
                    if pos[1] > ((-3.54 * pos[0]) + 2877.51):
                        FFXC.set_value('AxisLx', 1)
                    elif pos[1] > ((-0.9 * pos[0]) + 857.5):
                        FFXC.set_value('AxisLx', 1)
                    else:
                        FFXC.set_value('AxisLx', 0)
            elif checkpoint == 20:
                #print("Movement ", checkpoint)
                if pos[1] > 385:
                    checkpoint = 30
                else:
                    FFXC.set_value('AxisLx', 1)
                    if pos[1] < ((-0.78 * pos[0]) + 774):
                        FFXC.set_value('AxisLy', -1)
                    elif pos[1] > 385:
                        FFXC.set_value('AxisLy', 1)
                    else:
                        FFXC.set_value('AxisLy', 0)
            elif checkpoint == 30: #End of first screen
                #print("Movement ", checkpoint)
                if FFX_memory.getMap() == 192:
                    checkpoint = 1000
                else:
                    FFXC.set_value('AxisLx', 1)
                    if pos[1] > 390:
                        FFXC.set_value('AxisLy', 1)
                    elif pos[1] > ((0.39 * pos[0]) + 234):
                        FFXC.set_value('AxisLy', 1)
                    elif pos[1] > ((1.12 * pos[0]) + 109.69):
                        FFXC.set_value('AxisLy', 1)
                    elif pos[1] > ((2.13 * pos[0]) + 15.54):
                        FFXC.set_value('AxisLy', 1)
                    elif pos[1] > 385:
                        FFXC.set_value('AxisLy', 0)
                    #elif pos[1] < ((-0.65 * pos[0]) + 700):
                    #    FFXC.set_value('AxisLy', -1)
                    else:
                        FFXC.set_value('AxisLy', 0)
        else:
            #print("No action ", checkpoint)
            FFXC.set_value('AxisLy', 0)
            FFXC.set_value('AxisLx', 0)
            if FFX_Screen.BattleScreen():
                FFX_Battle.fleeAll()
                while not FFX_memory.userControl():
                    FFX_Xbox.menuB()
    
def wendigoFight():
    print("wendigoFight function is no longer used.")

def wendigoFight_old():
    checkpoint = 40
    lastCP = 0
    FFXC.set_value('AxisLy', -1)
    FFXC.set_value('AxisLx', 0)
    FFX_memory.awaitControl()
    while checkpoint != 1000:
        pos = FFX_memory.getCoords()
        #print("Checkpoint: ", checkpoint)
        if lastCP != checkpoint:
            print("Checkpoint reached: ", checkpoint)
            lastCP = checkpoint
        if FFX_memory.userControl():
            if checkpoint == 40: #Start of second screen
                #Second screen.
                if pos[1] < ((-0.72 * pos[0]) + 357.78):
                    checkpoint = 50
                else:
                    FFXC.set_value('AxisLy', -1)
                    if pos[1] > ((2.75 * pos[0]) + 431.65):
                        FFXC.set_value('AxisLx', 1)
                    else:
                        FFXC.set_value('AxisLx', 0)
            elif checkpoint == 50:
                if pos[1] < 230:
                    checkpoint = 60
                else:
                    FFXC.set_value('AxisLx', 1)
                    if pos[0] > 36:
                        FFXC.set_value('AxisLy', -1)
                    else:
                        FFXC.set_value('AxisLy', 0)
            elif checkpoint == 60:
                if pos[0] < -32:
                    checkpoint = 70
                else:
                    FFXC.set_value('AxisLy', -1)
                    FFXC.set_value('AxisLx', -1)
            elif checkpoint == 70:
                if pos[1] < -145:
                    checkpoint = 80
                else:
                    FFXC.set_value('AxisLy', -1)
                    if pos[0] < -35:
                        FFXC.set_value('AxisLx', 1)
                    if pos[0] > -15:
                        FFXC.set_value('AxisLx', -1)
                    else:
                        FFXC.set_value('AxisLx', 0)
            elif checkpoint == 80:
                FFXC.set_value('AxisLy', -1)
                if pos[0] < -15:
                    FFXC.set_value('AxisLx', 1)
                else:
                    FFXC.set_value('AxisLx', 0)
        else:
            #print("No action ", checkpoint)
            FFXC.set_value('AxisLy', 0)
            FFXC.set_value('AxisLx', 0)
            if FFX_Screen.BattleScreen():
                if FFX_memory.getBattleNum() == 195:
                    checkpoint = 1000
                else:
                    FFX_Battle.fleeAll()
                    while not FFX_memory.userControl():
                        FFX_Xbox.menuB()
    print("Done pathing. Now for the Wendigo fight.")
    FFX_Battle.wendigo()
    print("Wendigo fight over")

def underLake():
    FFX_memory.clickToControl()
    FFXC.set_value('AxisLy', 1)
    time.sleep(1)
    FFXC.set_value('AxisLx', -1)
    time.sleep(0.8)
    FFXC.set_value('AxisLx', 1)
    time.sleep(1)
    FFXC.set_value('AxisLx', 0)
    FFX_memory.clickToEvent()
    FFXC.set_value('AxisLy', 0)
    
    FFX_memory.clickToControl()
    FFXC.set_value('AxisLy', 1)
    time.sleep(1.5) #Approach Yuna
    FFXC.set_value('AxisLy', 0)
    
    FFX_memory.clickToControl()
    FFXC.set_value('AxisLy', 1)
    while FFX_memory.getCoords()[1] > 110:
        FFXC.set_value('AxisLx', -1)
    while FFX_memory.getCoords()[1] > 85:
        FFXC.set_value('AxisLx', 1)
    while FFX_memory.getCoords()[0] > -30:
        if FFX_memory.getCoords()[1] < 110:
            FFXC.set_value('AxisLy', -1)
        else:
            FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 1)
    FFX_memory.clickToEvent() #Chest with Lv.2 Key Sphere
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 0)
    FFX_Xbox.SkipDialog(0.2)
    FFX_memory.clickToControl()
    FFXC.set_value('AxisLx', -1)
    time.sleep(0.25)
    while FFX_memory.getCoords()[0] < -5:
        FFXC.set_value('AxisLy', 1)
    FFXC.set_value('AxisLx', 0)
    FFXC.set_value('AxisLy', 1)
    time.sleep(1) #To Auron
    FFX_Xbox.SkipDialog(1.5)
    FFXC.set_value('AxisLy', 0)
    FFXC.set_value('AxisLx', 1)
    FFX_Xbox.SkipDialog(0.4)
    FFXC.set_value('AxisLx', -1)
    FFX_Xbox.SkipDialog(0.4)
    FFXC.set_value('AxisLx', 0)
    FFX_memory.clickToControl()
    
    FFXC.set_value('AxisLy', -1)
    time.sleep(3)
    FFXC.set_value('AxisLy', 0)
    time.sleep(10)
    FFX_Xbox.skipScene()
    
    #Now at the oasis
    #FFX_Screen.clickToMap1()
    #FFXC.set_value('AxisLy', 1)
    #time.sleep(5)
    #FFXC.set_value('AxisLy', 0)
    #FFX_Screen.clickToMap1()
    #FFXC.set_value('AxisLx', -1)
    #FFXC.set_value('AxisLy', -1)
    #time.sleep(0.2)
    #FFXC.set_value('AxisLy', 0)
    #time.sleep(0.9)
    #FFXC.set_value('AxisLx', 0)
    #FFX_Xbox.touchSaveSphere()