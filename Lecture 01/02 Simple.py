# myString = "hi everybody! how are you"
# lenght = int(len(myString))
# print(str(lenght) + "\n")
# i, o = 0, 0
# for i in range(0, lenght):
#    if (myString[i] == "e"):
#     o += 1
# print(str(o))

# ===================================================
# add start between letters (B*o*n*j*o*u*r*)
myStr = input("inter a text to decorate\n")
a = ""
i = 0
for i in range(len(myStr)):
    a += myStr[i] + "*"
    if i == len(myStr) - 1:
        a = a[: len(a) - 1]
print(a)
