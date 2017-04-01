from fonksiyondalambda import *

giriş = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) üs hesapla
(6) kök hesapla
(7) mod
"""
print(giriş)

while True:
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q) : ")

    if soru == "q":
        print("çıkılıyor...")
        break

    elif soru == "1":
        sayi1 = int(input("Toplama işlemi için ilk sayıyı girin : "))
        sayi2 = int(input("Toplama işlemi için ikinci sayıyı girin : "))
        print("{} + {} = {}".format(sayi1,sayi2,topla(sayi1,sayi2)))

    elif soru == "2":
        sayi1 = int(input("Çıkarma işlemi için ilk sayıyı girin : "))
        sayi2 = int(input("Çıkarma işlemi için ikinci sayıyı girin : "))
        print("{} - {} = {}".format(sayi1, sayi2, cikar(sayi1, sayi2)))

    elif soru == "3":
        sayi1 = int(input("Çarpma işlemi için ilk sayıyı girin : "))
        sayi2 = int(input("Çarpma işlemi için ikinci sayıyı girin : "))
        print("{} x {} = {}".format(sayi1, sayi2, carp(sayi1, sayi2)))

    elif soru == "4":
        sayi1 = int(input("Bölme işlemi için ilk sayıyı girin : "))
        sayi2 = int(input("Bölme işlemi için ikinci sayıyı girin : "))
        print("{} / {} = {}".format(sayi1, sayi2, bol(sayi1, sayi2)))

    elif soru == "5":
        sayi = int(input("Üssünü hesaplamak istediğiniz sayıyı girin : "))
        us = int(input("Hesaplanacak üs girinzi : "))
        print("{} sayısının {} üssü = {}".format(sayi, us, usAl(sayi, us)))

    elif soru == "6":
        sayi = int(input("Kökünü hesaplamak istediğiniz sayıyı girin: "))
        kok = int(input("kökü giriniz : "))
        print("{} sayısının kök {} i = {}".format(sayi, kok, kokAl(sayi, kok)))

    elif soru == "7":
        sayi1 = int(input("Modunu hesaplamak istediğiniz sayıyı girin: "))
        mod = int(input("Kaça göre mod : "))
        print("{} + {} = ".format(sayi1, sayi2, topla(sayi1, sayi2)))

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz :", giriş)