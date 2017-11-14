import sys
import modul1 ## bu modül passcre'nin modülüdür
import os 
import logo
import APTEM


syslist = sys.argv
syslist.pop(0)

if ["--help"] == (syslist) or [] == (syslist):
	APTEM.clear()
	logo.logo1()
	print(""" 
	kullanım 
		python3 passcre.py -c 

	parametre
		["--help"] = bilgi verir
		["-c" veya "-C"] = parola oluşturma
		["-t" veya "-T"] = parola test etme
		
""")
elif ["-c"] == (syslist) or ["-C"] == (syslist):
	APTEM.clear()
	logo.logo1()
	modul1.pass1()
elif ["-t"] == (syslist) or ["-T"] == (syslist):
	APTEM.clear()
	logo.logo1()
	modul1.pass2()
elif ["-c","-C","--help","-t","-T"]:
	print("DAHA FAZLA BİLGİ İÇİN \"--help\"")