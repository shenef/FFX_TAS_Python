import time

import battle.main as main
import memory.main as main
import menu
import nemesis.arenaSelect as arenaSelect
import nemesis.menu as menu
import nemesis.targetPath as targetPath
import reset
import screen
import vars
import xbox

gameVars = vars.varsHandle()

FFXC = xbox.controllerHandle()

#The following functions extend the regular Bahamut run. Arena battles sections.

def saveGame(firstSave=False):
    while not targetPath.setMovement([-6,-27]):
        pass
    while not targetPath.setMovement([-2,-2]):
        pass
    print("Arena - Touch Save Sphere, and actually save")
    FFXC = xbox.controllerHandle()
    FFXC.set_neutral()
    ssDetails = main.getSaveSphereDetails()
    
    if main.userControl():
        while main.userControl():
            targetPath.setMovement([ssDetails[0], ssDetails[1]])
            xbox.tapB()
            main.waitFrames(1)
    try:
        FFXC.set_neutral()
    except:
        FFXC = xbox.controllerHandle()
        FFXC.set_neutral()
    main.waitFrames(30)
    xbox.tapB()
    main.waitFrames(10)
    
    print("Controller is now neutral. Attemption to open save menu.")
    while not main.saveMenuOpen():
        pass
    print("Save menu is open.")
    main.waitFrames(9)
    if not firstSave:
        xbox.menuDown()
        xbox.menuB()
        xbox.menuLeft()
    xbox.menuB() #Select the save file
    xbox.menuB() #Confirm the save
    main.waitFrames(90)
    xbox.menuA() #Back out
    xbox.menuA() #Back out
    xbox.menuA() #Back out
    xbox.menuA() #Back out
    
    print("Menu now closed. Back to the battles.")
    main.clearSaveMenuCursor()
    main.clearSaveMenuCursor2()
    while not targetPath.setMovement([-6,-27]):
        pass
    while not targetPath.setMovement([2,-25]):
        pass

def touchSave(realSave=False):
    while not targetPath.setMovement([-6,-27]):
        pass
    while not targetPath.setMovement([-2,-2]):
        pass
    main.touchSaveSphere()
    while not targetPath.setMovement([-6,-27]):
        pass
    while not targetPath.setMovement([2,-25]):
        pass
    arenaNPC()

def airShipDestination(destNum=0): #Default to Sin.
    while main.getMap() != 382:
        if main.userControl():
            targetPath.setMovement([-251,340])
        else:
            FFXC.set_neutral()
        xbox.menuB()
    while main.diagProgressFlag() != 4:
        xbox.menuB()
    print("Destination select on screen now.")
    while main.mapCursor() != destNum:
        if destNum < 8:
            xbox.tapDown()
        else:
            xbox.tapUp()
    xbox.tapB()
    main.waitFrames(2)
    xbox.tapB()
    main.clickToControl3()

def getSaveSphereDetails():
    mapVal = main.getMap()
    storyVal = main.getStoryProgress()
    print("Map:", mapVal, "| Story:", storyVal)
    x = 0
    y = 0
    diag = 0
    if mapVal == 322:
        #Inside Sin, next to airship
        x = 225
        y = -250
        diag = 15
    if mapVal == 19:
        #Besaid beach
        x = -310
        y = -475
        diag = 55
    if mapVal == 263:
        #Thunder Plains agency
        x = -30
        y = -10
        diag = 114
    if mapVal == 307:
        #Monster Arena
        x = 4
        y = 5
        diag = 166
    if mapVal == 98:
        #Kilika docks
        x = 46
        y = -252
        diag = 34
    if mapVal == 92:
        #MRR start
        x = -1
        y = -740
        diag = 43
    if mapVal == 266:
        #Calm Lands Gorge
        x = -310
        y = 190
        diag = 43
    if mapVal == 82:
        #Djose temple
        x = 100
        y = -240
        diag = 89
    if mapVal == 221:
        #Macalania Woods, near Spherimorph
        x = 197
        y = -120
        diag = 23
    if mapVal == 137:
        #Bikanel Desert
        x = -15
        y = 240
        diag = 31
    if mapVal == 313:
        #Zanarkand campfire
        x = 135
        y = -1
        diag = 4
    if mapVal == 327:
        #Sin, end zone
        x = -37
        y = -508
        diag = 10
    if mapVal == 258:
        #Omega (only used in Nemesis)
        x = -112
        y = -1066
        diag = 23
    
    print("Values: [", x, ",", y, "] - ", diag)
    return [x,y,diag]

def returnToAirship():
    print("Attempting Return to Airship")
    
    ssDetails = getSaveSphereDetails()
    
    if main.userControl():
        while main.userControl():
            targetPath.setMovement([ssDetails[0], ssDetails[1]])
            xbox.tapB()
            main.waitFrames(1)
    try:
        FFXC.set_neutral()
    except:
        FFXC = xbox.controllerHandle()
        FFXC.set_neutral()
    FFXC.set_neutral()
    
    while not main.getMap() in [194, 374]:
        if main.getMap() == 307 and main.getCoords()[1] < -5:
            while not targetPath.setMovement([-4,-21]):
                pass
            while not targetPath.setMovement([-2,-2]):
                pass
        else:
            FFXC.set_neutral()
            if main.saveMenuOpen():
                xbox.tapA()
            elif main.diagProgressFlag() == ssDetails[2]:
                # print("Cursor test:", memory.saveMenuCursor())
                if main.saveMenuCursor() != 1:
                    xbox.menuDown()
                else:
                    xbox.menuB()
            elif main.userControl():
                targetPath.setMovement([ssDetails[0], ssDetails[1]])
                xbox.menuB()
            elif main.diagSkipPossible():
                xbox.menuB()
            main.waitFrames(4)
    print("Return to Airship Complete.")
    main.clearSaveMenuCursor()
    main.clearSaveMenuCursor2()

def aeonStart():
    screen.awaitTurn()
    main.buddySwapYuna()
    main.aeonSummon(4)
    while not screen.turnTidus():
        if main.turnReady():
            if screen.turnAeon():
                main.attack('none')
            else:
                main.defend()

def yojimboBattle():
    #Incomplete
    screen.awaitTurn()
    if not 1 in main.getActiveBattleFormation():
        main.buddySwapYuna()
    print("+Yuna Overdrive to summon Yojimbo")
    main.yunaOD()
    print("+Pay the man")
    main.yojimboOD()
    main.waitFrames(90)
    while main.battleActive():
        if main.turnReady():
            if screen.turnTidus():
                main.tidusFlee()
            elif screen.turnAeon():
                xbox.SkipDialog(2)
            else:
                main.defend()
    
    #After battle stuff
    while not main.menuOpen():
        xbox.tapB()
    print("Battle is complete.")
    FFXC.set_value('BtnB', 1)
    main.waitFrames(180)
    FFXC.set_neutral()
    main.waitFrames(2)
    
    return main.battleArenaResults()

def autoLife():
    while not (main.turnReady() and screen.turnTidus()):
        if main.turnReady():
            if screen.turnAeon():
                main.attack('none')
            elif not screen.turnTidus():
                main.defend()
    while main.battleMenuCursor() != 22:
        if screen.turnTidus() == False:
            print("Attempting Haste, but it's not Tidus's turn")
            xbox.tapUp()
            xbox.tapUp()
            return
        if main.battleMenuCursor() == 1:
            xbox.tapUp()
        else:
            xbox.tapDown()
    while not main.otherBattleMenu():
        xbox.tapB()
    main._navigate_to_position(1)
    while main.otherBattleMenu():
        xbox.tapB()
    xbox.tapB()
    xbox.tapB()
    xbox.tapB()
    xbox.tapB()
    xbox.tapB()

def basicQuickAttacks(megaPhoenix = False, odVersion:int=0, yunaAutos=False):
    print("### Battle Start:", main.getEncounterID())
    FFXC.set_neutral()
    while main.battleActive():
        if main.turnReady():
            if screen.turnTidus():
                if megaPhoenix and screen.faintCheck() >= 2:
                    main.revive(itemNum = 7)
                elif main.getOverdriveBattle(0) == 100:
                    main.tidusOD(version=odVersion)
                else:
                    main.useSkill(1) #Quick hit
            elif screen.turnAeon():
                main.attack('none')
            else:
                main.defend()
    
    #After battle stuff
    while not main.menuOpen():
        xbox.tapB()
    FFXC.set_value('BtnB', 1)
    main.waitFrames(150)
    FFXC.set_neutral()
    main.waitFrames(2)
    return main.battleArenaResults()

def basicAttack(megaPhoenix = False, odVersion:int=0,useOD=False, yunaAutos=False):
    print("### Battle Start:", main.getEncounterID())
    FFXC.set_neutral()
    while main.battleActive():
        if main.turnReady():
            if screen.turnTidus():
                if megaPhoenix and screen.faintCheck() >= 2:
                    main.revive(itemNum = 7)
                elif useOD and main.getOverdriveBattle(0) == 100:
                    main.tidusOD(version=odVersion)
                else:
                    main.attack('none')
            elif screen.turnYuna() and yunaAutos:
                attack('none')
            elif screen.turnAeon():
                attack('none')
            else:
                main.defend()
    
    #After battle stuff
    while not main.menuOpen():
        xbox.tapB()
    FFXC.set_value('BtnB', 1)
    main.waitFrames(150)
    FFXC.set_neutral()
    main.waitFrames(2)
    return main.battleArenaResults()

def arenaNPC():
    if main.getMap() != 307:
        return
    while not (main.diagProgressFlag() == 74 and main.diagSkipPossible()):
        if main.userControl():
            if main.getCoords()[1] > -15:
                print("Wrong position, moving away from sphere")
                while not targetPath.setMovement([-6,-27]):
                    pass
                while not targetPath.setMovement([2,-25]):
                    pass
            else:
                print("Engaging NPC")
                targetPath.setMovement([5,-12])
                xbox.tapB()
        else:
            FFXC.set_neutral()
            if main.diagProgressFlag() == 59:
                xbox.menuA()
                xbox.menuA()
                xbox.menuA()
                xbox.tapB()
            elif main.diagSkipPossible() and not main.diagProgressFlag() == 74:
                xbox.tapB()
    print("Mark 1")
    main.waitFrames(30) #This buffer can be improved later.
    print("Mark 2")

def restockDowns():
    print("Restocking phoenix downs")
    if main.getItemCountSlot(main.getItemSlot(6)) >= 80:
        print("Restock not needed. Disregard.")
        return
    arenaNPC()
    arenaSelect.arenaMenuSelect(3)
    main.waitFrames(60)
    xbox.tapB()
    main.waitFrames(6)
    while main.equipBuyRow() != 2:
        if main.equipBuyRow() < 2:
            xbox.tapDown()
        else:
            xbox.tapUp()
    xbox.tapB()
    xbox.tapUp()
    xbox.tapUp()
    xbox.tapUp()
    xbox.tapUp()
    xbox.tapUp()
    xbox.tapUp()
    xbox.tapUp()
    xbox.tapUp()
    xbox.tapUp()
    xbox.tapB()
    main.waitFrames(6)
    xbox.menuA()
    main.waitFrames(6)
    xbox.menuA()

def battles1():
    if not main.equippedArmorHasAbility(charNum=1, abilityNum=0x800A):
        menu.equipArmor(character=1,ability=0x800A, fullMenuClose=False)
    if not main.equippedArmorHasAbility(charNum=4, abilityNum=0x800A):
        menu.equipArmor(character=4,ability=0x800A)
    main.closeMenu()
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=0)
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=0)
    gameVars.arenaSuccess(arrayNum=0,index=0)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=1)
    aeonStart()
    autoLife()
    while not basicQuickAttacks(megaPhoenix = True):
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(4)
        main.fullPartyFormat('kilikawoods1')
        touchSave()
        arenaNPC()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=1)
        aeonStart()
        if screen.turnTidus():
            autoLife()
    gameVars.arenaSuccess(arrayNum=0,index=1)
    restockDowns()
    arenaSelect.arenaMenuSelect(4)
    main.fullPartyFormat('kilikawoods1')
    menu.tidusSlayer(odPos=0)
    
    checkYojimboPossible()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=2)
    while not basicQuickAttacks(yunaAutos=True):
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=2)
    gameVars.arenaSuccess(arrayNum=0,index=2)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=3)
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=3)
    gameVars.arenaSuccess(arrayNum=0,index=3)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=4)
    autoLife()
    while not basicQuickAttacks(megaPhoenix=True):
        print("Battle not completed successfully.")
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=4)
        autoLife()
    gameVars.arenaSuccess(arrayNum=0,index=4)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=5)
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=5)
    gameVars.arenaSuccess(arrayNum=0,index=5)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaSelect.arenaMenuSelect(4)
    menu.tidusSlayer(odPos=2)
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=6)
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=6)
    gameVars.arenaSuccess(arrayNum=0,index=6)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=7)
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=7)
    gameVars.arenaSuccess(arrayNum=0,index=7)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=8)
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=8)
    gameVars.arenaSuccess(arrayNum=0,index=8)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaSelect.arenaMenuSelect(4)
    menu.tidusSlayer(odPos=0)
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=9)
    while not basicQuickAttacks(yunaAutos=True):
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=9)
    gameVars.arenaSuccess(arrayNum=0,index=9)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=10)
    autoLife()
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=10)
        autoLife()
    gameVars.arenaSuccess(arrayNum=0,index=10)
    restockDowns()
    
    checkYojimboPossible()
    
def battles2():
    print("++Starting second section++")
    arenaSelect.arenaMenuSelect(4)
    touchSave()
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=14,monsterIndex=1)
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(4)
        touchSave()
        arenaNPC()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=14,monsterIndex=1)
    gameVars.arenaSuccess(arrayNum=1,index=1)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaSelect.arenaMenuSelect(4)
    touchSave()
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=14,monsterIndex=3)
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=14,monsterIndex=3)
    gameVars.arenaSuccess(arrayNum=1,index=3)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaSelect.arenaMenuSelect(4)
    touchSave()
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=14,monsterIndex=5)
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=14,monsterIndex=5)
    gameVars.arenaSuccess(arrayNum=1,index=5)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaSelect.arenaMenuSelect(4)
    touchSave()
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=14,monsterIndex=8)
    while not basicQuickAttacks():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=14,monsterIndex=8)
    gameVars.arenaSuccess(arrayNum=1,index=8)
    restockDowns()
    arenaSelect.arenaMenuSelect(4)
    touchSave()
    
    checkYojimboPossible()

def jugFarmDone():
    print("||| Slot: ", main.getItemSlot(87))
    if main.getItemSlot(87) > 250:
        return False
    else:
        print("Count: ", main.getItemCountSlot(main.getItemSlot(87)))
        if main.getItemCountSlot(main.getItemSlot(87)) < 6:
            return False
    return True

def juggernautFarm():
    checkYojimboPossible()
    while not jugFarmDone():
        arenaNPC()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=14,monsterIndex=12)
        autoLife()
        basicQuickAttacks(megaPhoenix=True,odVersion=1)
        restockDowns()
        checkYojimboPossible()
        arenaSelect.arenaMenuSelect(4)
        touchSave()
    print("Good to go on strength spheres")
    gameVars.arenaSuccess(arrayNum=1,index=12)
    print("Starting menu to finish strength.")
    arenaSelect.arenaMenuSelect(4)
    menu.strBoost()
    print("Touch save sphere, and then good to go.")
    touchSave()
    
def battles3():
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=11)
    autoLife()
    while not basicQuickAttacks(megaPhoenix=True):
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=13,monsterIndex=11)
        autoLife()
    gameVars.arenaSuccess(arrayNum=0,index=11)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaSelect.arenaMenuSelect(4)
    touchSave()
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=14,monsterIndex=2)
    aeonStart()
    autoLife()
    while not basicAttack(useOD=False):
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(4)
        touchSave()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=14,monsterIndex=2)
        autoLife()
    gameVars.arenaSuccess(arrayNum=1,index=2)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=14,monsterIndex=0)
    autoLife()
    while not basicQuickAttacks(megaPhoenix=True,odVersion=1):
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=14,monsterIndex=0)
        autoLife()
    gameVars.arenaSuccess(arrayNum=1,index=0)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=14,monsterIndex=9)
    autoLife()
    while not basicQuickAttacks(megaPhoenix=True,odVersion=1):
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=14,monsterIndex=9)
        autoLife()
    gameVars.arenaSuccess(arrayNum=1,index=9)
    restockDowns()
    
    checkYojimboPossible()
    
    arenaSelect.arenaMenuSelect(4)
    touchSave()
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=14,monsterIndex=10)
    autoLife()
    while not basicQuickAttacks(megaPhoenix=True,odVersion=1):
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=14,monsterIndex=10)
        autoLife()
    gameVars.arenaSuccess(arrayNum=1,index=10)
    restockDowns()
    
    checkYojimboPossible()

def battles4():
    arenaSelect.arenaMenuSelect(4)
    touchSave()
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=15,monsterIndex=0)
    autoLife()
    while not basicQuickAttacks(megaPhoenix=True,odVersion=1):
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=15,monsterIndex=0)
        autoLife()
    gameVars.arenaSuccess(arrayNum=2,index=0)
    restockDowns()
    
    checkYojimboPossible()
    arenaSelect.arenaMenuSelect(4)
    touchSave()
    
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=15,monsterIndex=6)
    
    while not shinryuBattle():
        print("Battle not completed successfully.")
        restockDowns()
        arenaSelect.arenaMenuSelect(4)
        touchSave()
        arenaNPC()
        arenaSelect.arenaMenuSelect(1)
        arenaSelect.startFight(areaIndex=15,monsterIndex=6)
    
    gameVars.arenaSuccess(arrayNum=2,index=6)
    restockDowns()

def itemDump():
    arenaSelect.arenaMenuSelect(2)
    main.waitFrames(90)
    xbox.menuRight()
    xbox.menuB()
    menu.sellAll(NEA=True)
    xbox.menuA()
    xbox.menuA()
    xbox.menuA()
    xbox.menuA()

def quickResetLogic():
    reset.resetToMainMenu()
    main.waitFrames(90)
    while main.getMap() != 23:
        FFXC.set_value('BtnStart', 1)
        main.waitFrames(2)
        FFXC.set_value('BtnStart', 0)
        main.waitFrames(2)
    main.waitFrames(60)
    xbox.menuB()
    main.waitFrames(60)
    xbox.menuDown()
    xbox.menuB()
    xbox.menuB()
    FFXC.set_neutral()
    gameVars.printArenaStatus()
    main.waitFrames(30)

def checkYojimboPossible():
    if main.overdriveState2()[1] < 100:
        return False
    if main.overdriveState2()[1] == 100 and main.getGilvalue() < 300000:
        itemDump()
    
    if main.overdriveState2()[1] == 100 and main.getGilvalue() >= 300000:
        #Save game in preparation for the Yojimbo attempt
        main.waitFrames(20)
        arenaSelect.arenaMenuSelect(4)
        main.fullPartyFormat('kilikawoods1')
        if gameVars.yojimboGetIndex() == 1:
            saveGame(firstSave=True)
        else:
            saveGame(firstSave=False)
            
        #Now attempt to get Zanmato until successful, no re-saving.
        while not battles5(gameVars.yojimboGetIndex()):
            quickResetLogic()
        return True
    else:
        return False

def shinryuBattle():
    rikkuFirstTurn=False
    rikkuDriveComplete=False
    screen.awaitTurn()
    while main.battleActive():
        if main.turnReady():
            if screen.turnRikku():
                if rikkuFirstTurn == False:
                    main.defend()
                elif rikkuDriveComplete:
                    main._useHealingItem(itemID=9)
                else:
                    main.rikkuFullOD('shinryu')
                    rikkuDriveComplete=True
            elif screen.turnTidus():
                if main.getOverdriveBattle(0) == 100:
                    main.tidusOD(version=1)
                elif rikkuDriveComplete and not main.autoLifeState():
                    autoLife()
                else:
                    main.attack('none')
            else:
                main.defend()
    
    #After battle stuff
    while not main.menuOpen():
        xbox.tapB()
    FFXC.set_value('BtnB', 1)
    main.waitFrames(150)
    FFXC.set_neutral()
    main.waitFrames(2)
    return main.battleArenaResults()

def battles5(completionVersion:int):
    print("Yojimbo battle number: ", completionVersion)
    if completionVersion >= 12 and completionVersion != 99:
        return True #These battles are complete at this point.
    yojimboSuccess = False
    
    #Now for the Yojimbo section
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    
    #Battles here
    if completionVersion == 1:
        arenaSelect.startFight(areaIndex=15,monsterIndex=1)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=2,index=1)
            yojimboSuccess = True
    
    elif completionVersion == 2:
        arenaSelect.startFight(areaIndex=15,monsterIndex=2)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=2,index=2)
            yojimboSuccess = True
    
    elif completionVersion == 3:
        arenaSelect.startFight(areaIndex=15,monsterIndex=3)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=2,index=3)
            yojimboSuccess = True
    
    elif completionVersion == 4:
        arenaSelect.startFight(areaIndex=15,monsterIndex=4)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=2,index=4)
            yojimboSuccess = True
    
    elif completionVersion == 5:
        arenaSelect.startFight(areaIndex=15,monsterIndex=5)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=2,index=5)
            yojimboSuccess = True
    
    elif completionVersion == 6:
        arenaSelect.startFight(areaIndex=13,monsterIndex=12)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=0,index=12)
            yojimboSuccess = True
    
    elif completionVersion == 7:
        arenaSelect.startFight(areaIndex=14,monsterIndex=13)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=1,index=13)
            yojimboSuccess = True
    
    elif completionVersion == 8:
        arenaSelect.startFight(areaIndex=14,monsterIndex=11)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=1,index=11)
            yojimboSuccess = True
        
    elif completionVersion == 9:
        arenaSelect.startFight(areaIndex=14,monsterIndex=7)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=1,index=7)
            yojimboSuccess = True
    
    elif completionVersion == 10:
        arenaSelect.startFight(areaIndex=14,monsterIndex=6)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=1,index=6)
            yojimboSuccess = True
    
    
    elif completionVersion == 11:
        arenaSelect.startFight(areaIndex=14,monsterIndex=4)
        if yojimboBattle():
            gameVars.arenaSuccess(arrayNum=1,index=4)
            yojimboSuccess = True
    
    
    elif completionVersion == 99: #Nemesis
        arenaSelect.startFight(areaIndex=15,monsterIndex=7)
        if yojimboBattle():
            main.clickToDiagProgress(2)
            main.clickToControl3()
            return True
        else:
            return False
    
    
    #Wrap up decisions
    if yojimboSuccess == True:
        gameVars.yojimboIncrementIndex()
        if completionVersion != 99:
            restockDowns()
        return True
    else:
        arenaSelect.arenaMenuSelect(4)
        return False

def rechargeYuna():
    arenaNPC()
    arenaSelect.arenaMenuSelect(1)
    arenaSelect.startFight(areaIndex=13,monsterIndex=9)
    screen.awaitTurn()
    while main.battleActive():
        if main.turnReady():
            if screen.turnYuna():
                main.attack('none')
            else:
                main.escapeOne()

def nemesisBattle():
    if gameVars.yojimboGetIndex() < 12:
        arenaSelect.arenaMenuSelect(4)
        touchSave()
        while gameVars.yojimboGetIndex() < 12:
            #If Yuna is charged, do next battle. Otherwise charge.
            if main.overdriveState2()[1] == 100:
                battles5(gameVars.yojimboGetIndex())
            else:
                rechargeYuna()
            arenaSelect.arenaMenuSelect(4)
            touchSave()
                
    if main.overdriveState2()[1] != 100:
        rechargeYuna()
    if main.getGilvalue() < 300000:
        arenaSelect.arenaMenuSelect(4)
        menu.autoSortEquipment()
        # menu.autoSortItems()
        arenaNPC()
        arenaSelect.arenaMenuSelect(2)
        main.waitFrames(90)
        xbox.menuRight()
        xbox.menuB()
        menu.sellAll()
        xbox.menuA()
        xbox.menuA()
        xbox.menuA()
        xbox.menuA()
        xbox.menuA()
        xbox.menuA()
        xbox.menuA()
    arenaSelect.arenaMenuSelect(4)
    main.fullPartyFormat('kilikawoods1')
    saveGame(firstSave=False)
    while not battles5(completionVersion=99):
        quickResetLogic()
    # nemesis.arenaSelect.arenaMenuSelect(4)

def returnToSin():
    FFXC = xbox.controllerHandle()
    while not targetPath.setMovement([-6,-27]):
        pass
    while not targetPath.setMovement([-2,-2]):
        pass
    returnToAirship()
    
    menu.equipWeapon(character=0, ability=0x8001, fullMenuClose=True)
    airShipDestination(destNum=0)
    main.awaitControl()
    FFXC.set_movement(0,-1)
    main.waitFrames(2)
    main.awaitEvent()
    FFXC.set_neutral()