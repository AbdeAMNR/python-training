try:
    ls = list(range(1, 5))
    print(ls[5])
except Exception as err:
    print("index out of range bitch", err)
