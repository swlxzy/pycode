while True:  
    sifre = input("Lütfen 8 karakterlik bir şifre girin: ")  
    if len(sifre) == 8: 
        print("Şifreniz kaydedildi.") 
        break  
    else:  
        print("Şifreniz 8 karakter olmalıdır.")  
