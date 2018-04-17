from tkinter import Tk, Label, Button

class Books:
    def __init__(self, anaSayfa):
        self.anaSayfa = anaSayfa
        anaSayfa.title("Quote")

        list= ("sasdfdd", "dfggfffgg", "erttredd", "sryryryr", "qwerhyhy")

        self.etiket = Label(anaSayfa, text="Bir kitap seçiniz!")
        self.etiket.pack()

        self.kitapAdı = Button(anaSayfa, text="Bulantı", command=self.yazdir)
        self.kitapAdı.pack()

        self.kitapAdı2 = Button(anaSayfa, text="Akıl Çağı", command=self.yazdir)
        self.kitapAdı2.pack()

        self.kitapAdı3 = Button(anaSayfa, text="Deliliğe Övgü", command=self.yazdir)
        self.kitapAdı3.pack()

        self.kitapAdı4 = Button(anaSayfa, text="Sana Gül Bahçesi Vadetmedim", command=self.yazdir)
        self.kitapAdı4.pack()

        self.kitapAdı5 = Button(anaSayfa, text="Şeker Portakalı", command=self.yazdir)
        self.kitapAdı5.pack()

        self.kapatButonu = Button(anaSayfa, text="Kapat", command=anaSayfa.quit)
        self.kapatButonu.pack()

    def yazdir(self):
        if list in kitapAdı:
            print (0)







root = Tk()
kitaplar = Books(root)
root.mainloop()
