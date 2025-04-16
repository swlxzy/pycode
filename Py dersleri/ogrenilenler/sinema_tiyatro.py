sinema_bilet_fiyati = 15
tiyatro_bilet_fiyati = 10

tercih = input("Sinema mı? Tiyatro mu?: ")
ogrenci_mi = input("Öğrenci misiniz? (E/H): ")

if tercih == "Sinema":
    if ogrenci_mi == "E":
        print("Ödemeniz gereken:", sinema_bilet_fiyati / 2, "TL")
    else:
        print("Ödemeniz gereken:", sinema_bilet_fiyati, "TL")
elif tercih == "Tiyatro":
    if ogrenci_mi == "E":
        print("Ödemeniz gereken:", tiyatro_bilet_fiyati / 2, "TL")
    else:
        print("Ödemeniz gereken:", tiyatro_bilet_fiyati, "TL")
else:
    ("Geçersiz seçenek girdiniz")
