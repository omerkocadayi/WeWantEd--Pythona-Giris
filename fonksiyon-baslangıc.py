def kayit_olustur(isim, soyisim, issis, sehir):#sınırlı parametreler
    print("-" * 30)

    print("isim           : ", isim)
    print("soyisim        : ", soyisim)
    print("işletim sistemi: ", issis)
    print("şehir          : ", sehir)

    print("-" * 30)

    #geriye bi parametre dondurmediği icin none basar ekrana

print(kayit_olustur("mirac","kabatas","linux","istanbul"))

def kayit(**bilgiler):
    print("-" * 30)

    for anahtar, deger in bilgiler.items():
        print("{:<10}: {}".format(anahtar, deger))

    print("-" * 30)


print(kayit(ad="omer", soyad="kocadayi", şehir="İstanbul", tel="85454",sinif ="2",xcm=" ckmjv c"))
print(kayit(ad="mirac", soyad="kabatas", şehir="İstanbul", tel="85454"))