import random # random modülü
bh = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
kh = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nu = ["1","2","3","4","5","6","7","8","9","0"]
se = [".",":",";","_","-","=","+",",","/"]
Sifre = ""
sayı = int(input("kaç haneli şifre olsun >> "))
while(True):
    t = len(Sifre) # sifre karakter sayısını t deyişkenine adıyor 
    if sayı != t: # sayı deyişkeni t eşit deyilse devam et
        r = random.randint(1,4) # burda 1,4 kadar bir sayı belirler karekter sıralaması yapar
        if r == 1: # 1,4 kadar sayıda 1 geldiyse büyük harf karakteri gelir
            ibh = random.choice(bh) # random.choice(lsite)= listeden bir karakter seçer
            Sifre += ibh # ibh deyişkenini karakteri Sifre karakterine verir
        elif r == 2:
            ikh = random.choice(kh)
            Sifre += ikh
        elif r == 3:
            inu = random.choice(nu)
            Sifre += inu
        elif r == 4:
            ise = random.choice(se)
            Sifre += ise
        else:
            continue
    elif sayı == t:
        print(Sifre)
        pause = input("DEVAM ETMEK İÇİN ENTER TUŞUNA BASIN")
        exit()
    else:
        exit()
