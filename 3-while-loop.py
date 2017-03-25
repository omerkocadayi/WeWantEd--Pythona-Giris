counter = 0
while counter < 5:
   print ("%s is  less than 5" % counter)
   counter = counter + 1

print ("{} is not less than 5" .format(counter))


print("\n---------------------------------------\n")


print ("Karekok bulucu")

secim = 'e'
while (secim == 'e'):
    sayi = int(input("Bir Sayını giriniz : "))
    sayi = float(sayi)
    print("Girdiğiniz sayının karekökü : {}".format(sayi ** (1/2)))        # sqrt(sayi)

    secim = input("\nDevam etmek icin 'e' , cıkmak icin herhangi bir tusa bas : ")

print("*** Cıkıs Yapıldı ***")



print("\n---------------------------------------\n")

while True:
    parola = input("parola belirleyin: ")

    if not parola:
        print("parola bölümü boş geçilemez!")

    elif len(parola) in range(3, 8):
        print("Yeni parolanız", parola)
        break

    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")