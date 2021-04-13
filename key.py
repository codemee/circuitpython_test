import time
import usb_hid
from digitalio import DigitalInOut, Direction, Pull
import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

btn = DigitalInOut(board.GP28)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

kbd = Keyboard(usb_hid.devices)
ctl = ConsumerControl(usb_hid.devices)

prev = False

while True:
    if prev == False and btn.value == True:
        time.sleep(0.02)
        if btn.value == True:
            print("pressed")
            # 我的截圖軟體設定快捷鍵是 CTRL+SHIFT+A
            kbd.send(Keycode.PRINT_SCREEN)
            ctl.send(ConsumerControlCode.VOLUME_INCREMENT)
    prev = btn.value