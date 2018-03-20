erkek=input("Erkek İsmi Giriniz..:")
kadın=input("Kadın İsmi Giriniz..:")
mısra=input("1 ve 7 Arasında Mısra Sayısı Giriniz..:")
sec=int(mısra)
boşluk=" "
bağlaç="ile"
mekan =["yolda","istasyonda","kafede","tiyatroda","markette","müzede","okulda","kulede"]
yüklem =["dans etti","bekledi","sarhoş oldu","oynadı","çalıştı","koştu","evlendi","gülümsedi","sarıldı","geziye çıktıUmU"]

import random
def kelime2():
    secim = random.choice(mekan)
    mekan.remove(secim)
    return secim
def kelime3():
    secim = random.choice(yüklem)
    yüklem.remove(secim)
    return secim


a=(erkek+boşluk+kelime2()+boşluk+kadın+boşluk+bağlaç+boşluk+kelime3()+"\n")
b=(erkek+boşluk+kelime2()+boşluk+kadın+boşluk+bağlaç+boşluk+kelime3()+"\n")
c=(erkek+boşluk+kelime2()+boşluk+kadın+boşluk+bağlaç+boşluk+kelime3()+"\n")
d=(erkek+boşluk+kelime2()+boşluk+kadın+boşluk+bağlaç+boşluk+kelime3()+"\n")
e=("\n")
f=(erkek+boşluk+kelime2()+boşluk+kadın+boşluk+bağlaç+boşluk+kelime3()+"\n")
g=(erkek+boşluk+kelime2()+boşluk+kadın+boşluk+bağlaç+boşluk+kelime3()+"\n")
h=(erkek+boşluk+kelime2()+boşluk+kadın+boşluk+bağlaç+boşluk+kelime3()+"\n")



while True:
    if sec==1:
        print(e,a)
        print

    elif sec==2:
        print(e,a,b)
        print

    elif sec==3:
        print(e,a,b,c)
        print

    elif sec==4:
        print(e,a,b,c,d)
        print

    elif sec==5:
        print(e,a,b,c,d,e,f)
        print

    elif sec==6:
        print(e,a,b,c,d,e,f,g)
        print

    elif sec==7:
        print(e,a,b,c,d,e,f,g,h)
        print

    else:
        print("Yanlış mısra sayısı girdiniz.")
    break