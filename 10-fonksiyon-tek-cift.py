print("Tek mi? Çift mi? Fonksiyonu\n\n")

def kontrolEt(sayi):
    if(sayi%2==0):
        print("sayi çifttir")

    else:
        print("sayi tektir")

sayi=int(input("bir sayi giriniz"))

kontrolEt(sayi)