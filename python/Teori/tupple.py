tupple = (1, "ryjunix", 4, 5, "solotre")
print(tupple)

tupple_1 = (1, 6, 7, 8)

for i in (tupple):
    print("array;", i)

print("------------------------------------------")

for i in range(0, len(tupple)):
    print("tuple:", tupple[i])


n = "solotre"
if n in tupple_1:
    print(n, "ada di tupple")
else:
    print("tidak ada", n, "di tupple")