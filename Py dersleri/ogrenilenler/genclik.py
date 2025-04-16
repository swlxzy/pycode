dogum_yili = int(input("Doğum yılınızı giriniz: "))
yas = 2025-dogum_yili
if yas >= 0 and yas < 17:
    print("Çocuk")
elif yas >= 18 and yas < 65:
    print("Genç")
elif yas >= 66 and yas < 79:
    print("Orta  Yaşlı")
elif yas >= 80:
    print("Yaşlı")
else:
    print("Yanlış değer girdiniz")
