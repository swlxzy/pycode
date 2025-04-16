ad = input("Ad: ")
soyad = input("Soyad: ")
yas = int(input("Yaş: "))
yabanci_dil = input("Bildiğiniz yabancı Dil: ")
if ((yabanci_dil=="İngilizce" or yabanci_dil=="Fransızca") and yas<40):
    print(f"Sayın {ad} {soyad}, sonuç başarılı")
else:
    print(f"Sayın {ad} {soyad},Sonuç başarısız")
    