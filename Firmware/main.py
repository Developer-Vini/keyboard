import board

import digitalio

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


