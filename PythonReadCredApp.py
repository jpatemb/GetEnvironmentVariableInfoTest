#Author | JPE
#Encoding | -UTF-8 #
import os

email_id = os.environ['my_email']
password = os.environ['my_password']

print("My Email ID is: ", email_id)
print("The Password for said Email ID is: {} ".format(password))
