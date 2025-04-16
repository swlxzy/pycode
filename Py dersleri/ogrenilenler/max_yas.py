yas = int(input("Yaşınızı girin: "))
if yas < 40:
    mezunuyet = input("Üniversite mezunu musunuz?(E/H): ")
    surucu_belgesi = input("Sürücü belgeniz var mı? (E/H):")
    if mezunuyet == "E" and surucu_belgesi == "E":
        print("Tebrikler İşe alındınız")
    else:
        print("İşe alınmadınız")
else:
    print("Kriterleriniz uymuyor")
