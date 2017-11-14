import random # random modülü
import os # os modülü tanımlandı
import APTEM

sbh = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V","W", "X", "Y", "Z"]
skh = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
ssa = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
sse = [".", ":", ";", "_", "-", "=", "+", ",", "/"]
def pass1():
	try :
		sayı = int(input("kaç haneli parola olsun >> "))
	except (ValueError):
		print("!!! LÜTFEN SAYI GİRİNİZ !!!")
		APTEM.kapat()
		exit()

	buyuhharf = input("büyük harf olsun mu?(E/H)")
	kucukharf = input("küçük harf olsun mu?(E/H)")
	sorusayı = input("sayı olsun mu?(E/H)")
	nokta =input("noktalama olsun mu?(E/H)")

	# büyük harfin koşulu
	if (buyuhharf == "e" or buyuhharf == "E"):
		bh = sbh
	else:
		bh = [""]

	# küçük harfin koşulu
	if (kucukharf == "e" or kucukharf == "E"):
		kh = skh
	else:
		kh = [""]

	# satı
	if (sorusayı == "e" or sorusayı == "E"):
		sa = ssa
	else:
		sa = [""]

	# nokta
	if (nokta == "e" or nokta == "E"):
		se = sse
	else:
		se = [""]

	Sifre = ""

	name = os.name
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
			APTEM.clear()
			print(Sifre)
			APTEM.kapat()
			exit()
		else:
			exit()

def pass2():

	
	parola = input("parolayı girin >> ")
	puan = 0 
	parolal = [] # parolayı listeye cevirmek işin kullanılıyor
	for i in parola:
		parolal.append(i) 
	
	puan = int(len(parola)/3) # parolanın karakter sayısını 3 bölüm tam sayıya çeviriyoruz
	
	x = 0
	while (x != 26) :
		sru = sbh[x]
		dey = parolal.count(sru)
		if (dey == 1):
			puan = puan + 1
		x += 1
	x = 0	
	while (x != 26) :
		sru = kh[x]
		dey = parolal.count(sru)
		if (dey == 1):
			puan = puan + 1
		x += 1
	x = 0
	while (x != 10) :
		sru = bh[x]
		dey = parolal.count(sru)
		if (dey == 1):
			puan = puan + 1
		x += 1
	x = 0
	while (x != 10) :
		sru = bh[x]
		dey = parolal.count(sru)
		if (dey == 1):
			puan = puan + 1
		x += 1
	print(puan)