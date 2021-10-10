def Qone():
    def multiples(f1, f2start, f2end, name):
        print("Hi ", name, " here is your times table") 
        for index in range (f2start, f2end):
            print(f1, " x ", index, " = ", f1 * index) 

    Name = input("what is your name?") 
    Table = input("enter your times table")

def Qfour():
    def getPword(pw,Check):

        if (len(pw) < 6) or (len(pw) > 8): # if len of password is not between 6 and 8  
            print("password must be between 6 and 8 characters") 
            return x 
        elif pw != storepw: # if password does not match stored value of password 
            Attampt = attampt + 1 
            return x 
        else:
            Check += 1 
            return x   

    storepw = "password"
    x = ""
    Check = 0 
    Attampt = 1 
    if Check != 0:
        if Attampt == 1: 
            x = input("please enter password") 
    elif Attampt >= 2: 
        x = input("please re-enter password") 

    getPword()  

Qfour()