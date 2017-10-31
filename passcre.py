#!/usr/bin/python3
import random # random modülü

try :
    sayı = int(input("kaç haneli parola olsun >> "))
except (ValueError):
    print("!!! LÜTFEN SAYI GİRİNİZ !!!")
    input("DEVAM ETMEK İÇİN ENTER TUŞUNA BASIN")
    exit()

buyuhharf = input("büyük harf olsun mu?(E/H)")
kucukharf = input("küçük harf olsun mu?(E/H)")
sorusayı = input("sayı olsun mu?(E/H)")
nokta =input("noktalama olsun mu?(E/H)")

# büyük harfin koşulu
if (buyuhharf == "e" or buyuhharf == "E"):
    bh = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V","W", "X", "Y", "Z"]
else:
    bh = [""]

# küçük harfin koşulu
if (kucukharf == "e" or kucukharf == "E"):
    kh = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z"]
else:
    kh = [""]

# satı
if (sorusayı == "e" or sorusayı == "E"):
    sa = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
else:
    sa = [""]

# nokta
if (nokta == "e" or nokta == "E"):
    se = [".", ":", ";", "_", "-", "=", "+", ",", "/"]
else:
    se = [""]

Sifre = ""

while(True):
    t = len(Sifre)
    if sayı != t:
        r = random.randint(1,4)
        if r == 1: 
            Sifre += random.choice(bh)
        elif r == 2:
            Sifre += random.choice(kh)
        elif r == 3:
            Sifre += random.choice(sa)
        elif r == 4:
            Sifre += random.choice(se)
        else:
            continue
    elif sayı == t:
        print(Sifre)
        input("DEVAM ETMEK İÇİN ENTER TUŞUNA BASIN")
        exit()
    else:
        exit()
