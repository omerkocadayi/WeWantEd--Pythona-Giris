bilgi = """

# Dosya olusturma

1) olusacak-dosya-ismi = open(dosya_adı, kip)
   dosya = open("sinavsonuclarim.txt", "w")

2) olusacak-dosya-ismi = open(dosya dizini, kip)
   dosya = open("C:\okul\dersler\sinavsonuclarim.txt", "w")


----------------------------


Dosyaya yazma

dosya.write("A dersi : 90")


----------------------------


# Dosyayi okuma

dosya = open("sinavsonuclarim.txt", "r")
dosya = open("sinavsonuclarim.txt")

print(dosya.read())
print(dosya.readline())
print(dosya.readlines())


----------------------------


# Dosyayi kapatma

dosya.close()
close(dosya)
with open("sinavsonuclarim.txt", "r") as dosya:


----------------------------


Dosyayi ileri geri sarma

dosya.seek(0)
dosya.seek(10)
dosya.tell()


----------------------------


# Dosyanin sonunda degisiklik yapma

with open("sinavsonuclarim.txt", "a") as dosya:
dosya.write("B dersi : 80")



# Dosyanin basinda degisiklik yapma

with open("fihrist.txt", "r+") as f:
veri = dosya.read()
dosya.seek(0) #Dosyayı başa sarıyoruz
dosya.write("C dersi : 85"+veri)          // veri = dosya.read() -> yapmazsak ne olur ?


# Dosyanin ortasinda degisiklik yapma

with open("sinavsonuclarim.txt", "r+") as dosya:
veri = dosya.readlines()
veri.insert(2, "D dersi : 60")
dosya.seek(0)
dosya.writelines(veri)


----------------------------


# Dosya metotlari

dosya.closed              // dosya kapaliysa TRUE, açıksa FALSE deger dondurur.
dosya.readable()          // dosya okunabilir açıldıysa TRUE, okunabilir açılmadıysa FALSE deger dondurur.
dosya.writable            // dosya yazılabilir ozellikteyse TRUE, degilse FALSE deger dondurur.

 with open("sinavsonuclarim.txt", "r+") as dosya:
 dosya.truncate()          // tum dosyayi siler.
 dosya.truncate(10)        // ilk 10 bayti tutar. geri kalani siler.



# DOSYANIN ISTENEN KISIMLARINI NASIL KIRPABILIRIZ ??


with open("sinavsonuclarim.txt", "r+") as dosya:
dosya.readline()
dosya.seek(dosya.tell())
dosya.truncate()


# truncate'in anlami 'kirpmak' olsa da, bu metotla dosyalarin boyutunu artirmak da mumkun.
# elimizde 1 kilobaytlik bir dosyanin var oldugunu dusunelim.
# dosya.truncate(1024*3)     // dosyanin boyutunu bu sekilde 3 kilobayta cikarmis olduk.


dosya.mode                 // bu nitelik dosyanin hangi kipte acildigini soyler.
dosya.name                 // bu nitelik txt dosyasinin ismini gosterir.
dosya.encoding             // bu nitelik dosyamizin hangi dil kodlamasi ile kodlandigini soyler.

"""
