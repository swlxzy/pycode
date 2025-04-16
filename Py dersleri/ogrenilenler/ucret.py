sinir = 20
bagaj_kilo = float(input("bagaj kilosu: "))
fazla_kilo_basina_ucret = 10
if bagaj_kilo<=20:
    print("Herhangi bir ücret ödemenize gerek yok")
else:
    fazla_kilo = bagaj_kilo - sinir
    ucret = fazla_kilo * fazla_kilo_basina_ucret
    print(f"Fazladan {ucret} ödemeniz gerekli")