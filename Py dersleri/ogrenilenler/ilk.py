def ortalama():
    not1 = int(input("1. sınav notu: "))
    not2 = int(input("2. sınav notu: "))
    ortalama_hesabi = (not1+not2)/2
    if ortalama_hesabi < 50:
        print("Dersten geçemedi")
    else:
        print("Dersten geçti")
    print(f"ortalama {ortalama_hesabi}")

ortalama()

print("")
print("")
print("")
print("Listeleme")

def listeleme():
    liste = ["Denizli", "Adana", "Sinop", "Niğde", "Anlatya"]
    print(liste)
    sec = liste.index("Adana")
    print(sec)
    liste.insert
    
listeleme()