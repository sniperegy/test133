import requests,base64
from threading import Thread as t
import requests,os,sys,time,pyfiglet
from time import sleep
from colorama import Fore
G=Fore.GREEN
R=Fore.RED
Y=Fore.YELLOW
B=Fore.BLUE
email = input(Y+'Enter Your Email : '+G)
print()
password = input(Y+'Enter Your Password : '+G)
print()
number = input(Y+'Enter Your Number : '+G)
if '011' in number:
    nma = number[+1:]
else:
    nma = number
code =email+':'+password
ccode = code.encode('ascii')
base64_bytes = base64.b64encode(ccode)
auth = base64_bytes.decode('ascii')
autho = "Basic"+" "+auth

urllog = 'https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan'
headerslog = {"applicationVersion": "2","applicationName": "MAB",
"Accept": "text/xml",
"Authorization":autho,
"APP-BuildNumber": "547",
"APP-Version": "22.13.0",
"OS-Type": "Android",
"OS-Version": "10",
"APP-STORE": "Huawei",
"Is-Corporate": "false",
"Content-Type": "text/xml; charset=UTF-8",
"Content-Length": "290",
"Host": "mab.etisalat.com.eg:11003",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.12.8",
"ADRUM_1": "isMobile:true",
"ADRUM": "isAjax:true"}
datalog = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType>J19SG</modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
a = requests.post(urllog, headers=headerslog, data=datalog)

if 'true' in a.text:
    lk = a.headers['Set-Cookie']
    id = lk[:-127]
    bas = a.headers["auth"]
    os.system('clear')
    
    urlsub = "https://mab.etisalat.com.eg:11003/Saytar/rest/harleyPreset/migrate"
    
    headerssub = {"applicationVersion":"2",
"applicationName":"MAB",
"Accept":"text/xml",
"Cookie":id,
"Language":"ar",
"APP-BuildNumber":"891",
"APP-Version":"26.5.0",
"OS-Type":"Android",
"OS-Version":"10",
"APP-STORE":"GOOGLE",
"auth":"Bearer "+bas+"",
"Is-Corporate":"false",
"Content-Type":"text/xml; charset=UTF-8",
"Content-Length":"550",
"Host":"mab.etisalat.com.eg:11003",
"Connection":"Keep-Alive",
"User-Agent":"okhttp/4.10.0"}

    datasub = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><msisdn>%s</msisdn><operation>MIGRATE</operation><parameters><parameter><name>MI_QUOTA</name><value>300000</value></parameter><parameter><name>UNIT_QUOTA</name><value>300000</value></parameter><parameter><name>VALIDITY</name><value>30</value></parameter><parameter><name>PRICE</name><value>0</value></parameter><parameter><name>FREE_SERVICE_NAME</name><value>BE_FIT</value></parameter></parameters><productName>HARLEY_PRESET_BUNDEL</productName></submitOrderRequest>"%(nma)
    subscribe = requests.post(urlsub,headers=headerssub,data=datasub).text
    if "true" in subscribe:
    	print(G+"Done Add Unites")
    else:
    	print(R+"Something Went Wrong")
else:
    print(R+'Check Your Information ')


