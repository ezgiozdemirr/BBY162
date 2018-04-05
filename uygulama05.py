import random
oyuncu = 3
i = 0
kitapAdı = random.choice(["Deliliğe Övgü", "Dalgalar", "Akıl Çağı", "Bulantılar", "Yabancı"])
kelimeler = []
print("Oyuna hoşgeldiniz!")
for kelime in kitapAdı:
    kelimeler.append("-")
print(kelimeler)

while oyuncu > 0:
    girilenHarf = input("Bir harf giriniz: ")

    if girilenHarf in kitapAdı:
        for check in kitapAdı:
            if kitapAdı [i] == girilenHarf:
                kelimeler [i] = girilenHarf
            i+=1
        print(kelimeler)
        print("Bir harf bildiniz!")
        i=0

    check = girilenHarf in kitapAdı
    if check == False:
        oyuncu-=1
    print("Kalan can: ", oyuncu)
    i=0

if oyuncu == 0:
    print("Oyunu kaybettiniz!")

