import pandas as pd

df = pd.read_excel("data_korelasi.xlsx")  

print(df.head())

x = df["Jam Belajar (X)"]
y = df["Nilai Ujian (Y)"]

for nilai_x in x:
    print("x :", nilai_x)

total_x = 0
count_x = 0

for elment_x in x:
    total_x += elment_x
    count_x += 1

print("total x :", total_x)
print("count_x :", count_x)

print("===================================================================================")

for nilai_y in y:
    print("y :", nilai_y)

total_y = 0
count_y = 0

for element_y in y:
    total_y += element_y
    count_y += 1

print("total y :", total_y)
print("count_y :", count_y)


print("===================================================================================")

mean_x = (total_x / count_x)
mean_y = (total_y / count_y)
print(mean_x)
print(mean_y)


print("===================================================================================")

for angka_x, angka_y in zip(x, y):    
    angka_x = float(angka_x)
    angka_y = float(angka_y)
    x_y = angka_x * angka_y
    print("xy :", x_y)

hasil_xy = []

for angka_x, angka_y in zip(x, y):    
    angka_x = float(angka_x)
    angka_y = float(angka_y)
    x_y = angka_x * angka_y
    hasil_xy.append(x_y)


xy = [
    
      22.5, 48.0, 75.0, 
      104.0, 135.0, 168.0, 203.0, 240.0, 
      283.5, 325.0, 368.5, 420.0, 461.5, 511.0, 555.0, 608.0, 663.0, 711.0, 760.0, 820.0,
      871.5, 924.0, 977.5, 1032.0, 1087.5, 1144.0, 1188.0, 1246.0, 1305.0, 1365.0, 1410.5, 1472.0, 1534.5, 1581.0, 
      1645.0, 1692.0, 1757.5, 1805.0, 1872.0, 1920.0, 1968.0, 2037.0, 2085.5, 2156.0, 2205.0, 2254.0, 2326.5, 2376.0, 2450.0, 2500.0
      
      ]

total_xy = 0


for element_xy in xy:
    total_xy += element_xy

print("sigma xy:", total_xy)
    
print("===================================================================================")

for angka_x, angka_x in zip(x, x):    
    angka_x = float(angka_x)
    angka_x = float(angka_x)
    x_x = angka_x * angka_x
    print("xx :", x_x)

hasil_xx = []

for angka_x, angka_y in zip(x, x):    
    angka_x = float(angka_x)
    angka_x = float(angka_x)
    x_x = angka_x * angka_x
    hasil_xx.append(x_x)

xx = (hasil_xx)

total_xx = 0


for element_xx in xx:
    total_xx += element_xx

print("sigma xx:", total_xx)


print("===================================================================================")

for angka_y, angka_y in zip(y, y):    
    angka_y = float(angka_y)
    angka_y = float(angka_y)
    y_y = angka_y * angka_y
    print("yy :", y_y)

hasil_yy = []

for angka_y, angka_y in zip(y, y):    
    angka_y = float(angka_y)
    angka_y = float(angka_y)
    y_y = angka_y * angka_y
    hasil_yy.append(y_y)

yy = (hasil_yy)

total_yy = 0


for element_yy in yy:
    total_yy += element_yy

print("sigma yy:", total_yy)

print("===================================================================================")


I = [(50 * total_xy) - (total_x * total_y)]

L = [((50 * total_xx) - (total_x * total_x)) * ((50 * total_yy) - (total_y * total_y))]

import math

nilai_i = 274212.5

angka = 82779505156.25
akar_kuadrat = math.sqrt(angka)

r = nilai_i / akar_kuadrat

print("nilai r :", r)

print("===================================================================================")

lr = ((50 * total_xx) - (total_x * total_x))

b = 274212.5 / 130156.25

print("nilai b :", b)






