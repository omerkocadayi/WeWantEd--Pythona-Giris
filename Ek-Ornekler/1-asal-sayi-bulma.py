# ASAL SAYI BULMA

sayi = int(input('Bir sayi giriniz : '))
bolundu = 0

for i in range(2, (sayi//2):
# Bir sayinin yarısından daha buyuk bir boleni olmayacagi icin, programin daha hizli calismasi acisindan sayi//2'ye kadar dondurduk.
    if sayi%i == 0:
        print ("Girdiginiz sayi asal degildir !!")
        bolundu += 1
        break

if (bolundu == 0):
    print ("Bu sayi asaldir !!")
