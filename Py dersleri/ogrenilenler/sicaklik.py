sicaklik = int(input("Sıcaklık değeri giriniz: "))
if sicaklik <= 5:
    print("Soğuk")
elif sicaklik >= 6 and sicaklik <= 14:
    print("Ilık")
elif sicaklik >= 15:
    print("Sıcak")
