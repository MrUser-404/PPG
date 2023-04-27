import os
import requests
import time
import json
try:
	import requests
except:
	os.system("pip install requests")
def menu():
	try:
		os.system('clear')
		token=input("\x1b[7;91mVotre Token\033[0m=>\033[92m")
		res=requests.get("https://graph.facebook.com/me?access_token="+token)
		rp=json.loads(res.text)
		fb_name=rp["name"]
		fb_id=rp["id"]
		save_token=open("token.txt", 'w')
		save_token.write(token)
		save_token.close()
		save_id=open("id.txt", 'w')
		save_id.write(fb_id)
		save_id.close()
		os.system('clear')
		print("\033[0mNom:",fb_name)
		print("ID:",fb_id)
	except KeyError:
		print("Compte checkpoint!!!")
		time.sleep(2)
		menu()
		
		
	print(f"{oo(1)}Activé")
	print(f"{oo(2)}Désactiver")
	print(f"{oo(3)}Créateur")
	print(f"{oo(4)}Déconnecter")
	print(f"{oo(5)}Quittez")
	
	inpp=int(input("Votre choix==>"))	
	if (str(inpp))=="1":
		activated = ("true")
		jay(token, activated)
	elif (str(inpp))=="2":
		not_active = ("false")
		jay(token, not_active)
	elif (str(inpp))=="3":
		os.system('clear')
		os.system('xdg-open https://www.facebook.com/MrUser404')
	elif inpp=="4":
		os.system("rm -rf token.txt")
		os.system("clear")
		print("Compte Déconnecter avec succès")		
	elif (str(inpp))=="5":
		exit('À la prochaine!!!')
		
def oo(num):
	return f"[{num}]"
	
	
def jay(token, enable = True):
	try:
		id=open("id.txt", 'r').read()
	except:
		os.system("clear")
		print("ID utilisateur pas trouvé!!!")
		time.sleep(2)
		os.system('clear')
		menu()
		
	data= 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))

	headers={"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % token}
	url="https://graph.facebook.com/graphql"
	res=requests.post(url, data = data, headers = headers)
	if ('"is_shielded":true') in res.text:
			os.system('clear')
			print("PPG Activé")
			time.sleep(2)
			y=input("Voulez vous continuez [oui ou non]=>")
			if y=="oui":
				menu()
			elif y=="non":
				os.system("clear")
				exit("À la prochaine!!!")
				time.sleep(2)
	elif ('"is_shielded":false') in res.text:
			os.system("clear")
			print("PPG Désactivé avec succès!!")
			z=input("Voulez vous continuez [oui ou non]=>")
			if z=="oui":
				menu()
			elif z=="non":
				os.system("clear")
				print("À la prochaine!!!")
				time.sleep(2)
	else:
			os.system('clear')
			print("Opération terminer avec des erreurs!!!")
			
menu()
			
			
						
		
		
		

	