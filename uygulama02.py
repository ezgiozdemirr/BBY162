Toplamsaniye= input("Saniye Girin: ")
print ("yıl:",int(int(Toplamsaniye)/31104400))
a= int(Toplamsaniye)%31104400
print ("ay:",int(int(a)/2592000))
b = int(a)%2592000
print ("gün:",int(int(b)/86400))
c = int(b)%86400
print ("saat:",int(int(c)/3600))
d = int(c)%3600
print ("dakika:",int(int(d)/60))
e = int(d)%60
print ("saniye:",e)