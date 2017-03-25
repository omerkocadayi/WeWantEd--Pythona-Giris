# in kelimesi İngilizcede ‘içinde’ anlamına geliyor.
# Dolayısıyla for falanca in filanca
# yazdığımızda aslında şöyle bir şey demiş oluyoruz:
# filanca içinde falanca adını verdiğimiz herbir öğe için...

cumle = "We wanted Python"

for harf in cumle:
    print (harf)

print("\n---------------------------------------\n")

for i in range(0,10,2):                             # EKSİLTMEYİ DE GOSTER     range(10,0,-1)
    print (i)

print("\n---------------------------------------\n")


i=1
for x in range(1, 11):
    for y in range(1, 11):
        print("{} x {} = {}\t" .format(x, y, x * y))

    print("\n")

print("\n---------------------------------------\n")

# ASAL SAYI BULMA

sayi = int(input('Bir sayi giriniz : '))
bolundu = 0
for i in range(2,(sayi+1)//2):
    if sayi%i == 0:
        print ("Girdiginiz sayi asal degildir !!")
        bolundu += 1
        break

if(bolundu == 0):
    print ("Bu sayi asaldir !!")


print("\n---------------------------------------\n")

# ILK N ADET FIBONACCI SAYISINI YAZDIRMA

sayi = int(input('Bir sayi giriniz : '))
print("Fibonacci sayi dizisinin ilk {} sayisi" .format(sayi))

a, b = 1, 1
print (a)
print (b)
for i in range(2,sayi):
    a, b = b, a+b
    print (b)
    i += 1

print("\n---------------------------------------\n")