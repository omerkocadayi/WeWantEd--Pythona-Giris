import sys

sayı = input('Bir sayı girin: ')

if int(sayı) < 0:
    print('çıkılıyor...')
    sys.exit()

else:
    print(sayı)

print(sys.argv) # programda kullanılan parametreleri liste olarak sunar listenin ilk elemanı programın adı

# sys.platform #hangi platformda oldugu
# 'linux'

# sys.executable #hangi dizinde calıstırıldıgı
# '/usr/bin/python3.5'

# sys.prefix # pythonun hangi dizine kurulduğu

# konsol
# import sys
# >>> sys.stdin.read()
# omer
# 'omer\n'

# sys.stdin.readline()
# omer kocadayi
# 'omer kocadayi\n'