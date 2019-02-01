ls = list()
ls.append("gfhg")
ls.append("dfghj")
ls.append(5)
print(ls)
for i in ls:
    print(i)

ls.insert(2, "amanar")
ls.append("amanar")

ls.pop(0)

print(ls)
print("amanar" in ls)
print(ls.count("amanar"))  # count repait
