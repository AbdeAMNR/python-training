table = input("choose multiplacation table\n")
rang = input("choose table rang\n")
rang = int(rang)
i = 0
print("==============")
while (i < rang+1):
    res = i * int(table)
    print(str(table) + " * " + str(i) + " = " + str(res))
    i += 1
print("==============")
print("program finish")

