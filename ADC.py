import board
import analogio
import time

a2 = analogio.AnalogIn(board.A2)
while True:
    print(a2.value)
    time.sleep(0.20)
