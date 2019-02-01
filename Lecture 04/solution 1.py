# ******************* Softwar engenering *******************
######################
# this function return the first occurant character in the string
# Exemple :
# ABCBEF ==> "B"
# ABCBAE ==> "A"
# ABCDEF ==> None
######################


def count(given_string):
    ls = {}
    for char in given_string:
        if char in ls.keys():
            return char
        ls[char] = 1
    return None


print(count("ABCBAE"))
