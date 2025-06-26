list_3 = [1, 2, 3, 4]

for i in list_3 :
    print("isi array", i)

print("------------------------------------------------")

list_x = [4, 6, 7, 8]

for y in range(len(list_x)) :
    print("isi array of list_x", list_x[y])

print("isi array of list_x in 3", list_x[2])

print("------------------------------------------------")

list_1 = [70, 30, 20]

for i, v in enumerate(list_1):
    print("index:", i, "elem:", v)



print("------------------------------------------------")

matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 56, 1, 0],
]

for row in matrix:
    for cel in row:
        print(cel, end=" ")
    print()

    for j, l in enumerate(matrix):
        print("index:", j, "elemen:", l)

print("angka_matrix:", matrix[3][2])

print("------------------------------------------------")

matrix_1 = [
    [5, 6, 7, 8],
    [2, 3, 0, 9]
]

print("array:", matrix_1[1][:2])

print("------------------------------------------------")

range_1 = range(0, 10)
list_2 = list(range_1)
print(list_2)

list_2.remove(6)
print("array;", list_2 )

list_2[4] = 10
print(list_2)

print("------------------------------------------------")

tupple = (1,2,3)
list_converter = list(tupple)
print(list_converter)

print("------------------------------------------------")