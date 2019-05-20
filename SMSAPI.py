import requests, time, json, os, string

class colours:
    bold = '\033[1m'
    underline = '\033[4m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    end = '\033[0m'

email = 'ENTER_EMAIL'
pw = 'ENTER_PASSWORD'
tocountry = '+44'
fromcountry = '+44'
os.system('clear')
route = 'auto'

fromnumber = raw_input(colours.bold+colours.purple+'Ender sender number: '+colours.end)
os.system('clear')
print(colours.underline+colours.bold+colours.blue+'From: '+fromnumber+colours.end)
tonumber = raw_input('\n'+colours.bold+colours.purple+'Enter recipients number: '+colours.end)
os.system('clear')
print(colours.underline+colours.bold+colours.blue+'From: '+fromnumber+colours.end)
print(colours.underline+colours.bold+colours.blue+'To: '+tonumber+colours.end)
message = raw_input('\n'+colours.bold+colours.purple+'Enter message: '+colours.end)#.replace("'","\'").replace('"','\"')
os.system('clear')


print("\nGrabbing initial ID from spoofmytextmessage.com...")
url = ('https://api.spoofmytextmessage.com/2.0/index.php?task=login&email='+email+'&pass='+pw)
r = requests.get(url)
data = str(r.json())
#print(data)

secureid = (str(data)).split("secureid': u'")[1].split("', u'verifycode")[0]
id = (str(data)).split("u'id': u'")[1].split("', u'online")[0]
print(colours.bold+colours.blue+'\n* SecureID - '+colours.end+colours.bold+colours.green+secureid+colours.end)
print(colours.bold+colours.blue+'\n* ID - '+colours.end+colours.bold+colours.green+id+colours.end)

print('\n'+"Pulling unique identifier for SMS codes to send from spoofmytextmessage.com...")
url = ('https://api.spoofmytextmessage.com/2.0/index.php?task=getCodes&mid='+id+'&email='+email+'&secureid='+secureid)
r = requests.get(url)
data = str(r.json())
#print(data) 

if "count': 0" in data: 
	print(colours.red+"It does not appear you have any valid credits on spoofmytextmessage.com. Purchase more."+colours.end)
	ans = raw_input('\nGo to website (y/n); ')
	if ans == 'y':
		os.system('firefox https://www.spoofmytextmessage.com/my')
		os.system('clear')
		quit()
	else:
		os.system('clear')
		quit()
		
else:
        code = data.split("messages': [u'")[1].split("', u'")[0].replace('\']}]','')
	print(colours.bold+colours.blue+"\n* Unique Identifier - "+colours.end+colours.bold+colours.green+code+colours.end)

	print("\nCrafting the SMS message and sending through spoofmytextmessage.com...")
	payload = ('&non=number&fromnumber='+fromnumber+'&to='+tonumber+'&tocountry='+tocountry+'&fromcountry='+fromcountry+
	'&text='+message+'&code='+code+'&task=send&terms=1&secureid='+secureid+'&mid='+id+'&email='+email+'&source=setoolkit&selves=1&route='+route)
	url = ('https://api.spoofmytextmessage.com/2.0/index.php?task=send'+payload)

	r = requests.post(url)
	print('\n')
	data = str(r.json())
	print('\n'+data)
	


