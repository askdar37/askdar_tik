import requests
from colorama import Style,Fore

R = Fore.RED
G =Fore.GREEN
B = Fore.BLUE
Y = Fore.YELLOW
c = Fore.LIGHTMAGENTA_EX
b = Fore.LIGHTBLUE_EX
r = Fore.LIGHTRED_EX
w = Fore.WHITE
print(b+
"""
 ______   __     __  __   
/\__  _\ /\ \   /\ \/ /    
\/_/\ \/ \ \ \  \ \  _"-.  
   \ \_\  \ \_\  \ \_\ \_\  
    \/_/   \/_/   \/_/\/_/   
    --------------------------------------------------------------
 By fostn : Insta : askdar37 - Twitt : askdar37 - Telegram : @askdar37
    ---------------------------------------------------------------
"""
	)
User = input(w+"Enter Username : ")

Data = requests.get(f'https://0ff0a6eb-9885-4c7f-9d03-00c09c0a7e4b.id.repl.co/?username={User}').json()
name = Data['name']
bio = Data['bio']
followers = Data['followers']
following = Data['following']
id = Data['id']
url_date = requests.get(f"https://mr-abood.herokuapp.com/TikTok/Account/Create/Date?user_id={id}").json()
image = Data['avatar']
date_create = url_date["date"]
print(G+"---------------------------------")
print("Username : " + str(User))
print(r+"Name : "+ str(name))
print(Y+"Bio : "+ str(bio))
print(G+"Followers : "+ str(followers))
print(R+"Following : "+ str(following))
print(c+"Id : "+ str(id))
print(G+"Date Create : "+str(date_create))
print(G+"---------------------------------")
print(w+"\nfor more tools, follow me ! .")

