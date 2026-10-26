import board

import digitalio

import time

PINOS_COL = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP22
]
PINOS_ROW = [
    board.GP16, board.GP17, board.GP18, board.GP19, board.GP21, board.GP22
]

cols = []
for pin in PINOS_COL:
    cmk = digitalio.DigitalInOut(pin)
    cmk.direction = digitalio.Direction.OUTPUT
    cmk.value = False
    cols.append(c)

rows = []
for pin in PINOS_ROW:
    rmk = digitalio.DigitalInOut(pin)
    rmk.direction = digitalio.Direction.INPUT
    rmk.pull = digitalio.Pull.DOWN 
    rows.append(rmk)

pressed = set()

while True:
    for col_index, collumn in enumerate(cols):
        collumn.value = True
        for row_index, row in enumerate(rows):
            if row.value:
                print("Key: row", row_index, "collumn", col_index)
        collumn.value = False

    for key in now - pressed:
        print("pressed: line", key[0], "col", k[1])
    for key in pressed - now:
        print("solta: line", key[0], "col", k[1])
    
    pressed = now
    time.sleep(0.05)