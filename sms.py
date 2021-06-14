import requests, os, sys, time, datetime
from requests import get
starttime = datetime.datetime.now().strftime("%X")
print("\033[96mCoded by github.com/Vaishu8987 \033[0m ")
print("\033[93m Version 4.0 \033[0m")
print("\033[91m Checking dependencies... \033[0m")
time.sleep(2)
os.system("bash rq.sh")
def menu() :
    print("\033[91m1. \033[92mSend anonymous sms\033[0m")
    print("\033[91m2. \033[92mCheck status of sms\033[0m")
    print("\033[91m3. \033[92mHelp\033[0m")
    print("\033[91m4. \033[92mCheck previous history! \033[0m")
    print("\033[91m5. \033[92mExit\033[0m")
def control() :
    ctrl = input("What you want to do : ")
    if ctrl == "1" :
        sms()
    elif ctrl == "2" :
        status()
    elif ctrl == "3" :
        help()
    elif ctrl == "4" :
        history()
    elif ctrl == "5" :
        print("thanks for using it.\nplease stay connected with us. github.com/Vaishu8987")
        exit()
    else :
        print("\033[91mInvalid number\033[0m")
def sms() :
   phone_no = input("enter phone number : ")
   msg = input("message to send : ")

   resp = requests.post('http://api.txtlocal.com/send/?',{
	'phone' : phone_no,
	'message' : msg ,
	'key' : 'txtlocal'
   })
   print(resp.text)
   time = datetime.datetime.now()
   clock = time.strftime("%X")  
   date = time.strftime("%x")
   save = open("sess.txt", "a")
   save.write(f"\nip = {ip} : time = {clock} : date = {date} : stats = {resp.text} : phone no.  = {phone_no} ")
def history() :
    if os.path.exists("sess.txt") :
        with open("sess.txt","r") as file :
            sessions = file.read().splitlines()
            ses_numbers = len(sessions)
            if ses_numbers > 1 :
                os.system("python sess_info.py")
                more_details = input("Do you wanna see all sessions? (Default : no) : ").lower()
                if more_details == "yes" or more_details == "y" :
                    os.system("cat sess.txt")
                else :
                    print("Thanks for using sms-scammer, please keep supporting us.\nGithub : github.com/Vaishu8987")
            elif ses_number == 1: 
                print(file.readline)
            else :
                print("either file is empty or any error occurred!")
    else :
        print("Either you are using this first time or maybe you had deleted history. ")
def status() :
  textID = input("Enter textID of sms : ") 
  os.system(f"curl https://textbelt.com/status/{textID}")
def help() :
    print("please choose your problem from undergiven conditions! ")
    print("A. Can't send sms after one attempt in a to same number!")
    print("B. Can't send more than one sms even to different number. ")
    print("C. Other")
    qna = input(">>> ").lower()
    if qna == "a" :
        print("Bcoz this is just a demo version so it can send only 1 sms in a day to same number however you can send to different number by using vpn.")
    elif qna == "b" :
        print("please check your vpn carefully and use best vpns only. Like nordvpn , protonvpn etc. ")
    elif qna == "c" :
        print("sorry for any problem! Please mail us your problem on hackersacademyofindia@gmail.com or you can mention your problem in github.com/Vaishu8987")
    else :
        print("Invalid option!! \n exiting.. Sorry..")
        exit()
os.system("clear")
os.system("toilet -f mono12 -F gay Scammer")
print("\033[94m########################## \033[31mVr. 4.0\033[0m \033[94m#########################  ")
print("\033[1;96mCoded by github.com/Vaishu8987\033[0m")
print(f"Program started at : {starttime}")
ip = get("https://api.ipify.org").text
ip_c = input("\033[95;107mDo you want to see your current ip ? : \033[0m").lower()
if ip_c == "yes" or ip_c == "y" :
   print(f"\033[1;93mYou are currently using with ip :\033[0m \033[91;107m{ip}\033[0m ")
elif ip_c == "no" or ip_c == "n" :
   print("\033[93;101mi hope you know what you are doing. :) \033[0m")
else :
   print("invalid option!! type yes or no ")
menu()
control()
