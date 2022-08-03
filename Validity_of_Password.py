'''
Thomas Koutsidis
June 18th, 2022

Question 5

This program checks the validity of password input by users. 
The criteria for the password is:
    - minimum length: 4 characters
    - maximum length: 8 characters
    - first character has to be a letter
    - at least 1 number between [0-9]
    - at least 1 character from [$#@]
If an invalid password is entered, the program will print an error message stating which error and then quit.
'''

def main():
    print("This program checks passwords.")
    pw = input("Please enter a password: ")
    if len(pw) < 4:
        print("Error: This password has less than 4 characters!")
    elif len(pw) > 8:
        print("Error: This password has more than 8 characters!")
    elif pw[0].isalpha() == False:
        print("Error. First character has to be as letter.")
    else:
        digit = False
        special_char = False
        for i in pw:
            if i.isdigit():
                digit = True
                break
        if digit != True:
            print("Error. There needs to be a digit.")
        for i in pw:
            if i == "$":
                special_char = True
                break
            elif i == "#":
                special_char = True
                break
            elif i == "@":
                special_char = True
                break
        if special_char != True:
            print("Error. There needs to be a special character of [$#@]")
        
        if special_char == True and digit == True:
            print("You have entered a valid password.")
               
    
main()
