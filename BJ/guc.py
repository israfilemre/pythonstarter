def değerAl(el):
    değerler = []
    for kart in el:
        değerler.append(kart.değer)
    return sorted(değerler)
def renkAl(el):
    renkler = []
    for kart in el:
        renkler.append(kart.renk)
    return sorted(renkler)
def Sıralı(liste):
    return (len(set(liste)) == len(liste)) and (max(liste) - min(liste) == len(liste) -1) 
def Suited(liste):
    return len(set(liste)) == 1
        
def geç(el):
    değerler = değerAl(el)
    renkler = renkAl(el)

    #if len(set(el)) < len(el) or max(de�erler) > 14 or min(de�erler) < 1:
        #raise ValueError("am�nakoyum o kadar yazd�k")
    if Sıralı(değerler):
        if Suited(renkler):
            if max(değerler) == 1:
                return 23
            return 22
        return 18
    if Suited(renkler):
        return 19
    total = sum([değerler.count(x) for x in değerler])
    eller = {
        17: 21,
        13: 20,
        11: 17,
        9: 16,
        7: 15,
        5: sorted(değerler)[-1]
    }
    return eller[total]