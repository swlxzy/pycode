def yildiz_ucgen_ciz(SatirSayisi):
    print(f"{SatirSayisi} satırlık yıldız üçgen çiziliyor:")
    for satir in range(1, SatirSayisi + 1):
        print("*" * satir)

def aynali_ucgen_ciz(SatirSayisi):
    print(f"{SatirSayisi} satırlık aynalı yıldız üçgen çiziliyor:")
    for satir in range(1, SatirSayisi + 1):
        print(" " * (SatirSayisi - satir) + "*" * satir)

# Fonksiyonları çağırma
yildiz_ucgen_ciz(9)  
aynali_ucgen_ciz(9)  
