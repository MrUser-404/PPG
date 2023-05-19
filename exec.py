import os,time,platform
try:
	import requests
except ImportError:
	os.system('pip install requests')
	
x=platform.architecture()[0]
if x=="64bit":
	os.system('clear')
	print("\033[1;97m[\033[1;92m✓\033[1;97m]\033[0m\033[1;97m64bit Trouvé\033[0m")
	time.sleep(2)
	os.system('chmod +x guard64')
	os.system('./guard64')
	
'''elif x=="32bit":
	os.system('clear')
	print('\033[1;97m[\033[1;92m✓\033[1;97m]32bit Trouvé\033[0m')
	time.sleep(2)
	os.system('chmod +x guard32')
	os.system('./guard32')'''