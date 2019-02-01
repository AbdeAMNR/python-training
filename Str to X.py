

def str_to_x(my_chaine, symbol):
    s = ""
    for i in my_chaine:
        if i.__eq__(" "):
            s += " "
        s += symbol
    return s


chaine = "BEN SAID"
print(str_to_x(chaine, "X"))
