from machine import Pin, I2C
import SH1106
import time

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
display = SH1106.SH1106_I2C(128, 64, i2c, Pin(2), 0x3c)
display.sleep(False)
display.fill(0)

import math
import random

def poem():
    sentences = [
        "a gale wind breaks apart the fence",
        "padding silently across bricks and rubble",
        "the fox twitches her nose",
        "ones and zeroes fly across the sky in invisible formations",
        "spiralling into the sun's gaze",
        "the shadow observes silently",
        "resting in the cold",
        "an alarm bell rings somewhere across the skyline",
        "a siren wails and cuts short",
        "children play tig on electric scooters",
        "cracks in the pavement widen, spread apart by the tendrils of life growing inside",
        "nobody had the chance to say no",
        "they came for everybody in the end",
        "the crunch of a crisp packet as a wheel skids across it",
        "a lumbering yet fragile edifice",
        "like the light on a winter morning",
        "mist unfurls itself above the lake, spreading tiny fingers into the sky",
        "and telegraph wires hum in the storm"
        ]

    new = []

    for i in range(len(sentences)):
        r = random.randint(0, len(sentences)-1)
        if sentences[r] in new:
            pass
        else:
            new.append(sentences[r])


    for i in range(len(new)):
        L = len(new[i])
        display.fill(0)
        if L > 15:
            div = L % 15
            if div == 0:
                n = L/15
                for k in range(0, n):
                    m=(k+1)%4
                    if (k+1) % 4 == 0:
                        display.fill(0)
                    t = new[i][k*15:(15*(k+1))]
                    display.text(t, 0, 15*m, 1)
                    display.show()
                    time.sleep(1)
                    
            else:
                w = L - div
                n = w/15
                for k in range(0, n+div):
                    m=(k+1)%4
                    if (k+1) % 4 == 0 :
                        display.fill(0)                        
                    t = new[i][k*15:(15*(k+1))]
                    display.text(t, 0, 15*m, 1)
                    display.show()
                    time.sleep(1)        

while True:
    poem()
    time.sleep(30)
