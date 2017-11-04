import time
from dotstar import Adafruit_DotStar

numpixels = 48

datapin = [23, 25, 4]
clockpin = [24]

data = [
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
]

def cycle():
    strips = [
        Adafruit_DotStar(numpixels, datapin[0], clockpin[0]),
        Adafruit_DotStar(numpixels, datapin[1], clockpin[0]),
        Adafruit_DotStar(numpixels, datapin[2], clockpin[0])
    ]

    for strip in strips:
        strip.begin()

    color = 0x00FF00
    pos = (-1) * len(data[0])

    while True:
        for i, strip in enumerate(strips):
            strip.clear()

            for pixel in range(0, numpixels):
                for j, pixel in enumerate(data[i]):
                    if pixel == 1:
                        strip.setPixelColor(pos + j, color)

            strip.show()

        pos = pos + 1

        if pos == numpixels:
            pos = (-1) * len(data[0])

        time.sleep(0.10)

if __name__ == "__main__":
    try:
        cycle()
    except SystemError:
        pass
