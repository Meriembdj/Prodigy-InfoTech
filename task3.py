import string
def PasswordChecker(password):
    u = 0
    l = 0
    degits = 0
    schar = 0
    uplow = 0
    C=0
#loop to count degits ,  special characters  , upper and lower letters 
    for char in password:
        if char.isdigit():
            degits += 1
        if char not in string.ascii_letters + string.digits + string.whitespace:
            schar += 1
        if char.islower():
            l += 1
        if char.isupper():
            u += 1
# condition to check if both upper and lower letters include in the password
    if not (l > 0 and l < len(password) and u > 0 and u < len(password)):
        uplow += 1
#condition to check if the password is long enough 
    if len(password) < 8:
        print("Password is short, you must add more characters")
        C+=1
#condition to check if the password contains degits or not
    if degits == 0:
        print("You must add numbers")
        C+=1
# condition to check if both upper and lower letters include in the password
    if uplow != 0:
        print("Your password must include both upper and lower letters")
        C+=1
#condition to check if the password contains special characters 
    if schar == 0:
        print("You must add special characters such as @ ? ! % ; / ")
        C+=1
#the Counter C to give feedbacks on password strenght 
    if C == 0:
        print("Your password is very strong")
    elif C == 2 or C == 1 :
        print("Your password is Moderate")
    elif C == 3 or C == 4 :
        print("Your password is weak")
        
#Main block 
while True:
    password = input("Select your password ")
    
    PasswordChecker(password)