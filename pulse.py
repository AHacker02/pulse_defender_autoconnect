from config import *
import pyautogui as ui


def open():
    print("Opening Pulse\n")
    ui.click(MENU_X, MENU_Y)
    ui.click(PRIMARY_X, PRIMARY_Y)
    ui.click(CONNECT_X, CONNECT_Y)


def connect(pulse_token):
    ui.click(INPUT_X,INPUT_Y)
    ui.write(pulse_token)
    ui.click(BUTTON_X,BUTTON_Y)
