toplam = 0
# 0-10 arası sayılar toplanacağı için range değeri 11 olarak verilmiştir
for sayilar in range(11):
    # sayilar (range 11) ve toplam (0) burada toplanıyor
    toplama = toplam+sayilar
    print(toplama)  # sonuç
else:
    print("döngü bitti")
