import os

print("My Final Project")
print("John Jhedrick M. Tarronas")
print("BSIT 1C")

loop = True
############################################################
def menu(user):
    """This is the Main Menu of the Program"""
    print("\nMAIN MENU")
    print(f"Welcome to my final project, {user}!")
    print("a - Terminal\nb - Activities\nc - Code Challenges\nd - Exit")
    choice = input("Please Enter the letter of the topic you want to explore: ")
    
    if choice.lower() == "a":
        terminal(user)
    elif choice.lower() == "b":
        activities(user)
    elif choice.lower() == "c":
        codechallenges(user)
    elif choice.lower() == "d":
        print("Thank you for using the system!")
        exit()
    else:
        print("Please enter a valid choice.")
        menu(user)

def terminal(user):
    """First Menu Option [TERMINAL]."""
    print("\nTERMINAL MENU")
    print("a - Description\nb - Navigation\nc - Commands/Functions\nx - Back to Main Menu")
    choice = input("Please Enter the letter of the topic you want to explore: ")
    
    if choice.lower() == "x":
        menu(user)
    elif choice.lower() == "a":
        print("The Terminal is a modern interface for various shells like cmd, PowerShell, Linux, Python, etc.")
        input("Press ENTER to continue...")
        terminal(user)
    elif choice.lower() == "b":
        print("\nTo navigate through files using the terminal, use commands like \n 'md' (Make Directory)\n 'cd' (Change Directory)\n 'dir' (Show current location files).\n 'type nul > filename.ext' to create a new files.\n")
        input("Press ENTER to continue...")
        terminal(user)
    elif choice.lower() == "c":
        print("\nCommand Keywords:")
        print("- dir: Displays a list of files and directories.")
        print("- md: Creates a new directory.")
        print("- cd: Changes the current directory.")
        print("- type nul > filename: Creates a new file.")
        input("Press ENTER to continue...")
        terminal(user)
    else:
        print("Please enter a valid choice.")
        terminal(user)
        
def codechallenges(user2):
    """Code Challenges Placeholder"""
    print("This is the list of the code challenge")
    print("1. code_challenge1 \n2. code_challenge2\n3. code_challenge3\n4. code_challenge4\n5. code_challenge5\n6. code_challenge6\n7. code_challenge7\n8. code_challenge8\n9. code_challenge9\n10. code_challenge10\n11. code_challenge11\n12. code_challenge12\n13. code_challenge13\n14. code_challenge14\n15. code_challenge15\n16. code_challenge16\n17. exit")
    choice = input("Please select the Code challenge that you want to explore (enter the number 1/2/3/4/5/6): ")
    if choice == "17":
        print("Thankyou for checking the list of my code challenge")
        input("Press ENTER to return to the menu...")
        menu(user)

    elif choice == "1":
        ask = input("Do you want to check this code challenge (yes/no) : ")
        if ask == "no":
            print("Thankyou for checking")
            codechallenges(user2)
        elif ask == "yes":
            print (" \t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\b*** \n\t\t\t\t\t\t\t\t\t\t\b\b***** \n\t\t\t\t\t\t\t\t\t\t\b\b\b******* \n\t\t\t\t\t\t\t\t\t\t\b\b***** \n\t\t\t\t\t\t\t\t\t\t\b*** \n\t\t\t\t\t\t\t\t\t\t* \n ") 
            print(input("Press ENTER to return to the menu..."))
            codechallenges(user2)
    
    elif choice == "2":
        ask = input("Do you want to check this code challenge (yes/no) : ")
        if ask == "no":
            print("Thankyou for checking")
            codechallenges(user2)
        elif ask == "yes":
            name = input ("What is your name: ")
            print(" \t\t\t\t\t\t\t\t\t\t   *\n\n\t\t\t\t\t\t\t\t\t\t\b\b  *  *  *  \n\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b *  *  *  *  * \n\t\t\t\t\t\t\t\t\t\t\b\b\b-------------\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b* |   Hi! "+name+"  | *\n\t\t\t\t\t\t\t\t\t\t\b\b\b------------- \n\t\t\t\t\t\t\t\t\t\t\b\b\b*  *  *  *  *  \n\n\t\t\t\t\t\t\t\t\t\t\b\b  *  *  *  \n\n\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b*")
            print(input("Press ENTER to return to the menu..."))
            codechallenges(user2)

    elif choice == "3":
        ask = input("Do you want to check this code challenge (yes/no) : ")
        if ask.lower() == "no":
            print("Thankyou for checking")
            print(input("Press the ENTER to return to the menu"))
            codechallenges(user2)
        elif choice.lower() == "yes":
            print("Please give an answer to the following")
        num1 = eval (input("enter a number: "))
        num2 = eval (input("enter a number: "))
        answer = num1 / num2
        print(num1 , " Division " , num2 , " = " , answer)
        print(input("Press ENTER to return to the menu..."))
        codechallenges(user2)
    
    elif choice == "4":
        ask = input("Do you want to check this code challenge (yes/no) : ")
        if ask.lower() == "no":
            print("Thankyou for checking")
            print(input("Press the ENTER to return to the menu"))
            codechallenges(user2)
        elif choice.lower() == "yes":
            print("Please give an answer to the following")
        number1 = int(input("Enter a number : "))
        number2 = int(input("Enter another number : "))

        add = number1 + number2
        minus = number1 - number2
        multiply = number1 * number2
        divide = number1 / number2
        exp = number1 ** number2
        mod = number1 % number2
        floordiv = number1 // number2

        print("The sum of ", number1 ,"and", number2 ,"is" , add )
        print("The difference of ", number1 ,"and", number2 ,"is" , minus )
        print("The product of ", number1 ,"and", number2 ,"is" , multiply )
        print("The quotient of ", number1 ,"and", number2 ,"is" , divide )
        print("The exponent of ", number1 ,"and", number2 ,"is" , exp )
        print("The reminder of ", number1 ,"and", number2 ,"is" , mod )
        print("The floor division of ", number1 ,"and", number2 ,"is" , floordiv )
        print(input("Press ENTER to return to the menu..."))
        codechallenges(user2)

    elif choice == "5":
        ask = input("Do you want to check this code challenge (yes/no) : ")
        if ask.lower() == "no":
            print("Thankyou for checking")
            print(input("Press the ENTER to return to the menu"))
            codechallenges(user2)
        elif choice.lower() == "yes":
            print("Please give an answer to the following")
            print("Hi, Welcome to my Bank Deposit, PH Denomination Program")

        name = input("Please Enter your name: ")
        deposit = eval(input("Enter the Amount you want to Deposit: "))

        print("Hi", name, "Thank you, here is the breakdown of the deposited amount")


        libo = deposit // 1000
        libo_sukli = deposit % 1000

        five_h = libo_sukli // 500
        five_sukli = libo_sukli % 500

        two_h = five_sukli // 200
        two_sukli = five_sukli % 200

        one_h = two_sukli // 100
        one_sukli = two_sukli % 100

        fifty = one_sukli // 50
        fifty_sukli = one_sukli % 50

        twenty = fifty_sukli // 20
        twenty_sukli = fifty_sukli % 20

        ten = twenty_sukli // 10
        ten_sukli = twenty_sukli % 10

        five = ten_sukli // 5
        five_sukli = ten_sukli % 5

        one = five_sukli // 1

        print(libo, " - 1,000 ")
        print(five_h, " - 500 ")
        print(two_h, " - 200 ")
        print(one_h, " - 100 ")
        print(fifty, " - 50 ")
        print(twenty, " - 20 ")
        print(ten, " - 10 ")
        print(five, " - 5 ")
        print(one, " - 1 ")
        print(input("Press ENTER to return to the menu..."))
        codechallenges(user2)

    elif choice == "6":
        ask = input("Do you want to check this code challenge (yes/no) : ")
        if ask.lower() == "no":
            print("Thankyou for checking")
            print(input("Press the ENTER to return to the menu"))
            codechallenges(user2)
        elif choice.lower() == "yes":
            print("Please give an answer to the following")
        prelim = eval(input("Enter your Pre lim Grade : "))
        midterm = eval(input("Enter your Midterm Grade : "))
        sfinals = eval(input("Enter your Semi Finals Grade : "))
        finals = eval(input("Enter your Finals Grade : "))
        quiz = eval(input("Enter your Quiz Grade : "))
        project = eval(input("Enter your Project Grade : "))

        average_grade = (prelim + midterm + sfinals + finals + quiz + project) / 6

        print(f"Your average grade is: {average_grade:.2f}")

        if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100) and (sfinals >= 65 and sfinals <= 100) and (finals >= 65 and finals <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100) :


            FG = (prelim * 0.15) + (midterm * 0.15) + (sfinals * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)

            if FG >= 75 :
                print("Congratulations, you passed the course/subject ")
            else :
                print("Sorry, you failed")
                print("Better luck next time")
        else :
            print("INVALID GRADE")
            print(input("Press ENTER to return to menu..."))
        codechallenges(user2)


            
    

#####################################################################
def activities(user1):
    """Activities Placeholder"""
    print("\nSecond MAIN MENU Option")
    print("LIST OF ACTIVITIES")
    print("1. Act1\n2. Act2\n3. Act\n4. Act4\n5. Exit")
    choice = input("Please Enter the number of the activities that you want to explore: ")

    if choice == "5":
        print(f"Thankyou for checking this activity {user}")
        input("Press ENTER to return to the menu....")
        menu(user)
    elif choice == "1":
        print("It's still not ready")
        activities(user1)
    elif choice == "2":
        activities(user1)


#####################################################################################################################################################
    elif choice == "3":
        background = input("Are you sure you want to answer the survey (yes / no) : ")
        print("This is a survey for your background")
        if background.lower() == "yes":
            print("Please answer the following questions")
        elif background.lower() == "no":
            print("Thank you for checking this activity")
            activities(user1)

        fullname = input("PLEASE INPUT YOUR FULL NAME : ")
        birthDay = input("PLEASE INPUT YOUR BIRTHDAY : ")
        birthMonth = input("INPUT YOUR BIRTHMONTH : ")
        birthYear = input("INPUT YOUR BIRTHYEAR : ")
        placeofbirth = input ("INPUT YOUR PLACE OF BIRTH : ")
        age = input("PLEASE INPUT YOUR AGE : ")
        gender = input("PLEASE INPUT YOUR GENDER : ")
        nationality = input("PLEASE PUT YOUR NATIONALITY : ")
        fname = input("PLEASE INPUT YOUR FATHER'S NAME : ")
        religion = input("PLEASE INPUT YOUR RELIGION : ")
        status = input("PLEASE INPUT YOUR STATUS : ")
        fulladdress = input ("PLEASE INPUT YOUR FULL ADDRESS : ")
        cellphone = input("PLEASE INPUT YOUR CONTACT NUMBER : ")
        email = input("PLEASE INPUT YOUR EMAIL ADDRESS : \n")
        print("Hi! My name is ", fullname ,", I was  born on", birthMonth , birthDay , birthYear,"at" , placeofbirth ,". I'm", age ,"years old,", gender ,"and i am a", nationality ,". My Father'sname is", fname,". I am a" , religion,"and currently", status ,". I reside at ", fulladdress ,"and you can reach me  by cellphone at", cellphone ,"or via Email", email ,"\n")

######################################################################################################################################################  
    elif choice == "4":
        background2 = input("Do you want to run this Activity (yes/no) : ")
        if background2.lower() == "yes":
            print("Please fill the following!")
        elif background2.lower() == "no":
            print("Thankyou for checking this activity!!") 
            activities(user1)
        number1 = int(input("Enter a number : "))
        number2 = int(input("Enter another number : "))

        add = number1 + number2
        minus = number1 - number2
        multiply = number1 * number2
        divide = number1 / number2
        exp = number1 ** number2
        mod = number1 % number2
        floordiv = number1 // number2

        print("The sum of ", number1 ,"and", number2 ,"is" , add )
        print("The difference of ", number1 ,"and", number2 ,"is" , minus )
        print("The product of ", number1 ,"and", number2 ,"is" , multiply )
        print("The quotient of ", number1 ,"and", number2 ,"is" , divide )
        print("The exponent of ", number1 ,"and", number2 ,"is" , exp )
        print("The reminder of ", number1 ,"and", number2 ,"is" , mod )
        print("The floor division of ", number1 ,"and", number2 ,"is" , floordiv )
        activities(user1)
    elif choice == "5":
        return(user1)
    else:
        print("Please Enter a Valid Choice")
        activities(user1)
    


# Main program loop
while loop:
    start = input("\nWould you like to use the system? (yes / no): ")
    if start.lower() == "yes":
        user = input("What's your name: ")
        menu(user)
    elif start == "no":
        print("Thank you for using the system!")
        break
    else:
        print("Please enter a valid choice.")


        