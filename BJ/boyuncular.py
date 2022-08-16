class Oyuncu:
    def __init__(self,isim,bakiye=0):
        self.isim = isim
        self.bakiye = bakiye
        self.kartlar = []
    def __repr__(self):
        name = self.isim
        return name
    
Krupiyer = Oyuncu("Krupiyer")
Emre = Oyuncu("Emre",10)