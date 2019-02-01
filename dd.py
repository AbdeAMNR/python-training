# import clr
# from Autodesk.DesignScript.Geometry import *
#
# clr.AddReference("RevitNodes")
# clr.AddReference('ProtoGeometry')

# ila kant had la valeur entier rah ghatli3 lik error 7itach
# kan 9ssmo bla la parie decimal dialha bach nkhirjo c
path_length = 87443.9715165015
# path_length = IN[0]

# hadi Bohdha makatbdil
# la valeur dialha KAN passiwha f la fonction func()
PANEL = 3000  # 3000 mm


def func(pnl):
    x = path_length / pnl
    int_part = int(x)  # int_part ==> lfaraghat
    decimal_part = x - int(x)
    c = (int_part - 1) / (decimal_part * pnl)
    return c


my_OUT_value = None
while True:
    my_c = func(PANEL)
    if 10 <= my_c <= 30:
        my_OUT_value = my_c + PANEL
        break
    else:
        PANEL -= 10

OUT = my_OUT_value
print(OUT)
# voila jribt n3ti ldik IN[0] des nombre mkhtalfin okatrji3 li hadchi:
# IN[0]=200.2 ==> OUT=65.00000000000165
# IN[0]=40000.125 ==> OUT=322.6419753086425
