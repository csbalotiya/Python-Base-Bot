import webbrowser as web
import os
from gtts import gTTS
lng = 'en'
file= ''

print("-----------------Welcome to the App service Menu-----------")
print("                     -> Web Services")
print("                     -> Email")
print("                     -> Shopping")
print("                     -> Social Media")
print("                     -> Entertainment")

arr = ["notepad","idle","Zoom","Command Prompt","cmd","spotify"]
s = []
while(True):
    print("What Service you want to run :   ",end=" ")
    s = list(map(str,input().strip().split()))
    if(s[0] == "quit" or s[0] == "Quit"):
        txt = 'We are Quiting'
        obj = gTTS(text = txt , lang = lng,slow = False)
        file  = 'quit'
        obj.save(str(file)+".mp3")
        os.system("start "+str(file)+".mp3")
        break
    if(len(s) == 1):
        print("opening "+s[0])
        txt = "opening "+ str(s[0])
        obj = gTTS(text = txt , lang = lng,slow = False)
        file = s[0]
        obj.save(str(file)+".mp3")
        os.system("start "+str(file)+".mp3")
    else:
        print(s[-2]+"ing "+s[-1])
        txt = str(s[-2]) +"ing "+ str(s[-1])
        obj = gTTS(text = txt , lang = lng,slow = False)
        file = s[-1]
        obj.save(str(file)+".mp3")
        os.system("start "+str(file)+".mp3")
        
    x=os.system(s[-1])
    if (x == 0):
        pass    
    else:
        web.open("http://www."+s[-1]+".com")
    

# Code Writter - CS Balotiya 
