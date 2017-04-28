import sys


print(sys.stdout)

standartoutputtut=sys.stdout

with open("deneme.txt","w+") as dosya:
    sys.stdout=dosya

    print("we wanted python kursu", flush=True)
    print("karabuk universitesi")


#sys.stdout= standartoutputtut
#print("safranbolu")

#çıktılar = open('çıktılar.txt', 'w')
#hatalar = open('hatalar.txt', 'w')
#sys.stdout = çıktılar
#sys.stderr = hatalar

#print('normal çıktı')
#print('hata mesajı: ', 1/0)