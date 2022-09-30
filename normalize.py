from operator import contains

def normalize(key, value):
        if 'd' in key:  # distance
            return value / 128

        elif 'v' in key:  # velocity
            return value / 256

        elif 'a' in key:  # acceleration
            return value / 2048

        elif 'y' in key:  # yaw
            return value / 16384

        elif 'p' in key:  # probability
            return value / 128
