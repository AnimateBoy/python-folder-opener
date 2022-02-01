from pdb import run
import webbrowser
import os


a = int(input("Please Enter Your Password For Accessing The Folder"))

##the password is 1234
#But you can change the passsword
#change the value below from 1234 to your desire


if a == (1234):
    print('Correct Password!')
    os.startfile(r'C:\Users\shiva\Documents\Coding')
#                   ^^^^Change this to your path^^

else:
    print('Wrong Password')


  
