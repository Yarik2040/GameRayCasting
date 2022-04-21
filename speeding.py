from settings import *


def calculate_N(rpm):
    return max(-(((rpm - 5500) ** 2) / 500) + 51000, 0)


def speeding(speed, mode, rpm):
    N = calculate_N(rpm)
    if speed < SPEED_DATA[mode]:
        boost = (SPEEDING_DATA[mode] / 51000) * N
        return boost
    return 0


def reverse_speeding(speed, rpm):
    N = calculate_N(rpm)
    boost = (SPEEDING_DATA[0] / 51000) * N
    return abs(boost)



def stopping(speed):
    return -speed / 100
