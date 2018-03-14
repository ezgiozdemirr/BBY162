erkekadı = input("Bir erkek ismi giriniz: ")
kadınadı = input("Bir kadın ismi giriniz: ")
dize= int(input("Dize sayısı giriniz: "))



sarkı = [erkekadı + " " "olmak da ayıp değil" " " + kadınadı + " " "olmak da", "Hatta sevda yüzünden ölmek de ayıp değil" , "Bütün iş" " " + erkekadı + " " "ile" " " + kadınadı + " " "olabilmekte yani yürekte", "Mesela bir barikatta dövüşerek" " " + erkekadı , "Mesela Kuzey Kutbunu keşfe giderken" " " + kadınadı , "Mesela denerken damarlarında bir serumu ölmek ayıp olur mu?" , erkekadı + " " "olmak da ayıp değil" " " + kadınadı + " " "olmak da","Hatta sevda yüzünden ölmek de ayıp değil!"]

for olusturulacak_sarkı in sarkı[:dize]:
    print(olusturulacak_sarkı)

if dize > 8:
    print ("Maksimum 8 dize yazılır...")

