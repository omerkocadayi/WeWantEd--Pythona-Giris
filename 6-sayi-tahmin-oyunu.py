import random
sayi = random.randint(1,100)
print ("Tahmin Oyununa Hos Geldiniz")
sayac=0

while True:
    tahmin = int(input("Sayi Girin:"))
    sayac += 1
    
    if tahmin == sayi:
        print ("\nTebrikler {} denemede bildiniz!" .format(sayac))
        break

    elif tahmin < sayi:
        print ("Daha Buyuk Bir Sayi Girin")

    else:
        print ("Daha Kucuk Bir Sayi Girin")
