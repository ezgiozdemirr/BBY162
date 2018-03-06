#Alınan dersleri listeleyip, kodlarını sözlüğe ekledim. Ders adı yazılarak kod öğrenilebilir.

list = ["Bilginin Düzenlenmesi", "Programlama ve Algoritmalar", "Bilimsel İletişim", "Bilgi Erişim", "Bilgi Hizmetleri"]

dersler = {"Bilginin Düzenlenmesi": 152, "Programlama ve Algoritmalar": 162, "Bilimsel İletişim": 166, "Bilgi Erişim": 156, "Bilgi Hizmetleri": 154}

isim = input("Ders adı giriniz: ")

cevap = "{} dersinin kodu: {}"

print(cevap.format(isim,dersler[isim]))

