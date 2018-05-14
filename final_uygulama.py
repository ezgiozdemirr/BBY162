import tkinter
from random import choice
class Simon() :
    def __init__(self, master) :
        self.master = master
        self.master.minsize(240, 120)
        self.master.title("Simon&Simon")
        self.master.update()

        self.game_canvas = tkinter.Canvas(self.master, width = self.master.winfo_width(), height = self.master.winfo_height(), highlightthickness = 0)
        self.game_canvas.pack()

        self.ana_renkler = ("pink", "blue", "purple", "yellow")
        self.ara_renkler = ("#fc0086", "#b3b3fc", "#e157f9", "#fcfa97")
        self.mevcut_renkler = [color for color in self.ana_renkler]

        self.rectangle_ids = []

        self.dizi = [choice(self.ana_renkler)]
        self.dizi_sıklığı = 0

        self.draw_canvas()

        self.dizi_gösterim()

        self.master.mainloop()

    def dizi_gösterim(self) :
        self.flash(self.dizi[self.dizi_sıklığı])
        if(self.dizi_sıklığı < len(self.dizi) - 1) :
            self.dizi_sıklığı += 1
            self.master.after(1250, self.dizi_gösterim)
        else :
            self.dizi_sıklığı = 0

    def flash(self, color) :
        index = self.ana_renkler.index(color)
        if self.mevcut_renkler[index] == self.ana_renkler[index] :
            self.mevcut_renkler[index] = self.ara_renkler[index]
            self.master.after(1000, self.flash, color)
        else :
            self.mevcut_renkler[index] = self.ana_renkler[index]
        self.draw_canvas()

    def check_choice(self) :
        color = self.ana_renkler[self.rectangle_ids.index(self.game_canvas.find_withtag("current")[0])]
        if(color == self.dizi[self.dizi_sıklığı]) :
            if(self.dizi_sıklığı < len(self.dizi) - 1) :
                self.dizi_sıklığı += 1
            else :
                self.master.title("Simon Memory Game - Score: {}".format(len(self.dizi)))
                self.dizi.append(choice(self.ana_renkler))
                self.dizi_sıklığı = 0
                self.dizi_gösterim()
        else :
            self.master.title("Simon Memory Game - Game Over! | Final Score: {}".format(len(self.dizi)))
            self.dizi[:] = []
            self.dizi.append(choice(self.ana_renkler))
            self.dizi_sıklığı = 0
            self.dizi_gösterim()

    def draw_canvas(self) :
        self.rectangle_ids[:] = []
        self.game_canvas.delete("all")
        for index, color in enumerate(self.mevcut_renkler) :
            if index <= 1 :
                self.rectangle_ids.append(self.game_canvas.create_rectangle(index * self.master.winfo_width(), 0, self.master.winfo_width() / 2, self.master.winfo_height() / 2, fill = color, outline = color))
            else :
                self.rectangle_ids.append(self.game_canvas.create_rectangle((index - 2) * self.master.winfo_width(), self.master.winfo_height(), self.master.winfo_width() / 2, self.master.winfo_height() / 2, fill = color, outline = color))
        for id in self.rectangle_ids :
            self.game_canvas.tag_bind(id, '<ButtonPress-1>', lambda e : self.check_choice())

def main() :
    root = tkinter.Tk()
    gui = Simon(root)

if __name__ == "__main__" : main()