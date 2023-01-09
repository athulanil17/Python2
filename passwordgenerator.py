import string
import random

def password(length):
    passchar = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) 
    
    for n in range(length)])
    print("Your randomly generated password is:", passchar)

password(length=int(input("Enter the length of password:")))