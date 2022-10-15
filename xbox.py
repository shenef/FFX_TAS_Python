import json
import math
import time

import vgamepad as vg

import memory.main
import vars

gameVars = vars.varsHandle()


class vgTranslator:
    def __init__(self):
        self.gamepad = vg.VX360Gamepad()

    def set_value(self, xKey, value):
        # Buttons, pressing
        if xKey == "BtnBack" and value == 1:
            self.gamepad.press_button(button=0x0020)
        elif xKey == "BtnStart" and value == 1:
            self.gamepad.press_button(button=0x0010)
        elif xKey == "BtnA" and value == 1:
            self.gamepad.press_button(button=0x2000)
        elif xKey == "BtnB" and value == 1:
            self.gamepad.press_button(button=0x1000)
        elif xKey == "BtnX" and value == 1:
            self.gamepad.press_button(button=0x4000)
        elif xKey == "BtnY" and value == 1:
            self.gamepad.press_button(button=0x8000)
        elif xKey == "BtnShoulderL" and value == 1:
            self.gamepad.press_button(button=0x0100)
        elif xKey == "BtnShoulderR" and value == 1:
            self.gamepad.press_button(button=0x0200)
        elif xKey == "Dpad" and value == 1:  # Dpad up
            self.gamepad.press_button(button=0x0001)
        elif xKey == "Dpad" and value == 2:  # Dpad down
            self.gamepad.press_button(button=0x0002)
        elif xKey == "Dpad" and value == 4:  # Dpad left
            self.gamepad.press_button(button=0x0004)
        elif xKey == "Dpad" and value == 8:  # Dpad right
            self.gamepad.press_button(button=0x0008)
        elif xKey == "TriggerL" and value == 1:
            self.gamepad.left_trigger_float(value_float=1.0)
        elif xKey == "TriggerR" and value == 1:
            self.gamepad.right_trigger_float(value_float=1.0)

        # Buttons, releasing
        elif xKey == "BtnBack" and value == 0:
            self.gamepad.release_button(button=0x0020)
        elif xKey == "BtnStart" and value == 0:
            self.gamepad.release_button(button=0x0010)
        elif xKey == "BtnA" and value == 0:
            self.gamepad.release_button(button=0x2000)
        elif xKey == "BtnB" and value == 0:
            self.gamepad.release_button(button=0x1000)
        elif xKey == "BtnX" and value == 0:
            self.gamepad.release_button(button=0x4000)
        elif xKey == "BtnY" and value == 0:
            self.gamepad.release_button(button=0x8000)
        elif xKey == "BtnShoulderL" and value == 0:
            self.gamepad.release_button(button=0x0100)
        elif xKey == "BtnShoulderR" and value == 0:
            self.gamepad.release_button(button=0x0200)
        elif xKey == "Dpad" and value == 0:
            self.gamepad.release_button(button=0x0001)
            self.gamepad.release_button(button=0x0002)
            self.gamepad.release_button(button=0x0004)
            self.gamepad.release_button(button=0x0008)
        elif xKey == "TriggerL" and value == 0:
            self.gamepad.left_trigger_float(value_float=0.0)
        elif xKey == "TriggerR" and value == 0:
            self.gamepad.right_trigger_float(value_float=0.0)

        # Error states
        elif xKey == "AxisLx" or xKey == "AxisLy":
            print("ERROR - OLD MOVEMENT COMMAND FOUND")
            print("ERROR - OLD MOVEMENT COMMAND FOUND")
            print("ERROR - OLD MOVEMENT COMMAND FOUND")
            print("ERROR - ", xKey)
            print("ERROR - OLD MOVEMENT COMMAND FOUND")
            print("ERROR - OLD MOVEMENT COMMAND FOUND")
            print("ERROR - OLD MOVEMENT COMMAND FOUND")
            self.set_neutral()

        self.gamepad.update()
        # For additional details, review this website:
        # https://pypi.org/project/vgamepad/

    def set_movement(self, x, y):
        if x > 1:
            x = 1
        if x < -1:
            x = -1
        if y > 1:
            y = 1
        if y < -1:
            y = -1

        try:
            self.gamepad.left_joystick_float(x_value_float=x, y_value_float=y)
            self.gamepad.update()
        except Exception:
            pass

    def set_neutral(self):
        self.gamepad.reset()
        self.gamepad.update()


FFXC = vgTranslator()


def controllerHandle():
    return FFXC


processed_cutscenes = set()


def skipScene(fast_mode: bool = False):
    cutsceneID = memory.main.getCutsceneID()
    print(cutsceneID)
    if not fast_mode or cutsceneID not in processed_cutscenes:
        print("Skip cutscene")
        memory.main.waitFrames(2)
        FFXC.set_value('BtnStart', 1)  # Generate button to skip
        memory.main.waitFrames(1)
        FFXC.set_value('BtnStart', 0)
        memory.main.waitFrames(2)
        tapX()
        processed_cutscenes.add(cutsceneID)
    if not fast_mode:
        memory.main.waitFrames(60)


def skipSceneSpec():
    print("Skip cutscene and store an additional skip for a future scene")
    FFXC.set_value('BtnStart', 1)  # Generate button to skip
    memory.main.waitFrames(30 * 0.07)
    FFXC.set_value('BtnStart', 0)
    memory.main.waitFrames(30 * 0.105)
    FFXC.set_value('BtnX', 1)  # Perform the skip
    memory.main.waitFrames(30 * 0.035)
    FFXC.set_value('BtnX', 0)
    # Before despawn, regenerate the button for use in a future scene.
    FFXC.set_value('BtnStart', 1)
    memory.main.waitFrames(30 * 0.035)
    FFXC.set_value('BtnStart', 0)
    memory.main.waitFrames(30 * 0.2)


def skipStoredScene(skipTimer):
    print("Mashing skip button")
    currentTime = time.time()
    print("Current Time:", currentTime)
    clickTimer = currentTime + skipTimer
    print("Click Until:", clickTimer)
    while currentTime < clickTimer:
        FFXC.set_value('BtnX', 1)  # Perform the skip
        memory.main.waitFrames(30 * 0.035)
        FFXC.set_value('BtnX', 0)
        memory.main.waitFrames(30 * 0.035)
        currentTime = time.time()
    print("Mashing skip button - Complete")


def Attack():
    print("Basic attack")
    FFXC.set_value('BtnB', 1)
    memory.main.waitFrames(30 * 0.08)
    FFXC.set_value('BtnB', 0)
    memory.main.waitFrames(30 * 0.08)
    FFXC.set_value('BtnB', 1)
    memory.main.waitFrames(30 * 0.08)
    FFXC.set_value('BtnB', 0)
    memory.main.waitFrames(30 * 0.5)


def touchSaveSphere():
    FFXC.set_neutral()
    print("Touching the save sphere")
    while memory.main.userControl():
        tapB()
        memory.main.waitFrames(3)
    memory.main.waitFrames(15)
    while not memory.main.userControl():
        if memory.main.menuControl():
            if not memory.main.saveMenuCursor():
                menuA()
                memory.main.waitFrames(1)
            else:
                tapB()
    FFXC.set_neutral()
    memory.main.waitFrames(30 * 0.035)


def SkipDialog(Keystrokes):
    # 2 frames per button mash
    num_repetitions = math.ceil(round(Keystrokes * 30) / 2)
    print(f"Mashing B {num_repetitions} times.")
    for _ in range(num_repetitions):
        tapB()
    print("Mashing B - Complete")


def SkipDialogSpecial(Keystrokes):
    num_repetitions = math.ceil(round(Keystrokes * 30) / 2)
    print(f"Mashing A and B {num_repetitions} times.")
    for _ in range(num_repetitions):
        FFXC.set_value('BtnB', 1)
        FFXC.set_value('BtnA', 1)
        memory.main.waitFrames(1)
        FFXC.set_value('BtnB', 0)
        FFXC.set_value('BtnA', 0)
        memory.main.waitFrames(1)
    print("Mashing A and B - Complete")


def menuUp():
    FFXC.set_value('Dpad', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(3)


def menuDown():
    FFXC.set_value('Dpad', 2)
    memory.main.waitFrames(2)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(3)


def menuLeft():
    FFXC.set_value('Dpad', 4)
    memory.main.waitFrames(2)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(3)


def menuRight():
    FFXC.set_value('Dpad', 8)
    memory.main.waitFrames(2)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(3)


def tapUp():
    FFXC.set_value('Dpad', 1)
    memory.main.waitFrames(1)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(1)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def tapDown():
    FFXC.set_value('Dpad', 2)
    memory.main.waitFrames(1)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(1)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def tapLeft():
    FFXC.set_value('Dpad', 4)
    memory.main.waitFrames(1)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(1)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def tapRight():
    FFXC.set_value('Dpad', 8)
    memory.main.waitFrames(1)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(1)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def shoulderLeft():
    FFXC.set_value('BtnShoulderL', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('BtnShoulderL', 0)
    memory.main.waitFrames(2)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def shoulderRight():
    FFXC.set_value('BtnShoulderR', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('BtnShoulderR', 0)
    memory.main.waitFrames(2)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def menuA():
    FFXC.set_value('BtnA', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('BtnA', 0)
    memory.main.waitFrames(4)


def menuB():
    FFXC.set_value('BtnB', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('BtnB', 0)
    memory.main.waitFrames(4)


def tapA():
    FFXC.set_value('BtnA', 1)
    memory.main.waitFrames(1)
    FFXC.set_value('BtnA', 0)
    memory.main.waitFrames(1)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def tapB():
    FFXC.set_value('BtnB', 1)
    memory.main.waitFrames(1)
    FFXC.set_value('BtnB', 0)
    memory.main.waitFrames(1)
    if gameVars.usePause():
        memory.main.waitFrames(3)


def menuX():
    FFXC.set_value('BtnX', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('BtnX', 0)
    memory.main.waitFrames(4)


def menuY():
    FFXC.set_value('BtnY', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('BtnY', 0)
    memory.main.waitFrames(4)


def tapX():
    FFXC.set_value('BtnX', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('BtnX', 0)
    memory.main.waitFrames(1)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def tapY():
    FFXC.set_value('BtnY', 1)
    memory.main.waitFrames(1)
    FFXC.set_value('BtnY', 0)
    memory.main.waitFrames(1)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def menuBack():
    FFXC.set_value('BtnBack', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('BtnBack', 0)
    memory.main.waitFrames(2)


def lBumper():
    FFXC.set_value('BtnShoulderL', 1)
    memory.main.waitFrames(1)
    FFXC.set_value('BtnShoulderL', 0)
    memory.main.waitFrames(1)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def TriggerL():
    FFXC.set_value('TriggerL', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('TriggerL', 0)
    memory.main.waitFrames(2)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def TriggerR():
    FFXC.set_value('TriggerR', 1)
    memory.main.waitFrames(2)
    FFXC.set_value('TriggerR', 0)
    memory.main.waitFrames(2)
    if gameVars.usePause():
        memory.main.waitFrames(2)


def tapStart():
    FFXC.set_value('BtnStart', 1)  # Generate button to skip
    memory.main.waitFrames(1)
    FFXC.set_value('BtnStart', 0)
    memory.main.waitFrames(2)


def weapSwap(position):
    print("Weapon swap, weapon in position:", position)
    while memory.main.mainBattleMenu():
        tapRight()
    while memory.main.otherBattleMenu():
        tapB()
    while memory.main.battleCursor3() != position:
        tapDown()
    while memory.main.interiorBattleMenu():
        tapB()


def armorSwap(position):
    print("Armor swap, armor in position:", position)
    menuRight()
    memory.main.waitFrames(30 * 0.5)
    menuDown()
    memory.main.waitFrames(30 * 0.5)
    menuB()
    memory.main.waitFrames(30 * 0.7)
    armor = 0
    while armor < position:
        menuDown()
        armor += 1
    menuB()
    menuB()
    memory.main.waitFrames(30 * 0.3)


def clearSavePopup(clickToDiagNum=0):
    FFXC = controllerHandle()
    FFXC.set_neutral()
    memory.main.clickToDiagProgress(clickToDiagNum)
    complete = 0
    counter = 0
    while complete == 0:
        counter += 1
        if counter % 100 == 0:
            print("Waiting for Save dialog:", counter / 100)

        if memory.main.diagProgressFlag() != clickToDiagNum and memory.main.diagSkipPossible():
            tapB()

        elif memory.main.diagSkipPossible():
            if memory.main.savePopupCursor() == 0:
                menuUp()
            else:
                menuB()
                complete = 1
    memory.main.waitFrames(5)


def awaitSave(index=0):
    clearSavePopup(clickToDiagNum=index)


def remove():
    print("Controller may freeze the program here. If so, please restart your PC.")


def gridUp():
    FFXC.set_value('Dpad', 1)
    memory.main.waitFrames(30 * 0.04)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(30 * 0.12)


def gridDown():
    FFXC.set_value('Dpad', 2)
    memory.main.waitFrames(30 * 0.04)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(30 * 0.12)


def gridLeft():
    FFXC.set_value('Dpad', 4)
    memory.main.waitFrames(30 * 0.04)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(30 * 0.12)


def gridRight():
    FFXC.set_value('Dpad', 8)
    memory.main.waitFrames(30 * 0.04)
    FFXC.set_value('Dpad', 0)
    memory.main.waitFrames(30 * 0.12)


def clickToBattle():
    print("Mashing A until first turn in battle")
    FFXC.set_neutral()
    while not (memory.main.battleActive() and memory.main.turnReady()):
        if memory.main.userControl():
            break
        elif not memory.main.battleActive():
            tapB()
        elif memory.main.diagSkipPossible():
            tapB()


characterMapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
    " ": 26,
    "a": 30,
    "b": 31,
    "c": 32,
    "d": 33,
    "e": 34,
    "f": 35,
    "g": 36,
    "h": 37,
    "i": 38,
    "j": 39,
    "k": 40,
    "l": 41,
    "m": 42,
    "n": 43,
    "o": 44,
    "p": 45,
    "q": 46,
    "r": 47,
    "s": 48,
    "t": 49,
    "u": 50,
    "v": 51,
    "w": 52,
    "x": 53,
    "y": 54,
    "z": 55,
    "1": 60,
    "2": 61,
    "3": 62,
    "4": 63,
    "5": 64,
    "6": 65,
    "7": 66,
    "8": 67,
    "9": 68,
    "0": 69,
    "!": 70,
    "?": 71,
    '"': 72,
    "+": 73,
    "-": 74,
    "*": 75,
    "/": 76,
    "%": 77,
    "&": 78,
    "=": 79,
    ".": 80,
    ",": 81,
    ":": 82,
    ";": 83,
    "[": 85,
    "]": 86,
    "(": 87,
    ")": 88
}


def navigateToCharacter(curCharacter):
    positionTarget = characterMapping[curCharacter]
    while positionTarget != memory.main.getNamingIndex():
        if positionTarget - memory.main.getNamingIndex() >= 15:
            tapDown()
        elif memory.main.getNamingIndex() - positionTarget >= 15:
            tapUp()
        elif memory.main.getNamingIndex() < positionTarget:
            tapRight()
        elif memory.main.getNamingIndex() > positionTarget:
            tapLeft()


def nameAeon(character=""):
    print("Waiting for aeon naming screen")

    while not memory.main.nameAeonReady():
        if memory.main.diagSkipPossible() or memory.main.menuOpen():
            tapB()
    if character:
        with open("character_names.json") as fp:
            customName = json.load(fp)[character]
        if customName:
            customName = customName[:8]
            while memory.main.getNamingMenu():
                tapRight()
            while memory.main.nameHasCharacters():
                tapA()
            for curCharacter in customName:
                navigateToCharacter(curCharacter)
                tapB()

    print("Naming screen is up.")
    while memory.main.equipSellRow() != 1:
        tapStart()
    while memory.main.equipSellRow() != 0:
        tapUp()
    while memory.main.nameConfirmOpen():
        tapB()
