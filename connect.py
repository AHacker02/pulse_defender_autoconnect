import pulse
import defender_token

if __name__ == "__main__":
    pulse.open()
    # wait for dialog_box
    # r = None
    # while r is None:
    #     r = pyautogui.locateOnScreen("pulse_input_textbox.png")
    pulse.connect(defender_token.get())
