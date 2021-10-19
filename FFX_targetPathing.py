import pyxinput
import time
import FFX_Xbox
import FFX_memory

from math import copysign
import numpy as np

FFXC = FFX_Xbox.FFXC

def setMovement(target) -> bool:

    player = FFX_memory.getCoords()
    (forward, right) = FFX_memory.getMovementVectors()

    targetPos = np.array([target[0], target[1]])
    playerPos = np.array(player)

    # Calculate forward and right directions relative to camera space
    pX = player[0]
    pY = player[1]
    eX = target[0]
    eY = target[1]
    fX = forward[0]
    fY = forward[1]
    rX = right[0]
    rY = right[1]

    Ly = fX * (eX-pX) + rX * (eY-pY)
    Lx = fY * (eX-pX) + rY * (eY-pY)
    sumsUp = abs(Lx)+abs(Ly)
    if sumsUp == 0:
        sumsUp = 0.01
    Lx /= sumsUp
    Ly /= sumsUp
    if abs(Lx) > abs(Ly):
        Ly = copysign(Ly/Lx if Lx else 0, Ly)
        Lx = copysign(1, Lx)
    elif abs(Ly) > abs(Lx):
        Lx = copysign(Lx/Ly if Ly else 0, Lx)
        Ly = copysign(1, Ly)

    FFXC.set_value('AxisLx', Lx)
    FFXC.set_value('AxisLy', Ly)
    
    if abs(player[1] - target[1]) < 3 and abs(player[0] - target[0]) < 3:
        return True #Checkpoint reached
    else:
        return False

def tidusHome(checkpoint):
    if checkpoint == 0:
        x = 117
        y = 3
    if checkpoint == 1:
        x = 28
        y = 8
    if checkpoint == 2:
        print("Talk to the kids")
    if checkpoint == 3:
        x = 13
        y = -6
    if checkpoint == 4:
        print("Talk to the girls")
    if checkpoint == 5:
        x = -16
        y = 11
    if checkpoint == 6:
        x = 426
        y = -3
    if checkpoint == 7:
        x = 147
        y = -30
    if checkpoint == 8:
        x = 54
        y = -33
    if checkpoint == 9:
        x = -62
        y = -62
    if checkpoint == 10:
        x = -200
        y = -100
    if checkpoint == 11:
        x = 0
        y = 880
    if checkpoint == 12:
        x = 0
        y = 830
    if checkpoint == 13:
        x = 0
        y = 700
    if checkpoint == 14:
        x = 2
        y = 838
    if checkpoint == 15:
        x = 14
        y = 940
    if checkpoint == 16:
        x = 32
        y = 1038
    return [x,y]

def allStartsHere(checkpoint):
    if checkpoint == 0:
        x = 849
        y = -92
    if checkpoint == 1:
        x = 885
        y = -101
    if checkpoint == 2:
        x = 905
        y = -149
    if checkpoint == 3:
        x = 918
        y = -179
    if checkpoint == 4:
        x = 957
        y = -219
    if checkpoint == 5:
        x = 987
        y = -257
    if checkpoint == 6:
        print("Save sphere")
    if checkpoint == 7:
        x = 1003
        y = -253
    if checkpoint == 8:
        x = 1100
        y = -350
    if checkpoint == 9:
        x = 16
        y = -67
    if checkpoint == 10:
        x = 16
        y = -67
    if checkpoint == 11:
        x = 79
        y = -457
    if checkpoint == 12:
        x = 99
        y = -383
    if checkpoint == 13:
        x = 95
        y = -171
    if checkpoint == 14:
        x = 68
        y = 24
    if checkpoint == 15:
        x = 6
        y = 348
    if checkpoint == 16:
        x = -3
        y = 492
    if checkpoint == 17:
        x = -6
        y = 559
    if checkpoint == 18:
        x = -39
        y = 610
    if checkpoint == 19:
        x = -72
        y = 642
    if checkpoint == 20:
        x = -80
        y = 680
    return [x,y]

def baajHallway(checkpoint):
    if checkpoint == 0:
        x = -8
        y = 87
    if checkpoint == 1:
        x = 7
        y = 115
    if checkpoint == 2:
        x = 6
        y = 154
    if checkpoint == 3:
        x = 1
        y = 160
    if checkpoint == 4:
        x = -4
        y = 167
    if checkpoint == 5:
        x = 8
        y = 176
    if checkpoint == 6:
        x = 13
        y = 231
    if checkpoint == 7:
        x = 6
        y = 240
    if checkpoint == 8:
        x = -2
        y = 250
    return [x,y]

def baajPuzzle(checkpoint):
    if checkpoint == 0:
        x = -71
        y = 79
    if checkpoint == 1:
        x = -94
        y = 120
    if checkpoint == 2:
        x = -100
        y = 139
    if checkpoint == 3:
        print("Save sphere")
    if checkpoint == 4:
        x = -113
        y = 119
    if checkpoint == 5:
        print("Through first door")
    if checkpoint == 6:
        print("Flint obtained.")
    if checkpoint == 7:
        print("Back to main room")
    if checkpoint == 8:
        x = -87
        y = 94
    if checkpoint == 9:
        x = -24
        y = -10
    if checkpoint == 10:
        x = 81
        y = -90
    if checkpoint == 11:
        x = 135
        y = -137
    if checkpoint == 12:
        print("Map change towards withered bouquet")
    if checkpoint == 13:
        x = 85
        y = 71
    if checkpoint == 14:
        x = 78
        y = 30
    if checkpoint == 15:
        x = 72
        y = 8
    if checkpoint == 16:
        x = 76
        y = -6
    if checkpoint == 17:
        x = 65
        y = -31
    if checkpoint == 18:
        x = 48
        y = -39
    if checkpoint == 19:
        x = 29
        y = -64
    if checkpoint == 20:
        x = 8
        y = -78
    if checkpoint == 21:
        print("Withered bouquet")
    if checkpoint == 22:
        x = 8
        y = -78
    if checkpoint == 23:
        x = 29
        y = -64
    if checkpoint == 24:
        x = 48
        y = -39
    if checkpoint == 25:
        x = 65
        y = -31
    if checkpoint == 26:
        x = 76
        y = -6
    if checkpoint == 27:
        x = 72
        y = 8
    if checkpoint == 28:
        x = 78
        y = 30
    if checkpoint == 29:
        x = 85
        y = 71
    if checkpoint == 30:
        x = 82
        y = 81
    if checkpoint == 31:
        x = 75
        y = 90
    if checkpoint == 32:
        print("Back to main room")
    return [x,y]

def besaid1(checkpoint):
    if checkpoint == 0:
        x = -263
        y = -390
    if checkpoint == 1:
        x = -509
        y = -552
    if checkpoint == 2:
        x = 72
        y = -31
    if checkpoint == 3:
        x = 84
        y = -8
    if checkpoint == 4:
        x = 137
        y = 1
    if checkpoint == 5:
        x = 250
        y = 5
    if checkpoint == 6:
        x = -601
        y = -411
    if checkpoint == 7: #Wakka pushes Tidus
        x = -229
        y = -359
    if checkpoint == 8:
        x = 64
        y = -612
    if checkpoint == 9:
        x = 64
        y = -612
    if checkpoint == 10:
        x = 64
        y = -612
    if checkpoint == 11:
        x = 206
        y = -679
    if checkpoint == 12:
        x = 236
        y = -699
    if checkpoint == 13:
        x = 262
        y = -702
    if checkpoint == 14:
        x = 280
        y = -700
    if checkpoint == 15:
        x = 307
        y = -691
    if checkpoint == 16:
        x = 412
        y = -646
    if checkpoint == 17:
        x = 439
        y = -631
    if checkpoint == 18:
        x = 488
        y = -459
    if checkpoint == 19: #Pillar, before the big open area.
        x = 498
        y = -414
    if checkpoint == 20: #Adjust to best trigger for pirhanas
        x = 480
        y = -37
    if checkpoint == 21: #Adjust to best trigger for pirhanas
        x = 480
        y = 100
    if checkpoint == 22: #Hilltop
        x = 73
        y = -49
    if checkpoint == 23:
        x = 0
        y = -182
    if checkpoint == 24:
        x = -10
        y = -226
    if checkpoint == 25:
        x = -9
        y = -270
    if checkpoint == 26:
        x = 20
        y = -374
    if checkpoint == 27:
        x = 82
        y = -534
    if checkpoint == 28:
        x = 75
        y = -700
    if checkpoint == 29: #Enter Besiad village
        x = -22
        y = 186
    if checkpoint == 30:
        x = -16
        y = 14
    if checkpoint == 31:
        x = -8
        y = -59
    if checkpoint == 32:
        x = -5
        y = -179
    if checkpoint == 33: #Temple
        print("Temple")
    if checkpoint == 34:
        x = 38
        y = 27
    if checkpoint == 35:
        x = 0
        y = -124
    if checkpoint == 36:
        x = 0
        y = -180
    if checkpoint == 37:
        x = -13
        y = -69
    if checkpoint == 38:
        x = -15
        y = -5
    if checkpoint == 39:
        x = -17
        y = 50
    if checkpoint == 40:
        x = -51
        y = 202
    if checkpoint == 41:
        x = -79
        y = 292
    if checkpoint == 42: #Into Wakka's tent
        print("Into Wakka's tent")
    if checkpoint == 43:
        print("Sleep tight.")
    if checkpoint == 44:
        print("Exit the tent")
    if checkpoint == 45:
        x = -51
        y = 202
    if checkpoint == 46:
        x = -17
        y = 50
    if checkpoint == 47:
        x = -15
        y = -5
    if checkpoint == 48:
        x = -13
        y = -69
    if checkpoint == 49:
        x = 0
        y = -200
    if checkpoint == 50: #The Precepts must be obeyed!
        x = 0
        y = 30
    return [x,y]

def besaidTrials(checkpoint):
    if checkpoint == 0:
        x = -30
        y = 126
    if checkpoint == 1:
        print("First glyph")
    if checkpoint == 2:
        x = -11
        y = 116
    if checkpoint == 3:
        print("Second glyph")
    if checkpoint == 4:
        x = 7
        y = 117
    if checkpoint == 5:
        x = 45
        y = 123
    if checkpoint == 6:
        x = 67
        y = 133
    if checkpoint == 7:
        print("Pick up Besaid sphere")
    if checkpoint == 8:
        x = 41
        y = 146
    if checkpoint == 9:
        x = -4
        y = 143
    if checkpoint == 10:
        x = -14
        y = 133
    if checkpoint == 11:
        x = -17
        y = 104
    if checkpoint == 12:
        print("Insert Besaid sphere")
    if checkpoint == 13:
        x = -22
        y = 78
    if checkpoint == 14:
        x = -16
        y = 68
    if checkpoint == 15:
        x = 34
        y = 52
    if checkpoint == 16:
        x = 37
        y = 43
    if checkpoint == 17:
        x = 34
        y = -29
    if checkpoint == 18:
        x = 22
        y = -36
    if checkpoint == 19:
        x = -6
        y = -32
    if checkpoint == 20:
        print("Touch the hidden door glyph")
    if checkpoint == 21:
        x = -17
        y = -24
    if checkpoint == 22:
        x = -15
        y = 17
    if checkpoint == 23:
        print("Besaid sphere")
    if checkpoint == 24:
        x = -14
        y = -26
    if checkpoint == 25:
        x = -10
        y = -50
    if checkpoint == 26:
        print("Insert Besaid sphere, and push to completion")
    if checkpoint == 27: #Back from the temple
        x = 0
        y = -107
    if checkpoint == 28:
        x = 0
        y = -130
    if checkpoint == 29:
        x = -19
        y = -52
    if checkpoint == 30:
        x = -16
        y = -17
    if checkpoint == 31:
        x = -13
        y = 76
    if checkpoint == 32: #Approach Valefor's first scene
        x = 0
        y = 200
    if checkpoint == 33: #Night scene
        x = 15
        y = 194
    if checkpoint == 34:
        print("Talk to Yuna")
    if checkpoint == 35:
        x = -3
        y = 174
    if checkpoint == 36:
        print("Sleep tight")
    if checkpoint == 37:
        x = 340
        y = 15
    if checkpoint == 38:
        x = 343
        y = 105
    if checkpoint == 39:
        print("Dream about girls")
    if checkpoint == 40: #Ready to leave village.
        x = 7
        y = 24
    if checkpoint == 41:
        x = 4
        y = -46
    if checkpoint == 42:
        x = 0
        y = -200
    return [x,y]

def besaid2(checkpoint):
    if checkpoint == 0:
        print("Back into the village")
    if checkpoint == 1:
        x = 7
        y = 413
    if checkpoint == 2:
        x = 42
        y = 375
    if checkpoint == 3:
        print("Tent 1")
    if checkpoint == 4:
        x = -2
        y = 5
    if checkpoint == 5:
        print("Shopkeeper")
    if checkpoint == 6:
        x = -2
        y = -18
    if checkpoint == 7:
        print("Exit tent")
    if checkpoint == 8:
        x = -76
        y = 223
    if checkpoint == 9:
        print("Tent 2")
    if checkpoint == 10:
        x = -3
        y = -4
    if checkpoint == 11:
        print("Good doggo")
    if checkpoint == 12:
        x = -4
        y = -19
    if checkpoint == 13:
        print("Exit tent")
    if checkpoint == 14:
        x = -37
        y = 406
    if checkpoint == 15:
        x = -12
        y = 502
    if checkpoint == 16:
        print("Exit the front gates")
    if checkpoint == 17: #Outside village
        x = 63
        y = -469
    if checkpoint == 18:
        print("First tutorial")
    if checkpoint == 19:
        x = -10
        y = -270
    if checkpoint == 20:
        x = -17
        y = -245
    if checkpoint == 21:
        x = -1
        y = -189
    if checkpoint == 22:
        x = 43
        y = 21
    if checkpoint == 23:
        print("Second tutorial")
    if checkpoint == 24:
        print("Hilltop")
    if checkpoint == 25:
        x = -24
        y = 124
    if checkpoint == 26:
        x = 0
        y = 250
    if checkpoint == 27:
        x = 26
        y = -109
    if checkpoint == 28:
        x = 86
        y = 17
    if checkpoint == 29:
        x = 79
        y = 61
    if checkpoint == 30:
        x = -12
        y = 183
    if checkpoint == 31:
        x = -40
        y = 300
    if checkpoint == 32: #Waterfalls
        x = -803
        y = 39
    if checkpoint == 33:
        x = -686
        y = 78
    if checkpoint == 34:
        x = -630
        y = 91
    if checkpoint == 35:
        x = -570
        y = 91
    if checkpoint == 36:
        x = -499
        y = 80
    if checkpoint == 37:
        x = -334
        y = 43
    if checkpoint == 38:
        x = -245
        y = 36
    if checkpoint == 39:
        x = -186
        y = 21
    if checkpoint == 40:
        x = -109
        y = -27
    if checkpoint == 41:
        x = -27
        y = -71
    if checkpoint == 42:
        x = 26
        y = -93
    if checkpoint == 43:
        x = 90
        y = -120
    if checkpoint == 44:
        x = 159
        y = -133
    if checkpoint == 45:
        x = 215
        y = -123
    if checkpoint == 46:
        x = 253
        y = -108
    if checkpoint == 47:
        x = 354
        y = -2
    if checkpoint == 48:
        x = 410
        y = 96
    if checkpoint == 49:
        x = 453
        y = 197
    if checkpoint == 50:
        x = 490
        y = 300
    if checkpoint == 51: # Weird T screen
        x = -23
        y = 48
    if checkpoint == 52:
        x = -19
        y = 29
    if checkpoint == 53:
        x = -40
        y = -9
    if checkpoint == 54:
        x = -31
        y = -17
    if checkpoint == 55:
        x = 14
        y = -4
    if checkpoint == 56:
        x = 43
        y = -31
    if checkpoint == 57:
        x = 56
        y = -44
    if checkpoint == 58:
        x = 80
        y = -150
    if checkpoint == 59: #Beach
        x = -318
        y = -472
    if checkpoint == 60:
        print("Save sphere")
    if checkpoint == 61:
        x = -283
        y = -438
    if checkpoint == 62:
        x = -218
        y = -367
    if checkpoint == 63:
        x = 105
        y = -72
    if checkpoint == 64:
        x = 306
        y = -58
    if checkpoint == 65:
        x = 329
        y = -39
    if checkpoint == 66:
        x = 357
        y = 13
    if checkpoint == 67:
        x = 425
        y = -4
    if checkpoint == 68:
        x = 425
        y = 50
    if checkpoint == 69:
        x = 425
        y = 90
    return [x,y]

def liki(checkpoint):
    if checkpoint == 0:
        x = 5
        y = 176
    if checkpoint == 1:
        print("Group around Yuna")
    if checkpoint == 2:
        x = -22
        y = 90
    if checkpoint == 3:
        print("Talk to Wakka")
    if checkpoint == 4:
        x = -15
        y = 127
    if checkpoint == 5:
        x = 0
        y = 350
    return [x,y]

def Kilika1(checkpoint):
    if checkpoint == 0:
        x = -301
        y = -258
    if checkpoint == 1:
        x = -269
        y = -253
    if checkpoint == 2:
        x = -137
        y = -226
    if checkpoint == 3:
        x = -59
        y = -195
    if checkpoint == 4:
        print("Enter cutscene, Yuna's dance")
    if checkpoint == 5:
        x = 80
        y = -22
    if checkpoint == 6:
        print("Yuna dancing, ends in the inn")
    if checkpoint == 7:
        x = 32
        y = 0
    if checkpoint == 8:
        print("Exit the inn")
    if checkpoint == 9:
        x = 27
        y = 114
    if checkpoint == 10:
        x = 86
        y = 96
    if checkpoint == 11:
        x = 86
        y = 31
    if checkpoint == 12:
        print("Back to first map")
    if checkpoint == 13:
        x = -31
        y = -179
    if checkpoint == 14:
        x = -25
        y = -216
    if checkpoint == 15:
        x = -1
        y = -245
    if checkpoint == 16:
        print("Talking to Wakka")
    if checkpoint == 17:
        x = -24
        y = -166
    if checkpoint == 18:
        print("Back towards the inn")
    if checkpoint == 19:
        x = 84
        y = 99
    if checkpoint == 20:
        x = 4
        y = 106
    if checkpoint == 21:
        x = -112
        y = 117
    if checkpoint == 22:
        x = -125
        y = 135
    if checkpoint == 23:
        x = -155
        y = 205
    if checkpoint == 24:
        x = -155
        y = 350
    return [x,y]

def miihen(checkpoint):
    if checkpoint == 0:
        x = -15
        y = 203
    if checkpoint == 1:
        x = -44
        y = 419
    if checkpoint == 2:
        x = -49
        y = 496
    if checkpoint == 3:
        x = -39
        y = 538
    if checkpoint == 4:
        x = -10
        y = 1000
    if checkpoint == 5:
        x = -44
        y = 1344
    if checkpoint == 6 or checkpoint == 7 or checkpoint == 8:
        print("Attempting Miihen skip")
    if checkpoint == 9:
        x = 17
        y = 1536
    if checkpoint == 10:
        x = 24
        y = 1601
    if checkpoint == 11:
        x = 0
        y = 1796
    if checkpoint == 12:
        x = 0
        y = 2200
    if checkpoint == 13:
        x = -12
        y = 629
    if checkpoint == 14:
        x = 0
        y = 895
    if checkpoint == 15:
        x = -9
        y = 1222
    if checkpoint == 16:
        x = 0
        y = 1417
    if checkpoint == 17:
        x = 0
        y = 2000
    if checkpoint == 18:
        x = -22
        y = 774
    if checkpoint == 19:
        x = -3
        y = 1155
    if checkpoint == 20:
        x = -11
        y = 1621
    if checkpoint == 21:
        x = -8
        y = 2078
    if checkpoint == 22:
        x = 5
        y = 2369
    if checkpoint == 23:
        x = 0
        y = 2682
    if checkpoint == 24:
        x = -22
        y = 2783
    if checkpoint == 25: #Shelinda
        print("Shelinda")
    if checkpoint == 26:
        x = 5
        y = 2982
    if checkpoint == 27:
        x = 2
        y = 3088
    if checkpoint == 28:
        x = 0
        y = 3500
    if checkpoint == 29:
        x = 0
        y = -227
    return [x,y]

def lowRoad(checkpoint):
    if checkpoint == 0:
        x = 35
        y = -932
    if checkpoint == 1:
        x = 43
        y = -919
    if checkpoint == 2:
        print("Touching save sphere")
    if checkpoint == 3:
        x = 37
        y = -903
    if checkpoint == 4:
        x = 69
        y = -805
    if checkpoint == 5:
        x = 85
        y = -742
    if checkpoint == 6:
        x = 142
        y = -616
    if checkpoint == 7:
        x = 175
        y = -515
    if checkpoint == 8:
        x = 190
        y = -417
    if checkpoint == 9:
        x = 174
        y = -355
    if checkpoint == 10:
        x = 62
        y = -244
    if checkpoint == 11:
        x = 19
        y = -178
    if checkpoint == 12:
        x = 17
        y = -153
    if checkpoint == 13:
        x = 17
        y = -16
    if checkpoint == 14:
        x = 39
        y = 33
    if checkpoint == 15:
        x = 59
        y = 59
    if checkpoint == 16:
        x = 100
        y = 100
    if checkpoint == 17: #Second low road map
        x = 357
        y = 120
    if checkpoint == 18:
        x = 403
        y = 129
    if checkpoint == 19:
        x = 467
        y = 152
    if checkpoint == 20:
        x = 537
        y = 176
    if checkpoint == 21:
        x = 586
        y = 212
    if checkpoint == 22:
        x = 638
        y = 258
    if checkpoint == 23:
        x = 679
        y = 299
    if checkpoint == 24:
        x = 715
        y = 378
    if checkpoint == 25: #Last checkpoint before reviewing for Self Destruct
        x = 732
        y = 448
    if checkpoint == 26:
        x = 738
        y = 481
    if checkpoint == 27:
        x = 780
        y = 530
    if checkpoint == 28: #Final map, meeting Seymour
        x = 158
        y = -209
    if checkpoint == 29:
        x = 59
        y = -104
    if checkpoint == 30:
        x = 9
        y = -44
    if checkpoint == 31:
        x = -41
        y = 36
    if checkpoint == 32:
        x = -42
        y = 152
    if checkpoint == 33:
        x = -57
        y = 288
    if checkpoint == 34:
        print("Talk to the guard")
    if checkpoint == 35:
        x = -57
        y = 288
    if checkpoint == 36:
        x = -50
        y = 400
    return [x,y]

def mrrStart(checkpoint):
    if checkpoint == 0:
        x = -40
        y = -667
    if checkpoint == 1:
        x = -58
        y = -614
    if checkpoint == 2:
        x = -62
        y = -616
    if checkpoint == 3:
        print("Attempt skip")
    if checkpoint == 4:
        x = -21
        y = -593
    if checkpoint == 5:
        x = -30
        y = -530
    if checkpoint == 6:
        x = -59
        y = -498
    if checkpoint == 7:
        x = -80
        y = -488
    if checkpoint == 8:
        x = -115
        y = -488
    if checkpoint == 9:
        x = -206
        y = -418
    if checkpoint == 10:
        x = -206
        y = -300
    return [x,y]

def mrrMain(checkpoint):
    if checkpoint == 0:
        x = 12
        y = -738
    if checkpoint == 1:
        print("Touching save sphere")
    if checkpoint == 2:
        x = -28
        y = -663
    if checkpoint == 3:
        x = -37
        y = -601
    if checkpoint == 4:
        print("Up the first lift")
    if checkpoint == 5:
        x = -48
        y = -571
    if checkpoint == 6:
        x = -108
        y = -463
    if checkpoint == 7:
        x = -108
        y = -428
    if checkpoint == 8:
        x = -85
        y = -391
    if checkpoint == 9:
        x = -87
        y = -372
    if checkpoint == 10:
        x = -78
        y = -361
    if checkpoint == 11:
        x = -38
        y = -367
    if checkpoint == 12:
        x = -6
        y = -381
    if checkpoint == 13:
        x = 38
        y = -414
    if checkpoint == 14:
        x = 63
        y = -398
    if checkpoint == 15:
        x = 109
        y = -339
    if checkpoint == 16:
        x = 127
        y = -198
    if checkpoint == 17:
        x = 122
        y = -166
    if checkpoint == 18:
        x = 91
        y = -176
    if checkpoint == 19:
        x = 0
        y = -215
    if checkpoint == 20:
        x = -63
        y = -189
    if checkpoint == 21:
        x = -88
        y = -141
    if checkpoint == 22:
        x = -104
        y = 54
    if checkpoint == 23:
        x = -102
        y = 73
    if checkpoint == 24:
        x = -86
        y = 87
    if checkpoint == 25:
        x = 25
        y = 138
    if checkpoint == 26:
        x = 32
        y = 151
    if checkpoint == 27:
        x = 23
        y = 233
    if checkpoint == 28:
        x = -89
        y = 295
    if checkpoint == 29:
        x = -91
        y = 321
    if checkpoint == 30:
        x = -87
        y = 368
    if checkpoint == 31:
        x = -68
        y = 402
    if checkpoint == 32:
        x = -48
        y = 425
    if checkpoint == 33:
        x = 35
        y = 461
    if checkpoint == 34:
        x = 92
        y = 515
    if checkpoint == 35:
        x = 51
        y = 543
    if checkpoint == 36:
        x = -20
        y = 568
    if checkpoint == 37:
        x = -71
        y = 593
    if checkpoint == 38:
        x = -109
        y = 604
    if checkpoint == 39:
        x = -115
        y = 687
    if checkpoint == 40:
        x = -71
        y = 775
    if checkpoint == 41:
        x = -39
        y = 829
    if checkpoint == 42:
        x = -12
        y = 838
    if checkpoint == 43:
        x = 26
        y = 828
    if checkpoint == 44:
        x = 44
        y = 834
    if checkpoint == 45:
        x = 59
        y = 898
    if checkpoint == 46:
        print("Up the second lift")
    if checkpoint == 47:
        x = -36
        y = -194
    if checkpoint == 48:
        print("Grabbing X-potion from the dude")
    if checkpoint == 49:
        x = 24
        y = -157
    if checkpoint == 50:
        x = 52
        y = -135
    if checkpoint == 51:
        x = 116
        y = 4
    if checkpoint == 52:
        x = 121
        y = 50
    if checkpoint == 53: #Lining up with the guy for 400 gil
        x = 116
        y = 81
    if checkpoint == 54:
        x = 61
        y = 140
    if checkpoint == 55:
        x = 29
        y = 154
    if checkpoint == 56:
        x = -21
        y = 223
    if checkpoint == 57:
        x = 29
        y = 227
    if checkpoint == 58:
        print("Up the third lift")
    if checkpoint == 59:
        x = 59
        y = 244
    if checkpoint == 60:
        x = 99
        y = 254
    if checkpoint == 61:
        x = 198
        y = 251
    if checkpoint == 62:
        x = 219
        y = 202
    if checkpoint == 63: #Next to the final lift
        x = 227
        y = 165
    if checkpoint == 64:
        x = 249
        y = 172
    if checkpoint == 65:
        x = 264
        y = 156
    if checkpoint == 66:
        print("Up the final lift.")
    if checkpoint == 67:
        x = 281
        y = 152
    if checkpoint == 68:
        x = 328
        y = 154
    if checkpoint == 69:
        x = 342
        y = 160
    if checkpoint == 70:
        x = 450
        y = 160
    if checkpoint == 71: #Into Battle Site zone (upper, cannon area)
        x = 47
        y = 513
    if checkpoint == 72:
        x = 70
        y = 606
    if checkpoint == 73:
        x = 84
        y = 629
    if checkpoint == 74:
        x = 70
        y = 707
    if checkpoint == 75:
        x = -67
        y = 830
    return [x,y]

def battleSite(checkpoint):
    if checkpoint == 0:
        x = -430
        y = 3274
    if checkpoint == 1:
        x = -258
        y = 3227
    if checkpoint == 2:
        x = -207
        y = 3230
    if checkpoint == 3:
        x = -115
        y = 3330
    if checkpoint == 4:
        x = -52
        y = 3414
    if checkpoint == 5:
        print("O'aka menu")
    if checkpoint == 6:
        x = -68
        y = 3354
    if checkpoint == 7:
        x = -59
        y = 3345
    if checkpoint == 8:
        print("Touching save sphere")
    if checkpoint == 9:
        x = -71
        y = 3324
    if checkpoint == 10:
        x = -31
        y = 3300
    if checkpoint == 11:
        x = -3
        y = 3303
    if checkpoint == 12:
        print("Into the scene with Kinoc")
    if checkpoint == 13:
        x = 217
        y = 3134
    if checkpoint == 14:
        print("Start of fight, Sinspawn Gui")
    return [x,y]

def battleSiteAftermath(checkpoint):
    if checkpoint == 0:
        x = 148
        y = 2836
    if checkpoint == 1:
        x = 75
        y = 2992
    if checkpoint == 2: #Clasko position
        x = 50
        y = 3092
    if checkpoint == 3:
        x = 609
        y = -175
    if checkpoint == 4:
        x = 548
        y = -159
    if checkpoint == 5:
        x = 417
        y = -160
    if checkpoint == 6:
        print("Start conversation with Auron")
    if checkpoint == 7:
        x = 428
        y = -116
    if checkpoint == 8:
        x = 501
        y = 40
    if checkpoint == 9:
        x = 520
        y = 40
    if checkpoint == 10:
        x = 671
        y = 47
    if checkpoint == 11:
        x = 830
        y = 39
    if checkpoint == 12:
        x = 941
        y = 59
    if checkpoint == 13:
        x = 978
        y = 77
    if checkpoint == 14:
        print("Towards Djose section.")
    return [x,y]

def djoseTrials(checkpoint):
    if checkpoint == 0:
        x = -22
        y = -233
    if checkpoint == 1:
        print("First sphere")
    if checkpoint == 2:
        x = -6
        y = -193
    if checkpoint == 3:
        print("Sphere door")
    if checkpoint == 4:
        x = 24
        y = -208
    if checkpoint == 5:
        print("Second sphere")
    if checkpoint == 6:
        x = 6
        y = -191
    if checkpoint == 7:
        print("Sphere door")
    if checkpoint == 8:
        x = 0
        y = -176
    if checkpoint == 9:
        x = 0
        y = -58
    if checkpoint == 10:
        x = -3
        y = -7
    if checkpoint == 11:
        x = -8
        y = 18
    if checkpoint == 12:
        x = -19
        y = 42
    if checkpoint == 13:
        print("Left sphere")
    if checkpoint == 14:
        x = 34
        y = 31
    if checkpoint == 15:
        x = 69
        y = 34
    if checkpoint == 16:
        print("Insert left sphere")
    if checkpoint == 17:
        x = 31
        y = 30
    if checkpoint == 18:
        x = 23
        y = 43
    if checkpoint == 19:
        print("Right sphere")
    if checkpoint == 20:
        x = -8
        y = 30
    if checkpoint == 21:
        x = -8
        y = 26
    if checkpoint == 22:
        print("Pushing pedestol")
    if checkpoint == 23:
        x = 56
        y = 33
    if checkpoint == 24:
        print("Insert right sphere")
    if checkpoint == 25:
        print("Unused")
    if checkpoint == 26:
        print("Unused")
    if checkpoint == 27:
        x = 57
        y = 34
    if checkpoint == 28:
        print("Left sphere")
    if checkpoint == 29:
        x = 14
        y = 27
    if checkpoint == 30:
        x = -65
        y = 24
    if checkpoint == 31:
        print("Reset switch")
    if checkpoint == 32:
        x = -41
        y = 24
    if checkpoint == 33:
        x = -10
        y = 22
    if checkpoint == 34:
        print("Insert left sphere")
    if checkpoint == 35:
        x = -4
        y = 10
    if checkpoint == 36:
        x = 9
        y = 15
    if checkpoint == 37:
        x = 8
        y = 24
    if checkpoint == 38:
        print("Powered sphere")
    if checkpoint == 39:
        x = 22
        y = 39
    if checkpoint == 40:
        print("Insert powered sphere")
    if checkpoint == 41:
        x = 32
        y = 31
    if checkpoint == 42:
        x = 66
        y = 29
    if checkpoint == 43:
        print("Right sphere")
    if checkpoint == 44:
        x = 8
        y = 24
    if checkpoint == 45:
        print("Insert right sphere")
    if checkpoint == 46:
        x = 8
        y = 13
    if checkpoint == 47:
        x = 0
        y = 16
    if checkpoint == 48:
        print("All the hidden room stuff.")
    if checkpoint == 49:
        x = 2
        y = 47
    if checkpoint == 50:
        x = 20
        y = 47
    if checkpoint == 51:
        print("Powered sphere")
    if checkpoint == 52:
        x = -19
        y = 46
    if checkpoint == 53:
        print("Insert powered sphere")
    if checkpoint == 54:
        x = -14
        y = 24
    if checkpoint == 55:
        x = -65
        y = 24
    if checkpoint == 56:
        print("Reset switch")
    if checkpoint == 57:
        x = -7
        y = 24
    if checkpoint == 58:
        print("Left sphere")
    if checkpoint == 59:
        x = -2
        y = 1
    if checkpoint == 60:
        x = -2
        y = -53
    if checkpoint == 61:
        x = -2
        y = -191
    if checkpoint == 62:
        x = -26
        y = -216
    if checkpoint == 63:
        print("Final insert Left sphere")
    if checkpoint == 64:
        x = -1
        y = -185
    if checkpoint == 65:
        x = 3
        y = -9
    if checkpoint == 66:
        x = 6
        y = 5
    if checkpoint == 67:
        x = 9
        y = 26
    if checkpoint == 68:
        print("Right sphere")
    if checkpoint == 69:
        x = 6
        y = 5
    if checkpoint == 70:
        x = 3
        y = -9
    if checkpoint == 71:
        x = 3
        y = -185
    if checkpoint == 72:
        x = 26
        y = -214
    if checkpoint == 73:
        print("Final insert Right sphere")
    if checkpoint == 74:
        x = 3
        y = -185
    if checkpoint == 75:
        x = -3
        y = -8
    if checkpoint == 76:
        x = -3
        y = 0
    if checkpoint == 77:
        x = -4
        y = 4
    if checkpoint == 78:
        x = -37
        y = 26
    if checkpoint == 79:
        x = -58
        y = 22
    if checkpoint == 80: #Destro glyph
        print("Destruction Glyph")
    if checkpoint == 81:
        x = -62
        y = 55
    if checkpoint == 82:
        print("Destruction Sphere")
    if checkpoint == 83:
        x = -58
        y = 28
    if checkpoint == 84:
        x = -11
        y = 28
    if checkpoint == 85:
        print("Ride ze lift")
    if checkpoint == 86:
        x = -11
        y = 110
    if checkpoint == 87:
        x = -21
        y = 115
    if checkpoint == 88:
        print("Pedestol 1")
    if checkpoint == 89:
        x = -22
        y = 144
    if checkpoint == 90:
        print("Pedestol 2")
    if checkpoint == 91:
        x = -3
        y = 157
    if checkpoint == 92:
        print("Pedestol 3")
    if checkpoint == 93:
        x = 19
        y = 146
    if checkpoint == 94:
        print("Pedestol 4")
    if checkpoint == 95:
        x = 20
        y = 117
    if checkpoint == 96:
        print("Pedestol 5")
    if checkpoint == 97:
        x = 9
        y = 106
    if checkpoint == 98:
        x = 8
        y = 70
    if checkpoint == 99:
        x = 0
        y = 61
    if checkpoint == 100:
        print("Insert destro sphere")
    if checkpoint == 101:
        x = 22
        y = 42
    if checkpoint == 102:
        print("Destro chest")
    if checkpoint == 103:
        x = -26
        y = 37
    if checkpoint == 104:
        print("End of Trials")
    return [x,y]

def moonflow(checkpoint):
    if checkpoint == 0:
        x = -138
        y = -254
    if checkpoint == 1:
        x = -179
        y = -262
    if checkpoint == 2:
        print("Picking up chest")
    if checkpoint == 3:
        x = -114
        y = -291
    if checkpoint == 4:
        x = -36
        y = -369
    if checkpoint == 5:
        x = -10
        y = -450
    if checkpoint == 6:
        x = 57
        y = -19
    if checkpoint == 7:
        x = 60
        y = -54
    if checkpoint == 8:
        x = 3
        y = -227
    if checkpoint == 9:
        x = -11
        y = -325
    if checkpoint == 10:
        x = -20
        y = -400
    if checkpoint == 11: #Map - Fork in the road
        x = 610
        y = 843
    if checkpoint == 12:
        x = 567
        y = 991
    if checkpoint == 13:
        x = 567
        y = 1200
    if checkpoint == 14: #Start of the long Moonflow path/map
        x = -1004
        y = 1666
    if checkpoint == 15:
        x = -1093
        y = 1529
    if checkpoint == 16:
        x = -1166
        y = 1363
    if checkpoint == 17:
        x = -1218
        y = 1204
    if checkpoint == 18:
        x = -1272
        y = 914
    if checkpoint == 19:
        x = -1316
        y = 787
    if checkpoint == 20:
        x = -1364
        y = 760
    if checkpoint == 21:
        x = -1535
        y = 653
    if checkpoint == 22:
        x = -1577
        y = 627
    if checkpoint == 23:
        x = -1659
        y = 544
    if checkpoint == 24:
        x = -1713
        y = 479
    if checkpoint == 25:
        x = -1817
        y = 336
    if checkpoint == 26:
        x = -1839
        y = 291
    if checkpoint == 27:
        x = -1869
        y = 129
    if checkpoint == 28:
        x = -1876
        y = -204
    if checkpoint == 29:
        x = -1901
        y = -458
    if checkpoint == 30:
        x = -1895
        y = -504
    if checkpoint == 31:
        x = -1862
        y = -511
    if checkpoint == 32:
        x = -1810
        y = -480
    if checkpoint == 33: #Moonflow chest
        print("Moonflow chest")
    if checkpoint == 34:
        x = -1862
        y = -511
    if checkpoint == 35:
        x = -1901
        y = -513
    if checkpoint == 36:
        x = -1913
        y = -559
    if checkpoint == 37:
        x = -1968
        y = -650
    if checkpoint == 38:
        x = -1970
        y = -900
    if checkpoint == 39: #Actual Moonflow map
        x = -1190
        y = 193
    if checkpoint == 40:
        x = -1118 #Can be used for tuning later.
        y = -614
    if checkpoint == 41:
        x = -1118
        y = -614
    if checkpoint == 42:
        x = -1034
        y = -566
    if checkpoint == 43: #Last before "Whoa a Shoopuff"
        x = -960
        y = -500
    if checkpoint == 44:
        x = -200
        y = -60
    if checkpoint == 45:
        x = -30
        y = 180
    return [x,y]

def moonflowBankSouth(checkpoint):
    if checkpoint == 0:
        x = -104
        y = 112
    if checkpoint == 1:
        x = -108
        y = 97
    if checkpoint == 2:
        x = -83
        y = 69
    if checkpoint == 3:
        x = -71
        y = 48
    return [x,y]

def moonflowBankNorth(checkpoint):
    if checkpoint == 0:
        x = -305
        y = 184
    if checkpoint == 1:
        x = -400
        y = 150
    if checkpoint == 2:
        x = -1001
        y = -767
    if checkpoint == 3: #Rikku scene
        x = -1135
        y = -807
    if checkpoint == 4:
        x = -1123
        y = -759
    if checkpoint == 5:
        x = -1134
        y = -699
    if checkpoint == 6:
        x = -1125
        y = -627
    if checkpoint == 7: #Rikku steal/mix tutorial.
        print("Rikku steal/mix tutorial.")
    if checkpoint == 8:
        x = -1076
        y = -553
    if checkpoint == 9:
        x = -944
        y = -384
    if checkpoint == 10:
        x = -892
        y = -327
    if checkpoint == 11: #Into the Guadosalam entrance map
        x = -800
        y = -270
    if checkpoint == 12:
        x = 313
        y = -911
    if checkpoint == 13:
        x = 269
        y = -812
    if checkpoint == 14:
        x = 130
        y = -443
    if checkpoint == 15:
        x = 98
        y = -300
    if checkpoint == 16:
        x = 86
        y = -190
    if checkpoint == 17:
        x = 74
        y = 32
    if checkpoint == 18:
        x = 70
        y = 200
    return [x,y]

def guadoSkip(checkpoint):
    if checkpoint == 0:
        x = 4
        y = 0
    if checkpoint == 1:
        x = -59
        y = 80
    if checkpoint == 2:
        x = -59
        y = 97
    if checkpoint == 3:
        x = -43
        y = 105
    if checkpoint == 4:
        x = -33
        y = 92
    if checkpoint == 5:
        print("Test if skip was successful.")
    if checkpoint == 6:
        x = -24
        y = 61
    if checkpoint == 7:
        x = -43
        y = 55
    if checkpoint == 8:
        x = -60
        y = 83
    if checkpoint == 9:
        x = -80
        y = 137
    if checkpoint == 10:
        x = -78
        y = 166
    if checkpoint == 11:
        x = -70
        y = 250
    if checkpoint == 18:
        x = -24
        y = 61
    if checkpoint == 19:
        x = -43
        y = 55
    if checkpoint == 20:
        print("Guado skip failed.")
        x = -59
        y = 67
    if checkpoint == 21:
        print("Shelinda scene")
    if checkpoint == 22:
        x = -27
        y = 87
    if checkpoint == 23:
        x = -25
        y = 144
    if checkpoint == 24:
        print("Back to the party")
    if checkpoint == 25:
        x = -33
        y = 92
    if checkpoint == 26:
        x = -24
        y = 61
    if checkpoint == 27:
        x = -43
        y = 55
    if checkpoint == 28:
        x = -60
        y = 83
    if checkpoint == 29:
        x = -80
        y = 137
    if checkpoint == 30:
        x = -78
        y = 166
    if checkpoint == 31:
        x = -70
        y = 250
    return [x,y]

def tPlainsSouth(checkpoint):
    if checkpoint == 0:
        x = 16
        y = -961
    if checkpoint == 1:
        x = 9
        y = -934
    if checkpoint == 2:
        x = 0
        y = -816
    if checkpoint == 3:
        x = -22
        y = -592
    if checkpoint == 4:
        x = -21
        y = -273
    if checkpoint == 5:
        x = -72
        y = -56
    if checkpoint == 6:
        x = -72
        y = 42
    if checkpoint == 7:
        x = 34
        y = 330
    if checkpoint == 8:
        x = 70
        y = 475
    if checkpoint == 9:
        x = 81
        y = 529
    if checkpoint == 10:
        x = 48
        y = 680
    if checkpoint == 11:
        x = 54
        y = 865
    if checkpoint == 12:
        x = 54
        y = 1200
    return [x,y]

def tPlainsNorth(checkpoint):
    if checkpoint == 0:
        x = -92
        y = -1076
    if checkpoint == 1:
        x = -52
        y = -875
    if checkpoint == 2:
        x = 22
        y = -503
    if checkpoint == 3:
        x = 67
        y = -425
    if checkpoint == 4:
        x = 95
        y = -320
    if checkpoint == 5:
        x = 83
        y = -145
    if checkpoint == 6:
        x = 77
        y = -12
    if checkpoint == 7:
        x = 64
        y = 16
    if checkpoint == 8:
        x = -76
        y = 376
    if checkpoint == 9:
        x = -83
        y = 468
    if checkpoint == 10:
        x = 105
        y = 709
    if checkpoint == 11:
        x = 95
        y = 918
    if checkpoint == 12:
        x = 60
        y = 1500
    return [x,y]

def mWoods(checkpoint):
    if checkpoint == 0:
        x = 206
        y = 41
    if checkpoint == 1:
        x = 142
        y = 62
    if checkpoint == 2:
        x = 102
        y = 108
    if checkpoint == 3:
        x = 34
        y = 114
    if checkpoint == 4:
        x = 6
        y = 87
    if checkpoint == 5:
        x = 15
        y = 2
    if checkpoint == 6:
        x = 1
        y = -6
    if checkpoint == 7:
        x = -66
        y = 10
    if checkpoint == 8:
        x = -109
        y = 60
    if checkpoint == 9:
        x = -113
        y = 116
    if checkpoint == 10:
        x = -96
        y = 172
    if checkpoint == 11:
        x = -115
        y = 214
    if checkpoint == 12:
        x = -131
        y = 234
    if checkpoint == 13:
        x = -131
        y = 234
    if checkpoint == 14: #First chest
        print("First chest")
    if checkpoint == 15:
        x = -154
        y = 247
    if checkpoint == 16:
        x = -201
        y = 230
    if checkpoint == 17:
        x = -250
        y = 200
    if checkpoint == 18: #Second map - with the loop
        x = 57
        y = 60
    if checkpoint == 19:
        x = 56
        y = -60
    if checkpoint == 20:
        x = 47
        y = -72
    if checkpoint == 21:
        x = 25
        y = -78
    if checkpoint == 22:
        x = -45
        y = -31
    if checkpoint == 23:
        x = -81
        y = 84
    if checkpoint == 24:
        x = -110
        y = 120
    if checkpoint == 25:
        x = -165
        y = 120
    if checkpoint == 26:
        x = -201
        y = 81
    if checkpoint == 27:
        x = -185
        y = 25
    if checkpoint == 28:
        x = -158
        y = 8
    if checkpoint == 29:
        x = -89
        y = 56
    if checkpoint == 30:
        x = -49
        y = 76
    if checkpoint == 31:
        x = 161
        y = 24
    if checkpoint == 32: #Bartello
        x = 178
        y = -46
    if checkpoint == 33:
        x = 168
        y = -134
    if checkpoint == 34:
        x = 105
        y = -174
    if checkpoint == 35:
        x = -28
        y = -188
    if checkpoint == 36: #Butterfly guy
        x = -97
        y = -214
    if checkpoint == 37: #Touch butterfly
        x = -146
        y = -204
    if checkpoint == 38:
        x = -182
        y = -131
    if checkpoint == 39:
        x = -250
        y = -50
    if checkpoint == 40: #Into next screen
        x = -505
        y = 36
    if checkpoint == 41:
        x = -508
        y = 139
    if checkpoint == 42:
        x = -527
        y = 148
    if checkpoint == 43:
        x = -580
        y = 82
    if checkpoint == 44:
        x = -569
        y = 43
    if checkpoint == 45:
        x = -523
        y = 37
    if checkpoint == 46:
        x = -449
        y = 16
    if checkpoint == 47:
        x = -447
        y = -8
    if checkpoint == 48:
        x = -481
        y = -72
    if checkpoint == 49:
        x = -562
        y = -151
    if checkpoint == 50:
        x = -590
        y = -151
    if checkpoint == 51:
        x = -620
        y = -137
    if checkpoint == 52:
        x = -675
        y = -84
    if checkpoint == 53:
        x = -752
        y = 2
    if checkpoint == 54:
        x = -737
        y = 62
    if checkpoint == 55:
        x = -717
        y = 115
    if checkpoint == 56:
        x = -717
        y = 163
    if checkpoint == 57:
        x = -645
        y = 167
    if checkpoint == 58:
        x = -612
        y = 144
    if checkpoint == 59: # Check for completion status
        print("Check for completion status")
    if checkpoint == 60:
        x = -601
        y = 126
    if checkpoint == 61:
        x = -596
        y = 59
    if checkpoint == 62:
        x = -613
        y = -53
    if checkpoint == 63:
        x = -654
        y = -98
    if checkpoint == 64:
        x = -750
        y = -200
    return [x,y]

def mTempleApproach(checkpoint):
    if checkpoint == 0:
        x = 22
        y = 538
    if checkpoint == 1:
        x = 30
        y = 650
    if checkpoint == 2: #From snowmobile screen to curve screen
        x = 39
        y = 86
    if checkpoint == 3:
        x = 87
        y = 202
    if checkpoint == 4:
        x = 166
        y = 298
    if checkpoint == 5:
        x = 216
        y = 323
    if checkpoint == 6:
        x = 310
        y = 358
    if checkpoint == 7:
        x = 396
        y = 382
    if checkpoint == 8:
        x = 472
        y = 378
    if checkpoint == 9:
        x = 526
        y = 338
    if checkpoint == 10:
        x = 646
        y = 270
    if checkpoint == 11:
        x = 714
        y = 217
    if checkpoint == 12:
        x = 778
        y = 101
    if checkpoint == 13:
        x = 801
        y = -45
    if checkpoint == 14:
        x = 801
        y = -206
    if checkpoint == 15:
        x = 815
        y = -455
    if checkpoint == 16: #Into the door (dial in)
        x = 801
        y = -500
    return [x,y]

def templeFoyer(checkpoint):
    if checkpoint == 0:
        x = -18
        y = -124
    if checkpoint == 1:
        print("Touch save sphere")
    if checkpoint == 2:
        x = 19
        y = -103
    if checkpoint == 3:
        x = 23
        y = -102
    if checkpoint == 4:
        print("Trommell")
    if checkpoint == 5:
        print("Lining up for skip")
    if checkpoint == 6:
        x = -73
        y = -14
    if checkpoint == 7:
        x = -109
        y = -22
    if checkpoint == 8:
        print("Chest")
    if checkpoint == 9:
        x = -73
        y = -14
    if checkpoint == 10:
        x = -21
        y = 4
    if checkpoint == 11:
        print("Check if skip successful")
    if checkpoint == 12:
        x = 2
        y = 38
    if checkpoint == 13:
        x = 0
        y = 103
    if checkpoint == 14:
        print("Check if pause necessary")
    if checkpoint == 15: #Into the room before Seymour
        x = 0
        y = 300
    if checkpoint == 16: #Into Seymour's room
        x = 0
        y = -300
    if checkpoint == 20: #Skip fail, use this path instead.
        x = 16
        y = 30
    if checkpoint == 21:
        x = 41
        y = 59
    if checkpoint == 22:
        x = 59
        y = 118
    if checkpoint == 23:
        print("Into the door, Jyscal sphere")
    if checkpoint == 24:
        print("And back out again")
    if checkpoint == 25:
        x = 35
        y = 48
    if checkpoint == 26:
        x = 15
        y = 31
    return [x,y]

def mTempleTrials(checkpoint):
    if checkpoint == 0:
        x = 2
        y = -114
    if checkpoint == 1:
        x = 2
        y = -200
    if checkpoint == 2:
        print("Activate the trials")
    if checkpoint == 3:
        x = -12
        y = -116
    if checkpoint == 4:
        x = -33
        y = -113
    if checkpoint == 5:
        x = -50
        y = -88
    if checkpoint == 6:
        x = -66
        y = -16
    if checkpoint == 7:
        x = -47
        y = -12
    if checkpoint == 8:
        x = 31
        y = 4
    if checkpoint == 9:
        print("Push pedestol")
    if checkpoint == 10:
        x = 18
        y = 52
    if checkpoint == 11:
        x = 6
        y = 83
    if checkpoint == 12:
        x = 2
        y = 107
    if checkpoint == 13:
        print("Grab first Mac Sphere")
    if checkpoint == 14:
        x = 11
        y = 71
    if checkpoint == 15:
        x = 26
        y = 44
    if checkpoint == 16:
        x = 31
        y = 43
    if checkpoint == 17:
        print("Place first Mac Sphere")
    if checkpoint == 18:
        x = 12
        y = 2
    if checkpoint == 19:
        x = 0
        y = 3
    if checkpoint == 20:
        print("Pick up Glyph sphere")
    if checkpoint == 21:
        x = 12
        y = 2
    if checkpoint == 22:
        x = 41
        y = 44
    if checkpoint == 23:
        x = 41
        y = 49
    if checkpoint == 24:
        print("Push pedestol")
    if checkpoint == 25: #Spot next to the ramp-sphere
        x = -77
        y = 54
    if checkpoint == 26:
        x = -80
        y = 24
    if checkpoint == 27: #Bottom of the ramp
        x = -15
        y = 7
    if checkpoint == 28:
        x = 0
        y = 4
    if checkpoint == 29:
        print("Push pedestol")
    if checkpoint == 30:
        x = -11
        y = -27
    if checkpoint == 31:
        x = -9
        y = -49
    if checkpoint == 32:
        print("Insert glyph sphere")
    if checkpoint == 33:
        x = -15
        y = 7
    if checkpoint == 34:
        x = -80
        y = 24
    if checkpoint == 35:
        x = -77
        y = 54
    if checkpoint == 36:
        x = -62
        y = 51
    if checkpoint == 37:
        x = -21
        y = -40
    if checkpoint == 38:
        x = -19
        y = -53
    if checkpoint == 39:
        print("Second Mac sphere")
    if checkpoint == 40:
        x = -21
        y = -40
    if checkpoint == 41:
        x = -62
        y = 51
    if checkpoint == 42:
        x = -77
        y = 54
    if checkpoint == 43:
        x = -80
        y = 24
    if checkpoint == 44:
        x = -15
        y = 7
    if checkpoint == 45:
        x = 11
        y = -32
    if checkpoint == 46:
        print("Second Mac sphere")
    if checkpoint == 47:
        x = 10
        y = -27
    if checkpoint == 48:
        x = -15
        y = 7
    if checkpoint == 49:
        x = -80
        y = 24
    if checkpoint == 50:
        x = -77
        y = 54
    if checkpoint == 51:
        print("Third Mac sphere")
    if checkpoint == 52:
        x = -3
        y = 4
    if checkpoint == 53:
        print("Third Mac sphere")
    if checkpoint == 54: #Ready to get out of here
        x = -68
        y = -17
    if checkpoint == 55:
        x = -48
        y = -93
    if checkpoint == 56:
        x = -20
        y = -116
    if checkpoint == 57:
        x = -5
        y = -106
    if checkpoint == 58:
        print("Trials - end")
    return [x,y]

def mTempleEscape(checkpoint):
    if checkpoint == 0:
        x = 807
        y = -263
    if checkpoint == 1:
        x = 817
        y = -244
    if checkpoint == 2:
        print("Touching save sphere")
    if checkpoint == 3:
        x = 815
        y = -227
    if checkpoint == 4:
        x = 815
        y = -206
    if checkpoint == 5: #Start of turn
        x = 801
        y = -45
    if checkpoint == 6:
        x = 778
        y = 101
    if checkpoint == 7:
        x = 714
        y = 217
    if checkpoint == 8:
        x = 646
        y = 270
    if checkpoint == 9:
        x = 526
        y = 338
    if checkpoint == 10:
        x = 472
        y = 378
    if checkpoint == 11:
        x = 396
        y = 382
    if checkpoint == 12:
        x = 310
        y = 358
    if checkpoint == 13:
        x = 216
        y = 323
    if checkpoint == 14:
        x = 166
        y = 298
    if checkpoint == 15:
        x = 87
        y = 202
    if checkpoint == 16:
        x = 39
        y = 86
    if checkpoint == 17:
        x = -9
        y = -38
    if checkpoint == 18:
        x = -50
        y = -100
    if checkpoint == 19: #Back to the snowmobiles
        x = -13
        y = 410
    if checkpoint == 20:
        x = 6
        y = 363
    if checkpoint == 21:
        x = 44
        y = 320
    if checkpoint == 22:
        x = 51
        y = 274
    if checkpoint == 23:
        x = 40
        y = 243
    if checkpoint == 24:
        x = 25
        y = 218
    if checkpoint == 25:
        x = -32
        y = 196
    if checkpoint == 26:
        x = -30
        y = 169
    if checkpoint == 27:
        x = -28
        y = 63
    if checkpoint == 28:
        x = -20
        y = -159
    if checkpoint == 29:
        x = -8
        y = -269
    if checkpoint == 30:
        x = 13
        y = -420
    if checkpoint == 31:
        x = 33
        y = -565
    if checkpoint == 32:
        x = 33
        y = -700
    return [x,y]

def desert(checkpoint):
    if checkpoint == 0:
        x = 0
        y = -74
    if checkpoint == 1:
        x = 20
        y = -69
    if checkpoint == 2:
        print("Touching save sphere")
    if checkpoint == 3:
        x = 3
        y = -79
    if checkpoint == 4:
        x = -13
        y = -128
    if checkpoint == 5:
        x = 12
        y = -288
    if checkpoint == 6:
        x = 134
        y = -440
    if checkpoint == 7:
        x = 147
        y = -421
    if checkpoint == 8:
        x = 197
        y = -387
    if checkpoint == 9:
        print("Map change")
    if checkpoint == 10:
        x = 172
        y = -569
    if checkpoint == 11:
        x = 441
        y = -366
    if checkpoint == 12:
        x = 228
        y = -523
    if checkpoint == 13:
        x = 206
        y = -534
    if checkpoint == 14:
        x = 89
        y = -522
    if checkpoint == 15:
        x = -26
        y = -523
    if checkpoint == 16:
        x = -120
        y = -494
    if checkpoint == 17:
        x = -186
        y = -395
    if checkpoint == 18:
        x = -158
        y = -346
    if checkpoint == 19:
        x = 44
        y = -250
    if checkpoint == 20:
        x = 138
        y = -200
    if checkpoint == 21:
        x = 164
        y = -134
    if checkpoint == 22:
        x = 190
        y = -8
    if checkpoint == 23:
        x = 199
        y = 28
    if checkpoint == 24:
        print("Touching save sphere")
    if checkpoint == 25:
        x = 187
        y = 26
    if checkpoint == 26:
        x = 170
        y = 29
    if checkpoint == 27:
        x = 160
        y = 46
    if checkpoint == 28:
        x = 180
        y = 67
    if checkpoint == 29:
        x = 253
        y = 116
    if checkpoint == 30:
        x = 352
        y = 126
    if checkpoint == 31: #Machina battle mid-path
        x = 478
        y = 139
    if checkpoint == 32:
        x = 552
        y = 157
    if checkpoint == 33:
        x = 594
        y = 224
    if checkpoint == 34:
        x = 659
        y = 444
    if checkpoint == 35:
        x = 657
        y = 698
    if checkpoint == 36:
        x = 664
        y = 790
    if checkpoint == 37:
        x = 698
        y = 854
    if checkpoint == 38:
        x = 800
        y = 1000
    if checkpoint == 39: #Large open map with two directions
        x = 333
        y = -501
    if checkpoint == 40:
        x = -70
        y = 177
    if checkpoint == 41:
        x = -158
        y = 278
    if checkpoint == 42:
        x = -278
        y = 360
    if checkpoint == 43: #Extra spots for future precision if needed
        x = -278
        y = 360
    if checkpoint == 44: #Extra spots for future precision if needed
        x = -278
        y = 360
    if checkpoint == 45:
        x = -356
        y = 468
    if checkpoint == 46:
        x = -426
        y = 550
    if checkpoint == 47:
        x = -624
        y = 693
    if checkpoint == 48:
        x = -667
        y = 773
    if checkpoint == 49:
        x = -680
        y = 850
    if checkpoint == 50: #Final map before Home
        x = -252
        y = -91
    if checkpoint == 51:
        x = -192
        y = 45
    if checkpoint == 52:
        x = -41
        y = 419
    if checkpoint == 53: #Sandragora #1
        print("Sandragora #1")
    if checkpoint == 54:
        x = -61
        y = 443
    if checkpoint == 55:
        x = -160
        y = 614
    if checkpoint == 56:
        x = -267
        y = 762
    if checkpoint == 57: #Sandragora #2
        x = -294
        y = 820
    if checkpoint == 58:
        x = -294
        y = 886
    if checkpoint == 59:
        print("Test for area completion")
    if checkpoint == 60:
        x = -300
        y = 1000
    return [x,y]

def bevelleTrials(checkpoint):
    if checkpoint == 0:
        x = 64
        y = 177
    if checkpoint == 1:
        x = 75
        y = 200
    if checkpoint == 2:
        x = -19
        y = -62
    if checkpoint == 3:
        print("First pedestol.")
    if checkpoint == 4:
        print("Missed first alcove, recovering.")
    if checkpoint == 5:
        x = -50
        y = 88
    if checkpoint == 6:
        x = -66
        y = 93
    if checkpoint == 7:
        print("First Bevelle sphere, and then more gliding.")
    if checkpoint == 8:
        x = 13
        y = 88
    if checkpoint == 9:
        x = 13
        y = 93
    if checkpoint == 10:
        print("Insert Bevelle sphere. Activate lower areas.")
    if checkpoint == 11:
        x = 27
        y = 92
    if checkpoint == 12:
        x = 26
        y = 86
    if checkpoint == 13:
        print("Down to the lower areas.")
    if checkpoint == 14:
        x = 397
        y = 357
    if checkpoint == 15:
        x = 501
        y = 363
    if checkpoint == 16:
        print("Take sphere from second alcove")
    if checkpoint == 17:
        x = 406
        y = 364
    if checkpoint == 18:
        print("To third alcove, and insert Glyph sphere")
    if checkpoint == 19:
        x = 353
        y = 531
    if checkpoint == 20:
        x = 367
        y = 532
    if checkpoint == 21:
        x = 370
        y = 526
    if checkpoint == 22:
        print("Remove Bevelle sphere")
    if checkpoint == 23:
        x = 367
        y = 532
    if checkpoint == 24:
        print("Insert Bevelle sphere")
    if checkpoint == 25:
        x = 353
        y = 531
    if checkpoint == 26:
        x = 342
        y = 527
    if checkpoint == 27:
        x = 352
        y = 525
    if checkpoint == 28:
        print("Take Glyph sphere")
    if checkpoint == 29:
        x = 367
        y = 532
    if checkpoint == 30:
        x = 374
        y = 526
    if checkpoint == 31:
        x = 431
        y = 527
    if checkpoint == 32:
        print("Insert Glyph sphere")
    if checkpoint == 33:
        x = 499
        y = 522
    if checkpoint == 34:
        print("Take Destro sphere")
    if checkpoint == 35:
        x = 367
        y = 532
    if checkpoint == 36:
        x = 353
        y = 531
    if checkpoint == 37:
        x = 342
        y = 525
    if checkpoint == 38:
        x = 352
        y = 525
    if checkpoint == 39:
        print("Insert Destro sphere")
    if checkpoint == 40:
        x = 349
        y = 526
    if checkpoint == 41:
        print("Remove Bevelle sphere")
    if checkpoint == 42:
        x = 370
        y = 526
    if checkpoint == 43:
        x = 366
        y = 524
    if checkpoint == 44:
        print("Insert Bevelle sphere, and back on the track.")
    if checkpoint == 45:
        x = 392
        y = 367
    if checkpoint == 46:
        print("Take Destro sphere")
    if checkpoint == 47:
        x = 393
        y = 356
    if checkpoint == 48:
        x = 397
        y = 357
    if checkpoint == 49:
        x = 501
        y = 363
    if checkpoint == 50:
        print("Insert Destro sphere")
    if checkpoint == 51:
        x = 406
        y = 364
    if checkpoint == 52:
        print("Back on track, to the exit")
    if checkpoint == 53: #Final map with chests.
        x = 95
        y = 271
    if checkpoint == 54:
        x = 83
        y = 271
    if checkpoint == 55:
        x = 76
        y = 263
    if checkpoint == 56:
        x = -5
        y = 270
    if checkpoint == 57:
        x = -16
        y = 279
    if checkpoint == 58:
        print("Picking up chest")
    if checkpoint == 59:
        x = -5
        y = 302
    if checkpoint == 60:
        x = -5
        y = 400
    return [x,y]

def seymourNatus():
    x = 15
    y = 150
    return [x,y]

def calmLands(checkpoint):
    if checkpoint == 0:
        x = -332
        y = -1612
    if checkpoint == 1:
        x = -437
        y = -1603
    if checkpoint == 2:
        x = -640
        y = -1591
    if checkpoint == 3:
        x = -757
        y = -1530
    if checkpoint == 4:
        x = -777
        y = -1478
    if checkpoint == 5:
        x = 1045
        y = -8
    if checkpoint == 6:
        x = 1424
        y = 668
    if checkpoint == 7:
        x = 1474
        y = 843
    if checkpoint == 8:
        x = 1542
        y = 1063
    if checkpoint == 9:
        x = 1650
        y = 1170
    return [x,y]

def defenderX(checkpoint):
    if checkpoint == 0:
        x = 62
        y = -66
    if checkpoint == 1:
        x = 118
        y = 111
    if checkpoint == 2:
        x = -14
        y = 104
    if checkpoint == 3:
        x = -9
        y = 240
    if checkpoint == 4:
        x = 12
        y = 350
    return [x,y]

def kelkRonso(checkpoint):
    if checkpoint == 0:
        x = -122
        y = -552
    if checkpoint == 1:
        x = -10
        y = -444
    if checkpoint == 2:
        x = 23
        y = -369
    if checkpoint == 3:
        x = 21
        y = -192
    if checkpoint == 4:
        x = 17
        y = 146
    if checkpoint == 5:
        x = 50
        y = 290
    if checkpoint == 6:
        x = 80
        y = 550
    return [x,y]

def gagazetSnow(checkpoint):
    if checkpoint == 0:
        x = 18
        y = 45
    if checkpoint == 1:
        x = 57
        y = 328
    if checkpoint == 2:
        x = 40
        y = 375
    if checkpoint == 3:
        x = -1
        y = 421
    if checkpoint == 4:
        x = -49
        y = 444
    if checkpoint == 5:
        x = -237
        y = 311
    if checkpoint == 6:
        x = -273
        y = 315
    if checkpoint == 7:
        x = -327
        y = 383
    if checkpoint == 8:
        x = -369
        y = 465
    if checkpoint == 9:
        x = -409
        y = 460
    if checkpoint == 10:
        x = -538
        y = 264
    if checkpoint == 11:
        x = -619
        y = 210
    if checkpoint == 12:
        x = -913
        y = 163
    if checkpoint == 13:
        x = -941
        y = 191
    if checkpoint == 14:
        x = -903
        y = 330
    if checkpoint == 15:
        x = -878
        y = 433
    if checkpoint == 16:
        x = -830
        y = 540
    if checkpoint == 17:
        x = -728
        y = 565
    if checkpoint == 18:
        x = -664
        y = 537
    if checkpoint == 19:
        x = -633
        y = 497
    if checkpoint == 20:
        x = -599
        y = 370
    if checkpoint == 21:
        x = -592
        y = 262
    if checkpoint == 22:
        x = -600
        y = 223
    if checkpoint == 23:
        x = -790
        y = 207
    if checkpoint == 24:
        x = -877
        y = 232
    if checkpoint == 25:
        x = -1034
        y = 491
    if checkpoint == 26:
        x = -1065
        y = 502
    if checkpoint == 27:
        x = -1133
        y = 446
    if checkpoint == 28:
        x = -1248
        y = 166
    if checkpoint == 29:
        x = -1307
        y = -1
    if checkpoint == 30:
        x = -1365
        y = -85
    return [x,y]

def Flux(checkpoint):
    if checkpoint == 0:
        x = -368
        y = -330
    if checkpoint == 1:
        x = -303
        y = -259
    if checkpoint == 2:
        x = 31
        y = -202
    if checkpoint == 3:
        x = 146
        y = -285
    if checkpoint == 4:
        x = 173
        y = -343
    if checkpoint == 5:
        x = 167
        y = -550
    if checkpoint == 6:
        x = 150
        y = -619
    return [x,y]

def gagazetDream(checkpoint):
    if checkpoint == 0:
        x = 1140
        y = 87
    if checkpoint == 1:
        x = 1027
        y = 407
    if checkpoint == 2:
        x = 1027
        y = 407
    if checkpoint == 3:
        x = 1008
        y = 503
    if checkpoint == 4:
        x = 985
        y = 549
    if checkpoint == 5:
        x = 1001
        y = 593
    if checkpoint == 6:
        x = 1043
        y = 640
    if checkpoint == 7:
        x = 1070
        y = 640
    return [x,y]

def gagazetCave(checkpoint):
    if checkpoint == 0:
        x = -45
        y = -1252
    if checkpoint == 1:
        x = -27
        y = -1142
    if checkpoint == 2:
        x = 79
        y = -969
    if checkpoint == 3:
        x = 90
        y = -949
    if checkpoint == 4:
        x = 47
        y = -812
    if checkpoint == 5:
        x = 25
        y = -552
    if checkpoint == 6:
        x = 107
        y = -439
    if checkpoint == 7:
        print("Map change, no target from this function.")
    if checkpoint == 8:
        x = -45
        y = -393
    if checkpoint == 9:
        x = 9
        y = -257
    if checkpoint == 10:
        x = 106
        y = 9
    if checkpoint == 11:
        x = 192
        y = 153
    if checkpoint == 13:
        x = 100
        y = -3
    if checkpoint == 14:
        x = 7
        y = -266
    if checkpoint == 15:
        x = -49
        y = -420
    if checkpoint == 16:
        x = -52
        y = -477
    if checkpoint == 17:
        print("Map change, no target from this function.")
    if checkpoint == 18:
        x = 36
        y = -535
    if checkpoint == 19:
        x = 35
        y = -767
    if checkpoint == 20:
        x = 56
        y = -832
    if checkpoint == 21:
        x = 143
        y = -929
    if checkpoint == 22:
        x = 232
        y = -853
    if checkpoint == 23:
        x = 241
        y = -788
    if checkpoint == 24:
        x = 192
        y = -669
    if checkpoint == 25:
        x = 180
        y = -625
    if checkpoint == 26:
        x = 208
        y = -418
    if checkpoint == 27:
        x = 248
        y = -270
    if checkpoint == 28:
        x = 240
        y = -63
    if checkpoint == 29:
        print("Map change, no target from this function.")
    if checkpoint == 30:
        x = 183
        y = 66
    if checkpoint == 31:
        x = 201
        y = 208
    if checkpoint == 32:
        x = 208
        y = 260
    if checkpoint == 33:
        x = 181
        y = 292
    if checkpoint == 34:
        x = 140
        y = 301
    if checkpoint == 35:
        print("Second trial, no target from this function.")
    if checkpoint == 36:
        x = 168
        y = 295
    if checkpoint == 37:
        x = 189
        y = 283
    if checkpoint == 38:
        x = 208
        y = 256
    if checkpoint == 39:
        x = 199
        y = 175
    if checkpoint == 40:
        x = 179
        y = 67
    if checkpoint == 41:
        x = 204
        y = -10
    if checkpoint == 42:
        print("Map change, no target from this function.")
    if checkpoint == 43:
        x = 229
        y = -274
    if checkpoint == 44:
        x = 215
        y = -375
    if checkpoint == 45:
        x = 197
        y = -435
    if checkpoint == 46: #Turn to go up the new stairs
        x = 184
        y = -445
    if checkpoint == 47:
        x = 177
        y = -433
    if checkpoint == 48:
        x = 172
        y = -356
    if checkpoint == 49:
        x = 161
        y = -335
    if checkpoint == 50:
        x = 156
        y = -288
    if checkpoint == 51:
        x = 168
        y = -252
    if checkpoint == 52:
        x = 159
        y = -236
    if checkpoint == 53:
        x = 183
        y = -196
    if checkpoint == 54:
        x = 181
        y = -107
    if checkpoint == 55:
        x = 162
        y = -26
    if checkpoint == 56:
        x = 142
        y = 14
    if checkpoint == 57:
        x = 7
        y = 99
    if checkpoint == 58:
        x = -208
        y = 240
    if checkpoint == 60:
        x = -260
        y = 200
    return [x,y]

def gagazetPeak(checkpoint):
    if checkpoint == 0:
        x = 943
        y = -1055
    if checkpoint == 1:
        x = 860
        y = -994
    if checkpoint == 2:
        x = 787
        y = -839
    if checkpoint == 3:
        print("Miihen agency scene, no target from this function.")
    if checkpoint == 4:
        x = 779
        y = -695
    if checkpoint == 5:
        x = 844
        y = -551
    if checkpoint == 6:
        print("Map change, no target from this function.")
    if checkpoint == 7:
        x = -135
        y = -669
    if checkpoint == 8:
        x = 129
        y = -534
    if checkpoint == 9:
        x = 139
        y = -448
    if checkpoint == 10:
        x = 107
        y = -386
    if checkpoint == 11:
        x = 47
        y = -310
    if checkpoint == 12:
        x = -151
        y = -181
    if checkpoint == 13:
        x = -204
        y = -119
    if checkpoint == 14:
        x = -295
        y = 123
    if checkpoint == 15:
        x = -303
        y = 382
    if checkpoint == 16:
        x = -320
        y = 450
    return [x,y]

def zanarkandOutdoors(checkpoint):
    if checkpoint == 0:
        x = -16
        y = -671
    if checkpoint == 1:
        x = 1
        y = -507
    if checkpoint == 2:
        x = -17
        y = -435
    if checkpoint == 3:
        x = -98
        y = -442
    if checkpoint == 4:
        print("Fortune sphere, no direction from this function.")
    if checkpoint == 5:
        x = -108
        y = -418
    if checkpoint == 6:
        x = -210
        y = -282
    if checkpoint == 7:
        x = -190
        y = -100
    if checkpoint == 8: #Weird cutscene where we don't lose control immediately
        x = -133
        y = 8
    if checkpoint == 9:
        x = -161
        y = 368
    if checkpoint == 10:
        x = -365
        y = 565
    if checkpoint == 11:
        x = -523
        y = 656
    if checkpoint == 12:
        x = -564
        y = 801
    if checkpoint == 13:
        x = -628
        y = 936
    if checkpoint == 14:
        x = -750
        y = 1083
    return [x,y]

def zanarkandDome(checkpoint):
    if checkpoint == 0:
        x = 2
        y = -325
    if checkpoint == 1:
        x = 117
        y = -203
    if checkpoint == 2:
        x = 128
        y = -162
    if checkpoint == 3:
        x = 134
        y = -85
    if checkpoint == 4:
        x = 71
        y = -20
    if checkpoint == 5:
        x = -20
        y = 5
    if checkpoint == 6:
        x = -136
        y = -32
    if checkpoint == 7:
        x = -186
        y = -109
    if checkpoint == 8: #Near save sphere
        x = -144
        y = -124
    if checkpoint == 9:
        x = -132
        y = -105
    if checkpoint == 10: #Seymour scene
        x = -126
        y = 49
    if checkpoint == 11:
        x = -101
        y = 76
    if checkpoint == 12:
        x = 3
        y = 89
    if checkpoint == 13:
        print("Friend sphere, no direction from this function.")
    if checkpoint == 14:
        x = -127
        y = 68
    if checkpoint == 15:
        x = -230
        y = 146
    if checkpoint == 16:
        x = -154
        y = 195
    if checkpoint == 17: #Mini-bridge, running with Braska/Jecht
        x = -73
        y = 232
    if checkpoint == 18:
        x = -27
        y = 286
    if checkpoint == 19:
        x = 7
        y = 386
    if checkpoint == 20:
        x = -5
        y = 600
    if checkpoint == 21:
        x = -12
        y = -188
    if checkpoint == 22:
        x = 3
        y = -96
    if checkpoint == 23:
        x = 23
        y = -80
    if checkpoint == 24:
        print("Luck sphere, no direction from this function.")
    if checkpoint == 25:
        x = -15
        y = -49
    if checkpoint == 26:
        x = 1
        y = 36
    if checkpoint == 27:
        x = 5
        y = 240
    if checkpoint == 28:
        x = -21
        y = 352
    if checkpoint == 29:
        print("Touching save sphere, no direction from this function.")
    if checkpoint == 30:
        x = -3
        y = 360
    if checkpoint == 31:
        x = 1
        y = 500
    return [x,y]

def zanarkandTrials(checkpoint):
    if checkpoint == 0:
        x = 105
        y = -57
    if checkpoint == 1:
        x = 105
        y = -44
    if checkpoint == 2:
        x = 135
        y = -35
    if checkpoint == 3:
        x = 126
        y = -14
    if checkpoint == 4:
        x = 133
        y = 5
    if checkpoint == 5:
        x = 110
        y = 18
    if checkpoint == 6:
        x = 84
        y = 25
    if checkpoint == 7:
        x = 71
        y = 25
    if checkpoint == 8:
        print("First pedetsol, no direction from here.")
    if checkpoint == 9: #First pattern in big room
        x = -1
        y = 11
    if checkpoint == 10:
        x = -4
        y = -6
    if checkpoint == 11:
        x = -25
        y = -26
    if checkpoint == 12:
        x = -53
        y = 18
    if checkpoint == 13:
        x = -79
        y = 24
    if checkpoint == 14:
        x = -106
        y = 19
    if checkpoint == 15:
        x = -125
        y = 4
    if checkpoint == 16:
        x = -157
        y = 45
    if checkpoint == 17:
        x = -103
        y = 66
    if checkpoint == 18:
        x = -93
        y = 86
    if checkpoint == 19:
        x = -90
        y = 123
    if checkpoint == 20:
        print("Picking up Kilika sphere")
    if checkpoint == 21:
        x = -53
        y = 63
    if checkpoint == 22:
        x = 11
        y = 70
    if checkpoint == 23:
        x = 28
        y = 72
    if checkpoint == 24:
        x = 83
        y = 34
    if checkpoint == 25:
        x = 71
        y = 4
    if checkpoint == 26:
        print("Placing Kilika sphere")
    if checkpoint == 27:
        x = 71
        y = -21
    if checkpoint == 28:
        print("Activating second pedestol")
    if checkpoint == 29:
        x = 77
        y = 43
    if checkpoint == 30:
        print("Moving into next room.")
    if checkpoint == 31: #Second pattern in big room
        x = -5
        y = 74
    if checkpoint == 32:
        x = -17
        y = 44
    if checkpoint == 33:
        x = -28
        y = 42
    if checkpoint == 34:
        x = -88
        y = 31
    if checkpoint == 35:
        x = -106
        y = 33
    if checkpoint == 36:
        x = -114
        y = -1
    if checkpoint == 37:
        x = -128
        y = -29
    if checkpoint == 38:
        x = -156
        y = -55
    if checkpoint == 39:
        x = -104
        y = -64
    if checkpoint == 40:
        x = -84
        y = -75
    if checkpoint == 41:
        x = -13
        y = -42
    if checkpoint == 42:
        x = 1
        y = 57
    if checkpoint == 43:
        x = 28
        y = 74
    if checkpoint == 44:
        x = 83
        y = 34
    if checkpoint == 45:
        x = 137
        y = 23
    if checkpoint == 46:
        print("Activating second pedestol")
    if checkpoint == 47:
        x = 84
        y = 45
    if checkpoint == 48:
        print("Moving into next room.")
    if checkpoint == 49: #Third pattern in main room, start.
        x = -5
        y = 74
    if checkpoint == 50:
        x = -17
        y = 45
    if checkpoint == 51:
        x = -27
        y = 44
    if checkpoint == 52:
        x = -57
        y = 67
    if checkpoint == 53:
        x = -94
        y = 85
    if checkpoint == 54:
        x = -106
        y = 60
    if checkpoint == 55:
        x = -116
        y = 40
    if checkpoint == 56:
        x = -124
        y = 3
    if checkpoint == 57:
        x = -115
        y = -31
    if checkpoint == 58:
        x = -104
        y = -65
    if checkpoint == 59:
        x = -79
        y = -57
    if checkpoint == 60:
        x = -23
        y = -75
    if checkpoint == 61:
        x = -15
        y = -43
    if checkpoint == 62:
        x = 3
        y = 65
    if checkpoint == 63:
        x = 32
        y = 73
    if checkpoint == 64:
        x = 83
        y = 34
    if checkpoint == 65:
        x = 137
        y = -22
    if checkpoint == 66:
        print("Activating second pedestol")
    if checkpoint == 67:
        x = 84
        y = 45
    if checkpoint == 68:
        print("Moving into next room.")
    if checkpoint == 69: #Last pattern in main room.
        x = -6
        y = 75
    if checkpoint == 70:
        x = 0
        y = 6
    if checkpoint == 71:
        x = -14
        y = -46
    if checkpoint == 72:
        x = -24
        y = -75
    if checkpoint == 73:
        x = -86
        y = -75
    if checkpoint == 74:
        x = -104
        y = -67
    if checkpoint == 75:
        x = -124
        y = -5
    if checkpoint == 76:
        x = -136
        y = -1
    if checkpoint == 77:
        x = -155
        y = 46
    if checkpoint == 78:
        x = -104
        y = 78
    if checkpoint == 79:
        x = -92
        y = 88
    if checkpoint == 80:
        x = -68
        y = 110
    if checkpoint == 81: #Pick up Besaid sphere
        print("Picking up Besaid sphere")
    if checkpoint == 82:
        x = -67
        y = 94
    if checkpoint == 83:
        x = 5
        y = 71
    if checkpoint == 84:
        x = 33
        y = 72
    if checkpoint == 85:
        x = 83
        y = 34
    if checkpoint == 86:
        x = 136
        y = -1
    if checkpoint == 87:
        print("Placing Besaid sphere")
    if checkpoint == 88:
        x = 90
        y = 40
    return [x,y]

def yunalescaToAirship(checkpoint):
    if checkpoint == 0:
        x = -4
        y = -179
    if checkpoint == 1:
        x = -4
        y = -300
    if checkpoint == 2:
        x = 0
        y = 55
    if checkpoint == 3:
        x = 0
        y = -200
    if checkpoint == 4:
        x = 0
        y = -72
    if checkpoint == 5:
        x = -2
        y = -132
    if checkpoint == 6:
        x = 0
        y = -160
    if checkpoint == 7:
        x = 0
        y = -200
    if checkpoint == 8:
        x = 0
        y = -500
    if checkpoint == 9:
        x = -65
        y = -56
    if checkpoint == 10:
        x = -46
        y = -35
    if checkpoint == 11:
        x = 3
        y = 62
    if checkpoint == 12:
        x = 28
        y = 68
    if checkpoint == 13:
        x = 83
        y = 34
    if checkpoint == 14:
        x = 99
        y = -67
    if checkpoint == 15:
        x = 100
        y = -93
    if checkpoint == 16:
        x = 100
        y = -200
    if checkpoint == 17:
        x = -1
        y = 243
    if checkpoint == 18:
        x = -3
        y = 148
    if checkpoint == 19:
        x = -5
        y = 39
    if checkpoint == 20:
        x = -12
        y = -53
    if checkpoint == 21:
        x = -6
        y = -89
    if checkpoint == 22:
        x = -10
        y = -200
    if checkpoint == 23:
        x = -10
        y = -400
    if checkpoint == 24:
        x = 125
        y = 1423
    return [x,y]

def template(checkpoint):
    if checkpoint == 0:
        x = 0
        y = 0
    if checkpoint == 1:
        x = 0
        y = 0
    if checkpoint == 2:
        x = 0
        y = 0
    if checkpoint == 3:
        x = 0
        y = 0
    if checkpoint == 4:
        x = 0
        y = 0
    if checkpoint == 5:
        x = 0
        y = 0
    if checkpoint == 6:
        x = 0
        y = 0
    if checkpoint == 7:
        x = 0
        y = 0
    if checkpoint == 8:
        x = 0
        y = 0
    if checkpoint == 9:
        x = 0
        y = 0
    if checkpoint == 10:
        x = 0
        y = 0
    if checkpoint == 11:
        x = 0
        y = 0
    if checkpoint == 12:
        x = 0
        y = 0
    if checkpoint == 13:
        x = 0
        y = 0
    if checkpoint == 14:
        x = 0
        y = 0
    if checkpoint == 15:
        x = 0
        y = 0
    if checkpoint == 16:
        x = 0
        y = 0
    if checkpoint == 17:
        x = 0
        y = 0
    if checkpoint == 18:
        x = 0
        y = 0
    if checkpoint == 19:
        x = 0
        y = 0
    if checkpoint == 20:
        x = 0
        y = 0
    if checkpoint == 21:
        x = 0
        y = 0
    if checkpoint == 22:
        x = 0
        y = 0
    if checkpoint == 23:
        x = 0
        y = 0
    if checkpoint == 24:
        x = 0
        y = 0
    if checkpoint == 25:
        x = 0
        y = 0
    if checkpoint == 26:
        x = 0
        y = 0
    if checkpoint == 27:
        x = 0
        y = 0
    if checkpoint == 28:
        x = 0
        y = 0
    if checkpoint == 29:
        x = 0
        y = 0
    if checkpoint == 30:
        x = 0
        y = 0
    if checkpoint == 31:
        x = 0
        y = 0
    if checkpoint == 32:
        x = 0
        y = 0
    if checkpoint == 33:
        x = 0
        y = 0
    if checkpoint == 34:
        x = 0
        y = 0
    if checkpoint == 35:
        x = 0
        y = 0
    if checkpoint == 36:
        x = 0
        y = 0
    if checkpoint == 37:
        x = 0
        y = 0
    if checkpoint == 38:
        x = 0
        y = 0
    if checkpoint == 39:
        x = 0
        y = 0
    if checkpoint == 40:
        x = 0
        y = 0
    if checkpoint == 41:
        x = 0
        y = 0
    if checkpoint == 42:
        x = 0
        y = 0
    if checkpoint == 43:
        x = 0
        y = 0
    if checkpoint == 44:
        x = 0
        y = 0
    if checkpoint == 45:
        x = 0
        y = 0
    if checkpoint == 46:
        x = 0
        y = 0
    if checkpoint == 47:
        x = 0
        y = 0
    if checkpoint == 48:
        x = 0
        y = 0
    if checkpoint == 49:
        x = 0
        y = 0
    if checkpoint == 50:
        x = 0
        y = 0
    return [x,y]
