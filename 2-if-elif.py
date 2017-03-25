print('En iyi Yazılım Dili Hangisidir?')
cevap = input("Cevabınız : ")

if (cevap == 'python'):
    print('Tebrikler Kazandınız!')
else:
    print('Kaybettiniz!')

print("\n---------------------------------------\n")



sayi = int(input('Bir sayı yazınız : '))
if(sayi>0):
    mutlakdeger = sayi
else:
    mutlakdeger = -sayi     # abs(sayi)

print ("Sayının mutlak degeri = {}".format(mutlakdeger))

print("\n---------------------------------------\n")




sayi = int(input("Bir sayı giriniz : "))                   # Kullanıcıdan bir sayı girmesi isteniyor

if sayi > 0:                                             # Girilen sayı 0'dan büyük ise
    print("Sayı pozitiftir")

    if sayi % 2 == 0:                                    # Sayı 0'dan büyük ve çift olması durumu
        print("Sayı çifttir")
    else:                                                # Sayı 0'dan büyük ve tek olması durumu
        print("Sayı tektir")

elif sayi < 0:                                           # Girilen sayı 0'dan küçük ise
    print("Sayı negatiftir")

else:                           # Sayının 0 olma durumu (if ve elif durumlarının dışında kalan bütün durumlar)
    print("Sayı sıfırdır")