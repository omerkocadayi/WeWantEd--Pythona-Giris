yiyecekler = [["elma", "armut"], ["portakal", "limon"], ["nohut", "barbunya"]]

for yiyecek in yiyecekler:
    for yiye in yiyecek:
        print (yiye)

print ("\n")


yiyecekler2 = [["elma", "armut"], ["portakal", "limon"], ["nohut", "barbunya"], 1]


for yiyecek in yiyecekler2:
    print (yiyecek)

print ("\n")

for i, yiyecek in enumerate(yiyecekler):
    for j, item in enumerate(yiyecek):
        print (item, i, j)