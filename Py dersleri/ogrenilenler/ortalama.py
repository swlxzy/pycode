sinav1 = int(input("1. Sınav notunu giriniz:"))
sinav2 = int(input("2. Sınav notunu giriniz:"))
performans = int(input("performans notu giriniz: "))
ortalama = sinav1+sinav2+performans/3
if ortalama<50:
    print("Başarısız")
else:
    print("Başarılı")
print(f"Ortalama: {ortalama}")