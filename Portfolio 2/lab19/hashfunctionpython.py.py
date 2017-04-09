"""a basic salted-hash function in a programming language of your
choice that takes a password as a string and produces a pseudo-random
integer based on that string"""

import time

#input
password=input("Please enter your password you want to hash: ")
#putting password in a list
password=list(password)
#new list
hashpassword=[]

#asciivalue function, take each letter of the string and converting it to its ascii value
def asciivalue(): 
    for i in password:
        j=ord(i)
        hashpassword.append(j)
    return(hashpassword)

#multiply function, multiple it by a specific number based on its position in the string sequence
def multiply(hashpassword):
    Counter=1
    integer=0
    while integer<len(hashpassword):
        hashpassword[integer]=hashpassword[integer]*Counter
        Counter=Counter+1
        integer=integer+1
    return(hashpassword)

#add and salt function, add the values together and add salt in such as the current date.
def addnumberandsalt(hashpassword):
    total=sum(hashpassword)
    total=str(total)+time.strftime("%d%m%y")
    return(total)

#run functions
asciivalue()
multiply(hashpassword)
total=addnumberandsalt(hashpassword)
print("Your pseudo-random integer password is: " + total)





