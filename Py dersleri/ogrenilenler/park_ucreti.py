saatlik_ucret = 5
bes_saatten_fazlasi = 3
bir_bes_saat_arasi_saat_basina_fazladan_ucret = 4
kalinacak_saat = int(input("Kaç saat kalacaksınız?: "))
if kalinacak_saat == 1:
    print(f"{saatlik_ucret} TL ödemeniz gerekli")
elif kalinacak_saat > 1 and kalinacak_saat <= 5:
    ucret_hesap = (kalinacak_saat *
                   bir_bes_saat_arasi_saat_basina_fazladan_ucret)
    print(f"{ucret_hesap} TL ödemeniz gerekli")
elif kalinacak_saat > 5:
    bes_ucret = (kalinacak_saat * bes_saatten_fazlasi)
    print(bes_ucret)
