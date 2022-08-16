import os
import time
def cls():
    os.system("cls" if os.name=="nt" else "clear")
import adeste
import boyuncular
import guc
anadeste = adeste.Deste()
anadeste.kar()
def Oyun():
    cls()
    bet = int(input("Bahis Miktarı: "))
    if bet <= boyuncular.Emre.bakiye:
        ortakartlar = []
        boyuncular.Krupiyer.kartlar.append(anadeste.pop(0))
        boyuncular.Emre.kartlar.append(anadeste.pop(0))
        boyuncular.Krupiyer.kartlar.append(anadeste.pop(0))
        boyuncular.Emre.kartlar.append(anadeste.pop(0))
        anadeste.pop(0)
        ortakartlar.append(anadeste.pop(0))
        ortakartlar.append(anadeste.pop(0))
        ortakartlar.append(anadeste.pop(0))
        anadeste.pop(0)
        #ortakartlar.append(anadeste.pop(0))   
        anadeste.pop(0)
        #ortakartlar.append(anadeste.pop(0))

    

        cls()
        print(f"Kartlarınız: {boyuncular.Emre.kartlar}")
        print(f"Krupiyenin Kartları : {boyuncular.Krupiyer.kartlar}")
        print("*********************************\n*********************************")        
        print(f"Orta: {ortakartlar}")
        KrupiyerSon = boyuncular.Krupiyer.kartlar + ortakartlar
        EmreSon = boyuncular.Emre.kartlar + ortakartlar
        KrupiyerGüç = guc.güç(KrupiyerSon)
        EmreGüç = guc.güç(EmreSon)

        time.sleep(4)

        if EmreGüç < KrupiyerGüç:
                print("Kaybettiniz")
                boyuncular.Emre.bakiye -= bet
        elif EmreGüç > KrupiyerGüç:
                print("Kazandınız")
                boyuncular.Emre.bakiye += bet
        else:
                print("Berabere")
        print(EmreGüç)
        print(KrupiyerGüç)
        time.sleep(15)
        cls()
        if boyuncular.Emre.bakiye > 0:
                devam = int(input("1)Bir Oyun Daha\n2)Çıkış"))
                if devam == 1:
                    Oyun()
                elif devam == 2:
                    pass
        else:
                print("Yetersiz Bakiye Dolum Yapın!")
                time.sleep(3)
                cls()
    else:
        print(f"Yetersiz Bakiye, Bakiyeniz: {boyuncular.Emre.bakiye}")
        time.sleep(3)
        return Oyun()
Oyun()