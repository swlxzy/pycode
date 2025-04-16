sayi1 = int(input("1. sayıyı giriniz: "))
sayi2 = int(input("2. sayıyı giriniz: "))
islem = input("İşlem seçin (+,-,*,/): ")
if islem == "+":
    sonuc = (sayi1+sayi2)
    print(sonuc)
elif islem == "-":
    sonuc = (sayi1-sayi2)
    print(sonuc)
elif islem == "*":
    sonuc = (sayi1*sayi2)
    print(sonuc)
elif islem == "/":
    sonuc = (sayi1/sayi2)
    print(sonuc)
else:
    print("Yanlış işlem girdiniz")
