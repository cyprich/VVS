import time
from machine import Pin, PWM

print("Hello World")

p = PWM(Pin(5), freq=440)
p.init()

for i in range(1, 9):
    p.freq(int((i * 0.5)*220))
    time.sleep(0.1)

p.deinit()
