import math

# import clr
# from Autodesk.DesignScript.Geometry import *
#
# clr.AddReference("RevitNodes")
# clr.AddReference('ProtoGeometry')
#
# path_length = IN[0]

path_length = 87443.9715165015
PANEL = 3000


def func(pnl):
    x = path_length / pnl
    y = math.floor(x)
    z = x - y
    a = z * pnl
    b = y - 1
    c = b / a
    return c


out_val = None
while True:
    my_c = func(PANEL)
    if 10 <= my_c <= 30:
        out_val = my_c + PANEL
        break
    else:
        PANEL -= 10

OUT = out_val
print(OUT)
