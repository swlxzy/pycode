i=0
# while(i<5):
#     print("Kodlama")
#     i=i+1
# print("")
# print("Döngü Sonu")

# i=0
# while (i<=20):
#     print(i)
#     i=i+2
# print("Döngü sonu")

# i = 0
# while(i<30):
#     islem = i= i+1
#     print(islem)

# i = 60  # 

# while i > 30:
#     if i % 2 == 0:  
#         print() 
#     i = i-1  

# i = 1 

# while i <= 12:
#     print(f"{i}. sınıf")  
#     i += 1  

# i = 0

# while i <= 100:
#     print(i)
#     i += 5 

# i = 1  
# toplama = 0  

# while i <= 20:
#     toplama += i  
#     i += 1 

# print("Toplam:", toplama)  



# sayi1 = int(input("1: sayıyı giriniz: "))
# sayi2 = int(input("2: sayıyı giriniz: "))


# total = 0


# while sayi1 <= sayi2:
#     total += sayi1  
#     sayi1 += 1  

# print("Toplam:", total)  


# sayi1 = int(input("Başlangıç sayısını girin: "))
# sayi2 = int(input("Bitiş sayısını girin: "))

# toplam = 0  
# adet = 0 


# while sayi1 <= sayi2:
#     toplam += sayi1  #
#     adet += 1 
#     sayi1 += 1  
# if adet > 0:
#     ortalama = toplam / adet
#     print("Ortalama:", ortalama)
# else:
#     print("sayı geçersiz")

# toplam=0
# sayi=1
# while (sayi!=0):
#     sayi=int(input("Bir sayı giriniz: "))
# toplam=toplam+sayi
# print(f"Sonuc=",toplam)

# toplam = 0
# adet = 0

# sayi = int(input("Bir sayı girin: "))

# while sayi != 1:
#     toplam += sayi
#     adet += 1
#     sayi = int(input("Bir sayı girin: "))

# if adet > 0:
#     ortalama = toplam / adet
#     print("Ortalama:", ortalama)
# else:
#     print("Hiç sayı girilmedi.")

# for i in range(0, 3):
#     for j in range(0, 3):
#         print([i, j])

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print("-" * 18)  # Her çarpım tablosundan sonra ayırıcı
