import random
import os
#from termcolor import colored
#os.system("color")
class Kart:
    def __init__(self,değer,renk):
        self.değer = değer
        self.renk = renk

    def __repr__(self):
        x, y = "", ""
        if self.değer == 14:
            x = "A"
        if self.değer == 2:
            x  = "2"
        if self.değer == 3:
            x = "3"
        if self.değer == 4:
            x = "4"
        if self.değer == 5:
            x = "5"
        if self.değer == 6:
            x = "6"
        if self.değer == 7:
            x = "7"     
        if self.değer == 8:
            x = "8"
        if self.değer == 9:
            x = "9"
        if self.değer == 10:
            x = "10"
        if self.değer == 11:
            x = "J"
        if self.değer == 12:
            x = "Q"
        if self.değer == 13:
            x = "K"
        if self.renk == 1:
            y = "Sinek"
        if self.renk == 2:
            y = "Maça"
        if self.renk == 3:
            y = "Karo"
        if self.renk == 4:
            y = "Kupa"
        text = y + " " + x
        if self.renk == 1 or 2:
            return y + " " + x
        elif self.renk == 3 or 4:
            return y + " " + x
class Deste(list):
    def __init__(self):
        list.__init__(self)
        değerler = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        renkler = [1,2,3,4]
        for değer in değerler:
            for renk in renkler:
                self.append(Kart(değer,renk))
    def kar(self):
        random.shuffle(self)
    
    def dağıt(self,kime):
        kime.kartlar.append(self.pop(0)) #�al��mad�?

