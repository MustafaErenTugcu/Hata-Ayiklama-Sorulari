import re

liste = ["1","2","5a","10b","abc","10","50"]

# 1 : Liste elemanlari icindeki sayisal degerleri bulunuz.
for i in liste:
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue
# 2 : Kullanici 'q' degerini girmedikce aldiginiz her inputun sayisal deger oldugundan emin olun aksi halde hata mesaji veriniz. 

while True:
    kullanici_Girdi = input("Cikmak icin q degerini diger turlu sayisal deger giriniz : ")
    if(kullanici_Girdi == "q"):
        break
    try:
        res = float(kullanici_Girdi)
        print("Girdiginiz Sayi : " , res)
    except ValueError: 
        print("gecersiz sayi")

# 3 : Girilen parola icinde turkce karakter hatasi veriniz 
parola = input("parola : ")
for i in parola:
    if i in ["utf-8"]:
        raise TypeError('Parola turkce karakter iceremez.')
    else:
        pass
print("gecerli parola")

# 4 - Faktoriyel fonksiyonu olusturup fonksiyona gelen deger icin hata mesajlari veriniz 

def faktoriyel(x):
    x = int(x)

    if x < 0 : 
        raise ValueError("Negatif Deger")
    
    resu = 1
    for i in range(1,x+1):
        resu *= i 
    return resu

for x in [5,10,20,-3,"10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as error:
        print(error)
        continue
    print(y)




