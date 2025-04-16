def topla(a, b):
    a + b

def cikar(a, b):
    a - b

def carp(a, b):
    a * b

def bol(a, b):
    a/b

islem = input("işlem seçiniz(-, +, *, /): ")

sayi1 = float(input("1. sayı: "))
sayi2 = float(input("2. sayı: "))

if islem=="+":
    print(sayi1+sayi2)

if islem=="-":
    print(sayi1-sayi2)

if islem=="*":
    print(sayi1*sayi2)

if islem=="/":
    print(sayi1/sayi2)


