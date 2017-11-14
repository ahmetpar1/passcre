"""
modül yapımcı:
    AHMET PARMAKSIZOĞLU
modül açıklama
    basitleştirmek modül 
"""
import os # os modül dahil ettik

def pause(): # pause fonksiyom
    input("DEVAM ETMEK İÇİN ENTER TUŞUNA BASIN")
	
def kapat():
	input("KAPATMAK İÇİN ENTER TUŞUNA BASIN")

def clear(): # clear fonksiyon
	osn = os.name
	if (osn == "nt") :
		os.system("cls")
	elif (ons == "posix") :
		os.system("clear")