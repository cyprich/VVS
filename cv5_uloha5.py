from machine import Pin, PWM
from cv5_uloha3 import get_user_input_part

def get_user_input() -> list[int]:
    out = list()

    for i in range(4):
        out.append(get_user_input_part(i, 0, 1023))

    out.append(get_user_input_part(5, 20, 20000))

    return out

def cv5():
    r_duty, g_duty, b_duty, buz_vol, buz_freq = get_user_input()

    r = PWM(21, freq=120, duty_u16=r_duty*64)
    g = PWM(11, freq=120, duty_u16=g_duty*64)
    b = PWM(10, freq=120, duty_u16=b_duty*64)

    buz = PWM(5, freq=buz_freq, duty_u16=buz_vol*64)
