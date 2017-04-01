
def kelimeSay(string):

    count = 0

    for i in range(len(string)):
        if string[i]== ' ':
            count += 1

    return count


string = input("bir cumle giriniz")

print("Cümledeki kelime sayısı : {} ".format(kelimeSay(string)+1))
