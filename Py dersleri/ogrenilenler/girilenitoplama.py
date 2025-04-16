toplam = 0
sayi1 = int(input("1. sayıyı giriniz: "))
sayi2 = int(input("2. sayıyı giriniz: "))

for i in range(sayi1, sayi2):
    toplam += i

print(f"{sayi1} ve {sayi2} arasındaki sayıların toplam değeri: {toplam}")
