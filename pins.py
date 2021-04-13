import microcontroller
import board

# 晶片上的腳位
chip_pin_names = dir(microcontroller.pin)
# 開發板上標示的名稱 (同一腳位可能有多個名稱)
board_pin_names = dir(board)              

for chip_pin_name in chip_pin_names:
    # 取得對應腳位的 Pin 物件
    chip_pin = getattr(microcontroller.pin, chip_pin_name) 
    if isinstance(chip_pin, microcontroller.Pin):
        for board_pin_name in board_pin_names:
            # 取得對應名稱的 Pin 物件
            board_pin = getattr(board, board_pin_name)
            if chip_pin == board_pin: # 若是同一物件, 表示是同一腳位
                # 顯示開發板上的腳位名稱
                print(board_pin_name, end=" ")
        # 換下一個腳位, 換行顯示
        print("")                             
    

        