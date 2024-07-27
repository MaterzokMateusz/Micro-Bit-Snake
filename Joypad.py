from microbit import *

JoyStick_P = pin8
JoyStick_X = pin1
JoyStick_Y = pin2
KEY_A = pin5
KEY_B = pin11
KEY_C = pin15
KEY_D = pin14
KEY_E = pin13
KEY_F = pin12
DIR = {
    'NONE': 0,
    'U': 1,
    'D': 2,
    'L': 3,
    'R': 4,
    'U_L': 5,
    'U_R': 6,
    'D_L': 7,
    'D_R': 8
}
KEY = {
    'NONE': 0,
    'P': 1,
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 5,
    'E': 6,
    'F': 7
}

class JOYSTICK():
    def __init__(self):
        self.Read_X = JoyStick_X.read_analog()
        self.Read_Y = JoyStick_Y.read_analog()

    def Listen_Dir(self):
        New_X = JoyStick_X.read_analog()
        New_Y = JoyStick_Y.read_analog()

        Dx = abs(self.Read_X - New_X)
        Dy = abs(self.Read_Y - New_Y)

        Right = New_X - self.Read_X
        Left = self.Read_X - New_X
        Up = New_Y - self.Read_Y
        Down = self.Read_Y - New_Y

        # max = 1023
        Precision = 150

        if Right > Precision and Dy < Precision:
            return DIR['R']
        elif Left > Precision and Dy < Precision:
            return DIR['L']
        elif Up > Precision and Dx < Precision:
            return DIR['U']
        elif Down > Precision and Dx < Precision:
            return DIR['D']
        elif Right > Precision and Up > Precision:
            return DIR['U_R']
        elif Right > Precision and Down > Precision:
            return DIR['D_R']
        elif Left > Precision and Up > Precision:
            return DIR['U_L']
        elif Left > Precision and Down > Precision:
            return DIR['D_L']
        else:
            return DIR['NONE']

    def Listen_Key(self):
        if button_a.is_pressed():
            return KEY['A']
        elif button_b.is_pressed():
            return KEY['B']
        elif KEY_C.read_digital() == 0:
            return KEY['C']
        elif KEY_D.read_digital() == 0:
            return KEY['D']
        elif KEY_E.read_digital() == 0:
            return KEY['E']
        elif KEY_F.read_digital() == 0:
            return KEY['F']
        elif JoyStick_P.read_digital() == 0:
            return KEY['P']
        else:
            return KEY['NONE']

    def Test(self,button,direction):
        if button == KEY['A']:
            display.show("A")
            sleep(500)
        elif button == KEY['B']:
            display.show("B")
            sleep(500)
        elif button == KEY['C']:
            display.show("C")
            sleep(500)
        elif button == KEY['D']:
            display.show("D")
            sleep(500)
        elif button == KEY['E']:
            display.show("E")
            sleep(500)
        elif button == KEY['F']:
            display.show("F")
            sleep(500)
        elif direction == DIR['R']:
            display.show(Image.ARROW_E)
            sleep(500)
        elif direction == DIR['L']:
            display.show(Image.ARROW_W)
            sleep(500)
        elif direction == DIR['U']:
            display.show(Image.ARROW_N)
            sleep(500)
        elif direction == DIR['D']:
            display.show(Image.ARROW_S)
            sleep(500)

