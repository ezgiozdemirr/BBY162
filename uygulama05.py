import random

renkler = random.choice(['mavi', 'sarı', 'yeşil', 'kırmızı', 'pembe', 'mor', 'turuncu', 'kahverengi', 'siyah', 'beyaz', 'turkuaz'])
harfhavuzu = []
can = 10
oyuncizgileri = '_'

oyuncizgisayısı = list(oyuncizgileri * len(renkler))

dongu = 1

while dongu:
    print(' '.join(oyuncizgisayısı), end='\n\n')

    girilenharf = input('Bir harf giriniz: ').lower()

    try:
        int(girilenharf)
        print('Doğru bir şeyler girdiğinden emin ol.\n')
    except:
        if len(girilenharf) > 1:
            print('Harf giriniz!\n')
        else:
            if girilenharf in harfhavuzu:
                print('Bu harfi zaten girdiniz.\n')
            else:
                bulduk = None
                for i in range(len(renkler)):
                    if girilenharf == renkler[i]:
                        bulduk = True

                        oyuncizgisayısı[i] = girilenharf

                        harfhavuzu.append(girilenharf)

                        if oyuncizgileri not in oyuncizgisayısı:
                            print(' '.join(oyuncizgisayısı))
                            print('\nTebrikler kelimeyi buldunuz!')

                            dongu = 0

                else:

                    if bulduk != True:
                        can -= 1

                        print('Yanlış harf. Kalan hakkınız: {}\n'.format(can))

                        harfhavuzu.append(girilenharf)

                if can == 0:
                    print('Kaybettin. Doğru kelime "{}".\n'.format(renkler))

                    break