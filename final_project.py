import os

# print("My Final Project")
# print("John Jhedrick M. Tarronas")
# print("BSIT 1C")

loop = True
############################################################

def menu(user):
    """This is the Main Menu of the Program"""
    print("\nMAIN MENU")
    print(f"Welcome to my final project, {user}!")
    print("1. Terminal\n2. Activities\n3. Code Challenges\n4. Exit")
    while loop:
        choice = input("Please Enter the topic you want to explore (terminal/activities/code challenges/exit): ")

        if choice.lower() == "terminal":
            terminal(user)
        elif choice.lower() == "activities":
            activities(user)
        elif choice.lower() == "code challenges":
            codechallenges(user)
        elif choice.lower() == "exit":
            print("Thank you for using the system!")
            exit()
        else:
            print("Please enter a valid choice.")
        
##########################################################################################################################################################################
def terminal(user):
    """First Menu Option [TERMINAL]."""
    print("\nTERMINAL MENU")
    print("1. Description\n2. Navigation\n3. Commands/Functions\n4. Back to Main Menu")
    while loop:
        choice = input("Please Enter the number of the topic you want to explore: ")
        
        if choice.lower() == "4":
            menu(user)
        elif choice.lower() == "1":
            print("The Terminal is a modern interface for various shells like cmd, PowerShell, Linux, Python, etc.")
            input("Press ENTER to continue...")
            terminal(user)
        elif choice.lower() == "2":
            print("\nTo navigate through files using the terminal, use commands like \n 'md' (Make Directory)\n 'cd' (Change Directory)\n 'dir' (Show current location files).\n 'type nul > filename.ext' to create a new files.\n")
            input("Press ENTER to continue...")
            terminal(user)

        elif choice.lower() == "3":
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
#########################################################################################################################################################        
def codechallenges(user2):
    """Code Challenges Placeholder"""
    print("This is the list of the code challenge")
    print("1. code_challenge1 \n2. code_challenge2\n3. code_challenge3\n4. code_challenge4\n5. code_challenge5\n6. code_challenge6\n7. code_challenge7\n8. code_challenge8\n9. code_challenge9\n10. code_challenge10\n11. code_challenge11\n12. code_challenge12\n13. code_challenge13\n14. code_challenge14\n15. code_challenge15\n16. code_challenge16\n17. exit")
    while loop:
        choice = input("Please select the Code challenge that you want to explore (enter the number 1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17): ")
        if choice == "17":
            print("Thankyou for checking the list of my code challenge")
            input("Press ENTER to return to the menu...")
            menu(user)
    
        elif choice == "1":
            while loop:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask == "no":
                    print("Thankyou for checking")
                    codechallenges(user2)
                elif ask == "yes":
                    print (" \t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\b*** \n\t\t\t\t\t\t\t\t\t\t\b\b***** \n\t\t\t\t\t\t\t\t\t\t\b\b\b******* \n\t\t\t\t\t\t\t\t\t\t\b\b***** \n\t\t\t\t\t\t\t\t\t\t\b*** \n\t\t\t\t\t\t\t\t\t\t* \n ") 
                    print(input("Press ENTER to return to the menu..."))
                    codechallenges(user2)
                else:
                    print("Please enter a valid choice.")

        elif choice == "2":
            while loop:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask == "no":
                    print("Thankyou for checking")
                    codechallenges(user2)
                elif ask == "yes":
                    name = input ("What is your name: ")
                    print(" \t\t\t\t\t\t\t\t\t\t   *\n\n\t\t\t\t\t\t\t\t\t\t\b\b  *  *  *  \n\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b *  *  *  *  * \n\t\t\t\t\t\t\t\t\t\t\b\b\b-------------\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b* |   Hi! "+name+"  | *\n\t\t\t\t\t\t\t\t\t\t\b\b\b------------- \n\t\t\t\t\t\t\t\t\t\t\b\b\b*  *  *  *  *  \n\n\t\t\t\t\t\t\t\t\t\t\b\b  *  *  *  \n\n\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b*")
                    print(input("Press ENTER to return to the menu..."))
                    codechallenges(user2)
                else:
                    print("Please enter a valid choice.")


        elif choice == "3":
            while True:  
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking.")
                    input("Press ENTER to return to the menu...")
                    codechallenges(user2)  
                    break  
                elif ask.lower() == "yes":
                    print("Please give an answer to the following.")
                    try:
                        num1 = eval(input("Enter a number: ")) 
                        num2 = eval(input("Enter another number: "))
                        if num2 == 0:  
                            print("Division by zero is not allowed.")
                        else:
                            answer = num1 / num2
                            print(num1, "Division", num2, "=", answer)
                    except Exception as e: 
                        print(f"Error: {e}. Please enter valid numbers.")
                    input("Press ENTER to return to the menu...")
                    codechallenges(user2)  
                else:
                    print("Please Enter a valid choice")

               
        
        elif choice == "4":
            while True:  # Infinite loop to handle multiple inputs
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking")
                    input("Press ENTER to return to the menu...")
                    codechallenges(user2)  # Call the function to return to the menu
                    break  # Exit the loop
                elif ask.lower() == "yes":
                    print("Please give an answer to the following")
                    number1 = int(input("Enter a number: "))
                    number2 = int(input("Enter another number: "))

                    # Perform calculations
                    add = number1 + number2
                    minus = number1 - number2
                    multiply = number1 * number2
                    divide = number1 / number2
                    exp = number1 ** number2
                    mod = number1 % number2
                    floordiv = number1 // number2

                    # Print results
                    print("The sum of", number1, "and", number2, "is", add)
                    print("The difference of", number1, "and", number2, "is", minus)
                    print("The product of", number1, "and", number2, "is", multiply)
                    print("The quotient of", number1, "and", number2, "is", divide)
                    print("The exponent of", number1, "and", number2, "is", exp)
                    print("The remainder of", number1, "and", number2, "is", mod)
                    print("The floor division of", number1, "and", number2, "is", floordiv)
                    input("Press ENTER to return to the menu...")
                    codechallenges(user2)  # Call the function to return to the menu
                else:
                    # Handle invalid inputs
                    print("Please enter a valid choice.")

                

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

        elif choice == "7":
            ask = input("Do you want to check this code challenge (yes/no) : ")
            if ask.lower() == "no":
                print("Thankyou for checking")
                print(input("Press the ENTER to return to the menu"))
                codechallenges(user2)
            elif choice.lower() == "yes":
                print("Grocery")

            name = input("Enter your name: ")
            grocery_purchase = input("Did you purchase a grocery today : ")

            if grocery_purchase == 'yes':
                print(f"\nWelcome {name} to the Counter\n")

                item_name = input("What item did you purchase: ")
                item_price = float(input("Item price: "))
                
                age = input("Age: ")
                if age.isnumeric():
                    print("Yes, this is a number")
                    new_age = int(age) + 10  
                    payment_amount = float(input("Payment amount: "))
                    tax = item_price * 0.123  
                    senior_discount = 0

                    if int(age) >= 60:
                    
                        senior_discount = item_price * 0.052
                    total_price = item_price + tax - senior_discount
                
                    change = payment_amount - total_price
                
                    print("\nHere is your receipt:\n")
                    print(f"Item: {item_name}")
                    print(f"Item price: {item_price}")
                    print(f"Tax of 12.3% applied: {tax:.2f}")
                    print(f"Senior discount applied: {senior_discount:.2f}")
                    print(f"Total price after tax and discounts: {total_price:.2f}")
                    print(f"Thank you for your payment, your change is: {change:.2f}\n")

                else:
                    print("Invalid input. Age must be a number.")
            else:
                print("No grocery purchase today. Have a nice day!")

            print(f"Hello, {name} you have purchased a {item_name} and it cost {item_price} pesos, and by adding the tax which is {tax} pesos and the senior discount which is {senior_discount} pesos, the total is {total_price} pesos and you payed {payment_amount} pesos, so your change is {change} pesos ")
            print(input("Press ENTER to return to menu"))
            codechallenges(user2)

        elif choice == "8":
            ask = input("Do you want to check this code challenge (yes/no) : ")
            if ask.lower() == "no":
                print("Thankyou for checking")
                print(input("Press the ENTER to return to the menu"))
                codechallenges(user2)
            elif choice.lower() == "yes":
                print("Please answer the following")
            num = int(input("Enter a number: "))
            if num < 0:
                print("Factorial is not for negative numbers.")
            else:
                factorial = 1
                for jhed in range(num, 0, -1):
                    factorial *= jhed

                print(f"The factorial of {num} is {factorial}.")
                print(input("Press ENTER yo return to the menu"))
                codechallenges(user2)

        elif choice == "9":
            ask = input("Do you want to check this code challenge (yes/no) : ")
            if ask.lower() == "no":
                print("Thankyou for checking")
                print(input("Press the ENTER to return to the menu"))
                codechallenges(user2)
            elif choice.lower() == "yes":
                print("Please answer the following")
            j = int(input("Give a number: "))
            for x in range(j, 0,-1):
                for y in range(j,x,-1):
                    print(" ", end=" ")
                print("* " * x)
                print(input("Press ENTER yo return to the menu"))
                codechallenges(user2)


        elif choice == "10":
            ask = input("Do you want to check this code challenge (yes/no) : ")
            if ask.lower() == "no":
                print("Thankyou for checking")
                print(input("Press the ENTER to return to the menu"))
                codechallenges(user2)
            elif choice.lower() == "yes":
                print("Please answer the following")
            for x in range(6, 0, -1):
                for y in range(1, x + 1):
                    print(" ", end=" ")
                for z in range(6, x, -1):
                    print("*", end=" ")
                for a in range(6, x, -1):
                    print("*", end=" ")
                print()

            for x in range(1, 5):
                for y in range(1, x + 2):
                    print(" ", end=" ")
                for z in range(5, x, -1):
                    print("*", end=" ")
                for a in range(5, x, -1):
                    print("*", end=" ")
                print( )
            print(input("Press ENTER yo return to the menu"))
            codechallenges(user2)

        elif choice == "11":
            ask = input("Do you want to check this code challenge (yes/no) : ")
            if ask.lower() == "no":
                print("Thankyou for checking")
                print(input("Press the ENTER to return to the menu"))
                codechallenges(user2)
            elif choice.lower() == "yes":
                print("Please answer the following")
            for x in range(5, 0, -1):
                for y in range(1, x + 1):
                    print(" ", end=" ")
                for z in range(5, x, -1):
                    print("*", end=" ")
                for a in range(4, x, -1):
                    print("*", end=" ")
                print()


            for x in range(1, 5):
                for y in range(1, x + 2):
                    print(" ", end=" ")
                for z in range(4, x, -1):
                    print("*", end=" ")
                for a in range(3, x, -1):
                    print("*", end=" ")
                print()
            print(input("Press ENTER yo return to the menu"))
            codechallenges(user2)


        elif choice == "12":
            ask = input("Do you want to check this code challenge (yes/no) : ")
            if ask.lower() == "no":
                print("Thankyou for checking")
                print(input("Press the ENTER to return to the menu"))
                codechallenges(user2)
            elif choice.lower() == "yes":
                print("Please answer the following")
            for x in range(7, 0, -1):
                for y in range(1, x + 1):
                    print(" ", end=" ")
                for z in range(7, x, -1):
                    print("*", end=" ")
                for a in range(6, x, -1):
                    print("*", end=" ")
                print()
            for x in range(0, 4):
                for y in range(4, 0, -1):
                    print(" ", end= " ")
                for z in range(3, 4):
                    print("*", end= " ")
                for a in range(4, 0, -1):
                    print("*", end= " ")
                print()
            print(input("Press ENTER yo return to the menu"))
            codechallenges(user2)


        elif choice == "13":
            ask = input("Do you want to check this code challenge (yes/no) : ")
            if ask.lower() == "no":
                print("Thankyou for checking")
                print(input("Press the ENTER to return to the menu"))
                codechallenges(user2)
            elif choice.lower() == "yes":
                print("Please answer the following")
            for x in range(1,7):
                for y in range(6, x, -1):
                    print(" ", end= " ")
                for z in range(x, 1, -1):
                    print(z, end= " ")
                for a in range(1, x + 1):
                    print(a, end= " ")
                print()
            for x in range(5, 0, -1):
                for y in range(5 - x + 1):
                    print(" ", end=" ")
                for z in range(x, 0, -1):
                    print(z, end=" ")
                for a in range(2, x + 1):
                    print(a, end=" ")     
                print()  
            print(input("Press ENTER yo return to the menu"))
            codechallenges(user2)


        elif choice == "14":
            ask = input("Do you want to check this code challenge (yes/no) : ")
            if ask.lower() == "no":
                print("Thankyou for checking")
                print(input("Press the ENTER to return to the menu"))
                codechallenges(user2)
            elif choice.lower() == "yes":
                print("Please answer the following")
            go = True
            no = 0
            while go == True:
                num = eval(input("Please Enter a number--->  "))
                if num == 0:
                    print("Program Terminated")
                    print(f"The total of the number that you have given is {no}")
                    print(input("Press ENTER to return to the menu..."))
                    codechallenges(user2)

                else:
                    no += num
                    continue


        elif choice == "15":
            ask = input("Do you want to check this code challenge (yes/no) : ")
            if ask.lower() == "no":
                print("Thankyou for checking")
                print(input("Press the ENTER to return to the menu"))
                codechallenges(user2)
            elif choice.lower() == "yes":
                print("Please answer the following")
            isGo = True
            num = 0
            while isGo == True:
                question = input("Do you want to add more Triangles ----> ")

                if question.lower() == "no":
                    os.system("cls")
                    print("Progress Terminated")
                    print(input("Press ENTER to reuturn  to menu....")) 
                    codechallenges(user2)
                    isGo = False

                elif question.lower() == "yes":
                    os.system("cls")
                    num += 1
                    for x in range(1,6):
                        for y in range(1,num + 1):
                            for r in range(1, x + 1):
                                print("^", end=" ")
                            for z in range(5, x, - 1):
                                print(" ", end=" ")
                            print(" ", end=" ")
                        print()
                    continue
                else:
                    os.system("cls")
                    print("Please answer only with Yes or No") 


        elif choice == "16":
            ask = input("Do you want to check this code challenge (yes/no) : ")
            if ask.lower() == "no":
                print("Thankyou for checking")
                print(input("Press the ENTER to return to the menu"))
                codechallenges(user2)
            elif choice.lower() == "yes":
                print("Please answer the following")
            print("WELCOME TO OUR BANK PROGRAM")

            name = input("\nPlease Enter your Fullname: ")
            print(f"\nHello Welcome to our bank {name}")

            def ask_yes_no(question):
                while True:
                    response = input(question).lower()
                    if response == "yes" or response == "no":
                        return response
                    else:
                        print("Just answer with yes or no.")

            isapplying = ask_yes_no("\nDo you want to make a Bank Account? : ")

            if isapplying == "no":
                print("Thank you for your time.")
                exit()  

            if isapplying == "yes":
                print("\nLet me help you create a bank account.")
                isreq = ask_yes_no("\nAre you sure you want to create a Bank Account?: ")
                if isreq == "no":
                    print("Thank you for your time.")
                    exit()  
                elif isreq == "yes":
                    print("\nPlease fill in the information below.")
            else:
                print("Invalid response. Exiting the program.")
                exit()

            accounts = {}

            def create_account():
                username = input("Enter a username: ")
                password = input("Enter your password: ")
                if username in accounts:
                    print("Account already exists!")
                    if password in  accounts:
                        print("this password have been used")
                        
                else:
                    accounts[username] = 0
                    print(f"Account created successfully for {username}.")
                    accounts[password] = 0
                    print(f"password have been created successfully {password}.")


            def deposit():
                username = input("Enter your username: ")
                if username in accounts:
                        password = input("Enter your password: ")
                if password in accounts:
                    try:
                        amount = int(input("Enter amount to deposit : "))
                        if amount > 0:
                            accounts[username] += amount
                            print(f"Deposited {amount} successfully. New balance: {accounts[username]}")
                            denomination(amount)
                        else:
                            print("Amount must be positive!")
                    except ValueError:
                        print("Invalid input! Please enter a whole number.")
                else:
                    print("Account not found!")


            def withdrawal():
                username = input("Enter your username: ")
                if username in accounts:
                    password = input("Enter your password: ")
                if password in accounts:
                    try:
                        amount = int(input("Enter amount to withdraw (whole numbers only): "))
                        if 0 < amount <= accounts[username]:
                            accounts[username] -= amount
                            print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[username]}")
                            denomination(amount)
                        else:
                            print("Insufficient funds or invalid amount!")
                    except ValueError:
                        print("Invalid input! Please enter a whole number.")
                else:
                    print("Account not found!")


            def check_balance():
                username = input("Enter your username: ")
                if username in accounts:
                    print(f"Your balance: {accounts[username]}")
                
                else:
                    print("Account not found!")
            def denomination(amount):
                print("\nDenomination Breakdown:")
                A = amount // 1000
                AA = amount % 1000

                B = AA // 500
                BB = AA % 500

                C = BB // 200
                CC = BB % 200

                D = CC // 100
                DD = CC % 100

                E = DD // 50
                EE = DD % 50

                F = EE // 20
                FF = EE % 20

                G = FF // 10
                GG = FF % 10

                H = GG // 5
                HH = GG % 5

                I = HH // 1

                print("1000---", A)
                print("500----", B)
                print("200----", C)
                print("100----", D)
                print("50-----", E)
                print("20-----", F)
                print("10-----", G)
                print("5------", H)
                print("1------", I)




            def options():
                while True:
                    print("\nPlease follow this instructions.")
                    print("\nBanking System")
                    print("1. Create Account")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Check Balance")
                    print("5. Exit")
                    choice = input("Choose an option (1-5): ")


                    if choice == '1':
                        create_account()
                    elif choice == '2':
                        deposit()
                    elif choice == '3':
                        withdrawal()
                    elif choice == '4':
                        check_balance()
                    elif choice == '5' or "Exit":
                        print("Thank you for using the Banking System!")
                        break
                    else:
                        print("Invalid option. Please try again.")
                        print(input("Press ENTER"))

            options()
        else:
            print("Please enter a valid choice.")

                    







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


        