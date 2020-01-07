import math

def get_speed(a,b,c):
    speed = a /((b/667)*c)
    return speed
print(get_speed(29.4,1000,4))