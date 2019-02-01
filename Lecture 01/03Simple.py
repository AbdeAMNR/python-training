# EX1..Q1
def serieWithWhile(n):
    u, i = 2, 1
    while i <= n:
        u = 3 * u - 1
        i += 1
    return u


def serie():
    i = input('kjojdf')
    i += 2
    return str(i)


# EX1..Q2
def serieWithFor(n):
    u, i = 2, 1
    for i in range(1, n + 1):
        u = 3 * u - 1
        i += 1
    return u


# EX1..Q3
def nPremiersTermes(nPremiers):
    myList = []
    U = 2
    i = 1
    myList.append(U)
    while i <= nPremiers:
        U = 3 * U - 1
        i += 1
        myList.append(U)
    return myList


# EX1..Q4
def calcIndice(m):
    myList = []
    U = 2
    i = 1
    myList.append(U)
    while True:
        U = 3 * U - 1
        i += 1
        if U >= m:
            return myList
        myList.append(U)


# EX2..Q1

# func Execution Test
# print(serie())
print("kjesf", )
