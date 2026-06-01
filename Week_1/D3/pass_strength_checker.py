## How to boolean to perform checks instead of using too many loops or conditional statments



def password(code):
        if(len(code) < 8 ):
            return "Pass must have atleast 8 characters"
        upper = False
        schar =False
        num = False
        for char in code:
            if char.isupper():
                upper = True
            if char.isdigit():
                num = True
        
            if not char.isalnum():
                schar = True
        if upper == False:
            return "Password must have one Uppercase"
        if schar == False:
            return "Password must have one special character"
        if num == False:
            return "Password must have one digit"
        if(len(code)> 8 and len(code)<12):
            return "Password Strength Medium"
        if(len(code)> 12 and len(code)<18):
            return "Password Strngth Strong"

abc = input("Enter the password: ")
print(password(abc))

#concluded week 1