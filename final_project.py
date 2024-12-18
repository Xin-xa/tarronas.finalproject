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
    print("1. Lessons\n\n2.Terminal\n\n3. Activities\n\n4. Code Challenges\n\n5. Exit")
    while loop:
        choice = input("Please Enter the topic you want to explore (1/2/3/4/5): ")

        if choice.lower() == "1":
            lessons(user)
        elif choice.lower() == "2":
            terminal(user)
        elif choice.lower() == "3":
            activities(user)
        elif choice.lower() == "4":
            codechallenges(user)
        elif choice.lower() == "5":
            print("Thank you for using the system!")
            exit()
        else:
            print("Please enter a valid choice.")
        
##########################################################################################################################################################################
def terminal(user):
    os.system("cls")
    """First Menu Option [TERMINAL]."""
    print("\nTERMINAL MENU")
    print("1. Description\n\n2. Navigation\n\n3. Commands/Functions\n\n4. Back to Main Menu")
    while loop:
        choice = input("Please Enter the number of the topic you want to explore(1/2/3/4): ")
        if choice.lower() == "4":
            os.system("cls")
            menu(user)
        elif choice.lower() == "1":
            os.system("cls")
            print("\nThe Terminal is a modern interface for various shells like cmd, PowerShell, Linux, Python, etc. \n")
            print("A command line or terminal is a text-based interface used to interact with a computer. Unlike graphical user interfaces (GUIs) that rely on visual elements like icons and buttons, command lines allow users to type specific commands to perform tasks.")
            input("Press ENTER to continue...")
            terminal(user)
        elif choice.lower() == "2":
            os.system("cls")
            print("\n\nTo navigate through files using the terminal, use commands like \n\n 'md' (Make Directory) \n\n 'cd' (Change Directory) \n\n 'dir' (Show current location files). \n\n 'type nul > filename.ext' to create a new files. \n\n")
            input("Press ENTER to continue...")
            terminal(user)

        elif choice.lower() == "3":
            os.system("cls")
            print("\nCommand Keywords:")
            print("- dir: Displays a list of files and directories.")
            print("- md: Creates a new directory.")
            print("- cd: Changes the current directory.")
            print("- type nul > filename: Creates a new file.")
            input("Press ENTER to continue...")
            terminal(user)
        elif choice.lower() == "4":
            print("Thankyou for Using my system")
            print(input("Press ENTER to return to menu"))
            terminal(user)
#########################################################################################################################################################        
def codechallenges(user2):
    import os
    """Code Challenges Placeholder"""
    print("This is the list of the code challenge")
    print("1. code_challenge1\t\t11. code_challenge11\n\n2. code_challenge2\t\t12. code_challenge12\n\n3. code_challenge3\t\t13. code_challenge13\n\n4. code_challenge4\t\t14. code_challenge14\n\n5. code_challenge5\t\t15. code_challenge15\n\n6. code_challenge6\t\t16. code_challenge16\n\n7. code_challenge7\t\t17. exit\n\n8. code_challenge8\n\n9. code_challenge9\n\n10. code_challenge10")
    while loop:
        choice = input("\nPlease select the Code challenge that you want to explore (enter the number 1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17): ")
        if choice == "17":
            os.system("cls")
            print("Thankyou for checking the list of my code challenge")
            input("Press ENTER to return to the menu...")
            menu(user)
################################################################################################################################   
        elif choice == "1":
            os.system("cls")
            while loop:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask.lower() == "no":
                    print("Thankyou for checking")
                    codechallenges(user2)
                elif ask.lower() == "yes":
                    print (" \t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\b*** \n\t\t\t\t\t\t\t\t\t\t\b\b***** \n\t\t\t\t\t\t\t\t\t\t\b\b\b******* \n\t\t\t\t\t\t\t\t\t\t\b\b***** \n\t\t\t\t\t\t\t\t\t\t\b*** \n\t\t\t\t\t\t\t\t\t\t* \n ") 
                    print(input("Press ENTER to return to the menu..."))
                    codechallenges(user2)
                else:
                    print("Please enter a valid choice.")
################################################################################################################################   
        elif choice == "2":
            os.system("cls")
            while loop:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask.lower() == "no":
                    print("Thankyou for checking")
                    codechallenges(user2)
                elif ask.lower() == "yes":
                    name = input ("What is your name: ")
                    print(" \t\t\t\t\t\t\t\t\t\t   *\n\n\t\t\t\t\t\t\t\t\t\t\b\b  *  *  *  \n\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b *  *  *  *  * \n\t\t\t\t\t\t\t\t\t\t\b\b\b-------------\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b* |   Hi! "+name+"  | *\n\t\t\t\t\t\t\t\t\t\t\b\b\b------------- \n\t\t\t\t\t\t\t\t\t\t\b\b\b*  *  *  *  *  \n\n\t\t\t\t\t\t\t\t\t\t\b\b  *  *  *  \n\n\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b*")
                    print(input("Press ENTER to return to the menu..."))
                    codechallenges(user2)
                else:
                    print("Please enter a valid choice.")
################################################################################################################################   
        elif choice == "3":
            os.system("cls")
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
################################################################################################################################   
        elif choice == "4":
            os.system("cls")
            while True:  
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking")
                    input("Press ENTER to return to the menu...")
                    codechallenges(user2)  
                    break  
                elif ask.lower() == "yes":
                    print("Please give an answer to the following")
                    number1 = int(input("Enter a number: "))
                    number2 = int(input("Enter another number: "))

                    add = number1 + number2
                    minus = number1 - number2
                    multiply = number1 * number2
                    divide = number1 / number2
                    exp = number1 ** number2
                    mod = number1 % number2
                    floordiv = number1 // number2

                    print("The sum of", number1, "and", number2, "is", add)
                    print("The difference of", number1, "and", number2, "is", minus)
                    print("The product of", number1, "and", number2, "is", multiply)
                    print("The quotient of", number1, "and", number2, "is", divide)
                    print("The exponent of", number1, "and", number2, "is", exp)
                    print("The remainder of", number1, "and", number2, "is", mod)
                    print("The floor division of", number1, "and", number2, "is", floordiv)
                    input("Press ENTER to return to the menu...")
                    codechallenges(user2) 
                else:
                    print("Please enter a valid choice.")
################################################################################################################################   
        elif choice == "5":
            os.system("cls")
            while True:  
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking.")
                    input("Press ENTER to return to the menu...")
                    codechallenges(user2)  
                    break  
                elif ask.lower() == "yes":
                    print("Please give an answer to the following.")
                    print("Hi, Welcome to my Bank Deposit, PH Denomination Program!")

                    name = input("Please enter your name: ")
                    try:
                        deposit = eval(input("Enter the amount you want to deposit: "))

                        if deposit < 0:
                            print("Deposit amount cannot be negative. Please try again.")
                            continue

                        print(f"Hi {name}, thank you! Here is the breakdown of the deposited amount:")

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

                        print(f"{libo} - 1,000 PHP")
                        print(f"{five_h} - 500 PHP")
                        print(f"{two_h} - 200 PHP")
                        print(f"{one_h} - 100 PHP")
                        print(f"{fifty} - 50 PHP")
                        print(f"{twenty} - 20 PHP")
                        print(f"{ten} - 10 PHP")
                        print(f"{five} - 5 PHP")
                        print(f"{one} - 1 PHP")
                        input("Press ENTER to return to the menu...")
                        codechallenges(user2) 
                    except Exception as e:
                        print(f"Error: {e}. Please enter a valid amount.")
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "6":
            os.system("cls")
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
            
                        prelim = eval(input("Enter your Prelim Grade: "))
                        midterm = eval(input("Enter your Midterm Grade: "))
                        sfinals = eval(input("Enter your Semi Finals Grade: "))
                        finals = eval(input("Enter your Finals Grade: "))
                        quiz = eval(input("Enter your Quiz Grade: "))
                        project = eval(input("Enter your Project Grade: "))

                      
                        if all(65 <= grade <= 100 for grade in [prelim, midterm, sfinals, finals, quiz, project]):
                            average_grade = (prelim + midterm + sfinals + finals + quiz + project) / 6
                            print(f"Your average grade is: {average_grade:.2f}")

                            FG = (
                                (prelim * 0.15)
                                + (midterm * 0.15)
                                + (sfinals * 0.15)
                                + (finals * 0.15)
                                + (quiz * 0.25)
                                + (project * 0.15)
                            )

                            if FG >= 75:
                                print(f"Your Final Grade is: {FG:.2f}")
                                print("Congratulations, you passed the course/subject!")
                            else:
                                print(f"Your Final Grade is: {FG:.2f}")
                                print("Sorry, you failed.")
                                print("Better luck next time!")
                        else:
                            print("INVALID GRADE: All grades must be between 65 and 100.")
                    except Exception as e:
                        print(f"Error: {e}. Please enter valid numeric grades.")

                    input("Press ENTER to return to the menu...")
                    codechallenges(user2)
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "7":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu.")
                    codechallenges(user2)
                    break
                elif ask.lower() == "yes":
                    print("Grocery Challenge")

                    name = input("Enter your name: ")
                    grocery_purchase = input("Did you purchase grocery today (yes/no): ")

                    if grocery_purchase.lower() == 'yes':
                        print(f"\nWelcome {name} to the Counter\n")

                        item_name = input("What item did you purchase: ")
                        try:
                            item_price = float(input("Item price: "))
                        except ValueError:
                            print("Invalid input for price. Please enter a number.")
                            continue

                        age = input("Enter your age: ")
                        if not age.isnumeric():
                            print("Invalid input. Age must be a number.")
                            continue
                        else:
                            age = int(age)
                            print("Age validated successfully.")

                        
                        payment_amount = float(input("Enter payment amount: "))
                        tax = item_price * 0.123  
                        senior_discount = item_price * 0.052 if age >= 60 else 0
                        total_price = item_price + tax - senior_discount

                       
                        change = payment_amount - total_price

                       
                        print("\nHere is your receipt:\n")
                        print(f"Item: {item_name}")
                        print(f"Item price: {item_price:.2f}")
                        print(f"Tax (12.3%): {tax:.2f}")
                        print(f"Senior discount: {senior_discount:.2f}")
                        print(f"Total price: {total_price:.2f}")
                        print(f"Payment: {payment_amount:.2f}")
                        print(f"Your change: {change:.2f}")
                        print("\nThank you for your purchase!\n")

                    else:
                        print(f"No grocery purchase today, {name}. Have a nice day!\n")

                    input("Press ENTER to return to menu.")
                    codechallenges(user2)
                    break
                else:
                    print("Invalid choice. Please answer 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "8":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break  
                elif ask.lower() == "yes":
                    print("Please answer the following.")
                    
                    try:
                        num = int(input("Enter a number: "))
                        if num < 0:
                            print("Factorial is not for negative numbers.")
                        else:
                            factorial = 1
                            for jhed in range(num, 0, -1):
                                factorial *= jhed

                            print(f"The factorial of {num} is {factorial}.")
                    except ValueError:
                        print("Please enter a valid number.")
                    
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break 
                else:
                    print("INVALID CHOICE. Please enter 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "9":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break 
                elif ask.lower() == "yes":
                    print("Please answer the following")
                    try:
                        j = int(input("Give a number: "))
                        for x in range(j, 0, -1):  
                            for y in range(j, x, -1): 
                                print(" ", end=" ")
                            print("* " * x)  

                    except ValueError:
                        print("Please enter a valid number.")
                    
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break  
                else:
                    print("INVALID CHOICE. Please enter 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "10":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break  
                elif ask.lower() == "yes":
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
                        print() 
                    
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break 
                else:
                    print("INVALID CHOICE. Please enter 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "11":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break  
                elif ask.lower() == "yes":
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

                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break  
                else:
                    print("INVALID CHOICE. Please enter 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "12":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break 
                elif ask.lower() == "yes":
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
                            print(" ", end=" ")
                        for z in range(3, 4):  
                            print("*", end=" ")
                        for a in range(4, 0, -1):  
                            print("*", end=" ")
                        print()  #

                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break 
                else:
                    print("INVALID CHOICE. Please enter 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "13":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break  
                elif ask.lower() == "yes":
                    print("Please answer the following")

                    for x in range(1, 7):
                        for y in range(6, x, -1): 
                            print(" ", end=" ")
                        for z in range(x, 1, -1):  
                            print(z, end=" ")
                        for a in range(1, x + 1):  
                            print(a, end=" ")
                        print()  

        
                    for x in range(5, 0, -1):
                        for y in range(5 - x + 1):  
                            print(" ", end=" ")
                        for z in range(x, 0, -1):  
                            print(z, end=" ")
                        for a in range(2, x + 1):  
                            print(a, end=" ")
                        print()  

                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break 
                else:
                    print("INVALID CHOICE. Please enter 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "14":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break  
                elif ask.lower() == "yes":
                    print("Please answer the following")

                    go = True
                    no = 0
                    while go:
                        try:
                            num = float(input("Please Enter a number--->  "))  
                            if num == 0:
                                print("Program Terminated")
                                print(f"The total of the numbers you have given is {no}")
                                input("Press ENTER to return to the menu...")
                                codechallenges(user2)
                                break 
                            else:
                                no += num  #
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")  

                else:
                    print("INVALID CHOICE. Please enter 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "15":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no) : ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu")
                    codechallenges(user2)
                    break  # Exit the loop and return to the menu
                elif ask.lower() == "yes":
                    print("Please answer the following")
                    
                    isGo = True
                    num = 0
                    while isGo:
                        question = input("Do you want to add more Triangles ----> ")

                        if question.lower() == "no":
                            os.system("cls")  # Clear screen in Windows
                            print("Progress Terminated")
                            input("Press ENTER to return to menu....")
                            codechallenges(user2)
                            break  # Exit the inner loop when user chooses "no"

                        elif question.lower() == "yes":
                            os.system("cls")  # Clear screen
                            num += 1
                            for x in range(1, 6):  # Loop for rows
                                for y in range(1, num + 1):  # Loop to repeat triangles
                                    for r in range(1, x + 1):  # Loop for triangle height
                                        print("^", end=" ")
                                    for z in range(5, x, -1):  # Loop for spacing
                                        print(" ", end=" ")
                                    print(" ", end=" ")
                                print()  # Print a new line after each triangle
                        else:
                            os.system("cls")
                            print("Please answer only with 'Yes' or 'No'")  # Handle invalid input
                else:
                    print("INVALID CHOICE. Please enter 'yes' or 'no'.")
################################################################################################################################   
        elif choice == "16":
            os.system("cls")
            import os
            def ask_yes_no(question):
                while True:
                    response = input(question).lower()
                    if response == "yes" or response == "no":
                        return response
                    else:
                        print("Just answer with yes or no.")

            def create_account(accounts, passwords):
                username = input("Enter a username: ")
                if username in accounts:
                    print("Account already exists!")
                else:
                    password = input("Enter your password: ")
                    accounts[username] = 0  # Initial balance is 0
                    passwords[username] = password  # Store password separately
                    print(f"Account created successfully for {username}.")

            def deposit(accounts, passwords):
                username = input("Enter your username: ")
                if username in accounts:
                    password = input("Enter your password: ")
                    if passwords.get(username) == password:
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
                        print("Incorrect password!")
                else:
                    print("Account not found!")

            def withdrawal(accounts, passwords):
                username = input("Enter your username: ")
                if username in accounts:
                    password = input("Enter your password: ")
                    if passwords.get(username) == password:
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
                        print("Incorrect password!")
                else:
                    print("Account not found!")

            def check_balance(accounts):
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

            def options(accounts, passwords):
                while True:
                    print("\nBanking System")
                    print("1. Create Account")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Check Balance")
                    print("5. Exit")
                    choice = input("Choose an option (1-5): ")

                    if choice == '1':
                        create_account(accounts, passwords)
                    elif choice == '2':
                        deposit(accounts, passwords)
                    elif choice == '3':
                        withdrawal(accounts, passwords)
                    elif choice == '4':
                        check_balance(accounts)
                    elif choice == '5':
                        print("Thank you for using the Banking System!")
                        break  # Exit the options menu
                    else:
                        print("Invalid option. Please try again.")

            def bank_program():
                accounts = {}
                passwords = {}  

                while True:
                    ask = input("Do you want to check this code challenge (yes/no) : ")
                    if ask.lower() == "no":
                        print("Thank you for checking!")
                        input("Press ENTER to return to the menu")
                        break  
                    elif ask.lower() == "yes":
                        print("WELCOME TO OUR BANK PROGRAM")
                        name = input("\nPlease Enter your Fullname: ")
                        print(f"\nHello, Welcome to our bank {name}")

                        isapplying = ask_yes_no("\nDo you want to make a Bank Account? : ")

                        if isapplying == "no":
                            print("Thank you for your time.")
                            break 

                        if isapplying == "yes":
                            print("\nLet me help you create a bank account.")
                            isreq = ask_yes_no("\nAre you sure you want to create a Bank Account?: ")
                            if isreq == "no":
                                print("Thank you for your time.")
                                break 
                            elif isreq == "yes":
                                print("\nPlease fill in the information below.")
                                options(accounts, passwords)

                    else:
                        print("Invalid response. Exiting the program.")
                        break  

            bank_program()
#####################################################################
def activities(user1):
    os.system("cls")
    """Activities Placeholder"""
    print("\nSecond MAIN MENU Option")
    print("LIST OF ACTIVITIES")
    print("1. Activity1\t\t11. Activity11\t\t21. Activity21\n\n2. Activity2\t\t12. Activity12\t\t22. Activity22\n\n3. Activity3\t\t13. Activity13\t\t23. Activity23\n\n4. Activity4\t\t14. Activity14\t\t24. Activity24\n\n5. Activity5\t\t15. Activity15\t\t25. Activity25\n\n6. Activity6\t\t16. Activity16\t\t26. Activity26\n\n7. Activity7\t\t17. Activity17\n\n8. Activity8\t\t18. Activity18\n\n9. Activity9\t\t19. Activity19\n\n10. Activity10\t\t20. Activity20\n")                
    while True:
        choice = input("Please Enter the number of the activities that you want to explore: ")
        if choice == "26":
            os.system("cls")
            print(f"Thankyou for checking this activity {user}")
            input("Press ENTER to return to the menu....")
            menu(user)
        elif choice == "1":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    print(input("Press ENTER to return to the menu...."))
                    activities(user1)  
                    break 
                elif ask.lower() == "yes":  
                    print("Hello World")
                    name = input("Please Enter your Name: ")
                    print("Hi " + name)
                    input("Press ENTER to return to the menu...")  
                    activities(user1)
                    break  
                else:
                    print("Invalid input. Please answer with 'yes' or 'no'.")
####################################################################################################################
        elif choice == "2":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    print(input("Press ENTER to return to the menu...."))
                    activities(user1)  
                    break 
                elif ask.lower() == "yes":  
                    num1 = eval(input("Please Enter the First Number: "))
                    num2 = eval(input("Please Enter the Second Number: "))
                    answer = num1 + num2
                    print(num1, "+" , num2 , "=" , answer)
                    print(input("Press ENTER to return to the menu"))
                    activities(user1)
                else:
                    print("Invalid input. Please answer with 'yes' or 'no'.")
    #####################################################################################################################################################
        elif choice == "3":
            os.system("cls")
            while True:
                background = input("Are you sure you want to answer the survey (yes / no): ")
                if background.lower() == "no":  
                    print("Thank you for checking this activity.")
                    activities(user1)
                    break  
                
                elif background.lower() == "yes":
                    print("\nThis is a survey for your background.")
                    print("Please answer the following questions:\n")
                    
                    # Collect user input
                    fullname = input("PLEASE INPUT YOUR FULL NAME: ")
                    birthDay = input("PLEASE INPUT YOUR BIRTHDAY (day): ")
                    birthMonth = input("PLEASE INPUT YOUR BIRTHMONTH: ")
                    birthYear = input("PLEASE INPUT YOUR BIRTHYEAR: ")
                    placeofbirth = input("INPUT YOUR PLACE OF BIRTH: ")
                    age = input("PLEASE INPUT YOUR AGE: ")
                    gender = input("PLEASE INPUT YOUR GENDER: ")
                    nationality = input("PLEASE INPUT YOUR NATIONALITY: ")
                    fname = input("PLEASE INPUT YOUR FATHER'S NAME: ")
                    religion = input("PLEASE INPUT YOUR RELIGION: ")
                    status = input("PLEASE INPUT YOUR STATUS: ")
                    fulladdress = input("PLEASE INPUT YOUR FULL ADDRESS: ")
                    cellphone = input("PLEASE INPUT YOUR CONTACT NUMBER: ")
                    email = input("PLEASE INPUT YOUR EMAIL ADDRESS: \n")

                   
                    print("\nSurvey Summary:")
                    print(f"Hi! My name is {fullname}, I was born on {birthMonth} {birthDay}, {birthYear} at {placeofbirth}.")
                    print(f"I'm {age} years old, {gender}, and I am a {nationality}.")
                    print(f"My father's name is {fname}. I am a {religion} and currently {status}.")
                    print(f"I reside at {fulladdress}, and you can reach me by cellphone at {cellphone} or via email at {email}.\n")

                    input("Press ENTER to return to the menu...")  # Pause before returning
                    activities(user1)
                    break 

                else:  
                    print("Invalid input. Please answer with 'yes' or 'no'.\n")
    ######################################################################################################################################################  
        elif choice == "4":
            os.system("cls")
            while True:
                background2 = input("Do you want to run this Activity (yes/no): ")
                
                if background2.lower() == "yes":
                    print("\nPlease fill in the following:")
                    try:
                        number1 = int(input("Enter a number: "))
                        number2 = int(input("Enter another number: "))

                        add = number1 + number2
                        minus = number1 - number2
                        multiply = number1 * number2
                        divide = number1 / number2
                        exp = number1 ** number2
                        mod = number1 % number2
                        floordiv = number1 // number2

                        print("\nResults:")
                        print(f"The sum of {number1} and {number2} is {add}")
                        print(f"The difference of {number1} and {number2} is {minus}")
                        print(f"The product of {number1} and {number2} is {multiply}")
                        print(f"The quotient of {number1} and {number2} is {divide}")
                        print(f"The exponent of {number1} to {number2} is {exp}")
                        print(f"The remainder of {number1} divided by {number2} is {mod}")
                        print(f"The floor division of {number1} by {number2} is {floordiv}")

                    except ValueError:
                        print("Invalid input! Please enter valid numbers.")

                    print("\nPress ENTER to return to the menu...")
                    input()
                    activities(user1)
                    break

                elif background2.lower() == "no":
                    print("Thank you for checking this activity!!")
                    activities(user1)
                    break

            else:
                print("INVALID CHOICE! Please answer with 'yes' or 'no'.")
####################################################################################################################
        elif choice == "5":
            os.system("cls")
            while True:
                background = input("Are you sure you want to answer the survey (yes / no): ").lower()
                
                if background.lower() == "no":  
                    print("Thank you for checking this activity.")
                    activities(user1)
                    break  

                elif background.lower() == "yes":  
                    print("\nFAHRENHEIT to CELSIUS CONVERTER")
                    try:
                        temp = float(input("Enter temperature in Fahrenheit: "))
                        celsius = (temp - 32) * 5 / 9
                        print(f"\nThe conversion of {temp}° Fahrenheit is {round(celsius, 2)}° Celsius.")
                        input("\nPress ENTER to return to the menu...")
                        activities(user1)
                        break
                    except ValueError:
                        print("Invalid input! Please enter a valid number.")
                
                else:
                    print("INVALID CHOICE! Please answer with 'yes' or 'no'.")
##################################################################################################################################
        elif choice == "6":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ").lower()
                
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                
                elif ask.lower() == "yes":
                    print("\nArithmetic Operations Example:\n")
                    
                    x = 10
                    print(f"x = {x}")

                    a = x + 10
                    print(f"x + 10 = {a}")

                    c = 100
                    c += 100
                    print(f"c += 100: {c}")

                    d = 100
                    d -= 100
                    print(f"d -= 100: {d}")

                    e = 100
                    e *= 100
                    print(f"e *= 100: {e}")

                    f = 100
                    f /= 100
                    print(f"f /= 100: {f}")

                    g = 100
                    g //= 100
                    print(f"g //= 100: {g}")

                    h = 100
                    h **= 1
                    print(f"h **= 1: {h}")

                    i = 100
                    i %= 100
                    print(f"i %= 100: {i}")

                    input("\nPress ENTER to return to the menu....")
                    activities(user1)
                    break
                else:
                    print("Invalid Choice! Please answer with 'yes' or 'no'.")
########################################################################################################################
        elif choice == "7":
            os.system("cls")
            while True:
                gold = 0  # Initial gold count
                miner = input("Hi, please enter your name: ")
                while True:
                    has_mine = input("Did you mine something today? (yes/no): ")
                    if has_mine.lower() == "no":
                        print(f"Hi {miner}, please mine some gold! :)")
                        break  
                    elif has_mine.lower() == "yes":
                        gold += 1_000_000_000
                        print(f"Hi {miner}, today you have a total of {gold} gold.")
                        print(input("Press ENTER to return to the menu..."))
                        activities(user1)
                    else:
                        print("Invalid input. Please answer with 'yes' or 'no'.")
##########################################################################################################################################
        elif choice == "8":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)  
                    break
                elif ask.lower() == "yes":
                    password = input("Please enter your password: ")
                    
                    if password.lower() == "secret":
                        print("Access Granted")
                        print("Welcome to the System")
                        print("Enjoy using the System")
                        print(input("Press ENTER to return to the menu..."))
                        activities(user1)
                    else:
                        print("Access Denied!")
                        print("Thank you for using the System!")  
                else:
                    print("INVALID CHOICE! Please answer with 'yes' or 'no'.")
############################################################################################################################
        elif choice == "9":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                elif ask.lower() == "yes":
                    try:
                        Age = int(input("Enter your Age: "))
                        if Age >= 0 and Age <= 7:
                            print("You are a Toddler")
                        elif Age > 7 and Age <= 13:
                            print("You are a Pre-Teen")
                        elif Age > 13 and Age <= 18:
                            print("You are a Teenager")
                        elif Age > 18 and Age <= 31:
                            print("You are an Early Adult")
                        elif Age > 31 and Age <= 45:
                            print("You are a Mid Adult")
                        elif Age > 45 and Age <= 59:
                            print("You are a Past Adult")
                        elif Age > 59 and Age <= 120:
                            print("You are a Senior")
                        else:
                            print("Please Input a Valid Number")
                    except ValueError:
                        print("Invalid input! Please enter a valid number.")
                else:
                    print("Please answer with 'yes' or 'no'.")
###########################################################################################################################################
        elif choice == "10":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)  
                    break
                elif ask.lower() == "yes":
                    print("DLL Free BSIT Scholarship Form\n")
                    isDLL = input("Are you a current student of DLL (yes/no): ")
                    if isDLL.lower() == "yes":
                        print("Welcome to our system")
                    elif isDLL.lower() == "no":
                        print("Sorry, but this is for DLL students only!")
                        input("Press ENTER to return to menu")
                        activities(user1)
                        break  
                    isIT = input("Are you interested in taking the course of Bachelor of Science in Information Technology (yes/no): ")
                    if isIT.lower() == "yes":
                        print("Welcome, Future IT Student!")
                    elif isIT.lower() == "no":
                        print("Sorry, but this scholarship is for IT students only!")
                        input("Press ENTER to return to menu")
                        activities(user1)
                        break
                    isGG = input("Are you from Brgy. Gulang - Gulang (yes/no): ")
                    if isGG.lower() == "yes":
                        print("Please fill up the second form.")
                    else:
                        print("Sorry, this scholarship is only available for residents of Gulang - Gulang.")
                        input("Press ENTER to return to menu")
                        activities(user1)
                        break  

                    isLevel = input("What is your current year level right now in DLL?\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer: ")
                    if isLevel.lower() == "f":
                        print("Hi, Freshman!")
                    elif isLevel.lower() == "s":
                        print("Hi, Sophomore!")
                    elif isLevel.lower() == "j":
                        print("Hi, Junior!")
                    elif isLevel.lower() == "r":
                        print("Hi, Senior!")
                    else:
                        print("Invalid choice. Please enter a valid year level.")
                        continue  

                    isNeeded = input("Do you need this scholarship? (yes/no): ")
                    if isNeeded.lower() == "yes":
                        print("Scholarship Granted!")
                        print(input("Press ENTER to return to the menu..."))
                        activities(user1)
                    else:
                        print("Thank you for stopping by!")
                    print("Thank you for stopping by!")
                    break 
                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")
#####################################################################################################################################################
        elif choice == "11":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                elif ask.lower() == "yes":
                    for x in range(1, 11):
                        print(x, "Hello World")
                        print("Happy Foundation Day")
                        name = input("Hi, what is your name: ")
                        print(f"Hi {name}!")
                        continue_prompt = input("Do you want to continue? (yes/no): ")
                        if continue_prompt.lower() == "no":
                            print("Thank you for participating!")
                            input("Press ENTER to return to the menu....")
                            activities(user1)  
                            break
                    break  
                else:
                    print("Invalid input. Please answer with 'yes' or 'no'.")
#################################################################################################################################################
        elif choice == "12":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ").lower()
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1) 
                    break
                elif ask.lower() == "yes":
                    print("Starting the countdown from 10 to 2:")
                    for x in range(10, 1, -1):
                        print(f"\t\t\t\t\t{x}")
                    print("\nCountdown complete!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")
################################################################################################################################
        elif choice == "13":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1) 
                    break
                elif ask.lower() == "yes":
                    try:
                        num1 = int(input("Enter any non-negative integer: "))
                        if num1 < 0:
                            print("Factorial is not defined for negative numbers. Please try again.")
                            continue 
                        factorial = 1
                        for i in range(num1, 0, -1):
                            factorial *= i
                        print(f"The factorial of {num1} is {factorial}")
                        input("Press ENTER to return to the menu....")
                        activities(user1)
                        break
                    except ValueError:
                        print("Invalid input! Please enter a valid integer.")
                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")
############################################################################################################################
        elif choice == "14":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ").lower()
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1) 
                    break
                elif ask.lower() == "yes":
                    print("Welcome to the Code Challenge for Choice 14!")
                    try:
                        num = int(input("Enter a positive integer: "))
                        if num < 2:
                            print(f"{num} is not a prime number.")
                        else:
                            is_prime = True
                            for i in range(2, int(num ** 0.5) + 1):
                                if num % i == 0:
                                    is_prime = False
                                    break
                            if is_prime:
                                print(f"{num} is a prime number.")
                            else:
                                print(f"{num} is not a prime number.")
                    except ValueError:
                        print("Invalid input! Please enter a valid positive integer.")
                    
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")
##################################################################################################################################################
        elif choice == "15":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                elif ask.lower() == "yes":
                    print("Generated Pattern:")
                    for x in range(0, 21):  
                        print(x, end=" ") 
                        for y in range(0, x):  
                            print("*", end=" ")  
                        print()  
                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")

########################################################################################################################################################
        elif choice == "16":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                elif ask.lower() == "yes":
                    for a in range(1, 6):  
                        for b in range(6, a, -1): 
                            print(" ", end=" ")
                        for c in range(1, a * 2): 
                            print("*", end=" ")
                        print()  
                    print("Invalid input! Please answer with 'yes' or 'no'.")  
################################################################################################################################
        elif choice == "17":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                elif ask.lower() == "yes":
                    try:
                        col = int(input("Enter number of columns: "))
                        if col <= 0:
                            print("Please enter a positive number for columns.")
                            continue
                        for x in range(1, 11):
                            for y in range(1, col + 1):
                                print(f"{x} x {y} = {x * y}", end="\t")
                            print()  
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")  
######################################################################################################################
        elif choice == "18":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                elif ask.lower() == "yes":
                    try:
                        no = int(input("Enter number of Triangle rows: ")) 
                        for x in range(1, no + 1): 
                            for y in range(no - x):
                                print(" ", end=" ")
                            for z in range(1, 2 * x):  
                                print("*", end=" ")
                            print() 
                    except ValueError:
                        print("Please enter a valid number for the rows.")
                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")
####################################################################################################################################
        elif choice == "19":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                elif ask.lower() == "yes":
                    while True:
                        name = input('Please enter a name: ')
                        if name.lower() == "stop":
                            print("Program Terminated")
                            print(input("Press ENTER to return to menu"))
                            activities(user1)
                            break 
                        else:
                            print(f"Hello, {name}!")  
                            continue
                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")
##########################################################################################################################################
        elif choice == "20":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)  
                    break
                elif ask.lower() == "yes":
                    isContinue = True
                    no = 0
                    while isContinue:  
                        ask = input("Would you like to add another Triangle (Yes/No): ")

                        if ask.lower() == "no":
                            print('PROGRAM TERMINATED')
                            print(input("Press ENTER to return to menu"))
                            activities(user1)
                            break  
                        os.system('cls')
                        no += 1 
                        for x in range(1, 5):  
                            for r in range(1, no + 1):  
                                for y in range(1, x + 1):  
                                    print("*", end=" ")

                                for z in range(5, x, -1): 
                                    print(" ", end=" ")
                            print() 
                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")
#####################################################################################################################################
        elif choice == "21":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1) 
                    break
                elif ask.lower() == "yes":
                    nameno = 0  
                    while True:
                        name = input("Enter a name: ")

                        if name.lower() == "stop":
                            print("Okay tama na")
                            print(f"You have entered a total of {nameno} names!")
                            break 

                        else:
                            print("type 'stop' if you want to terminate the program")
                            nameno += 1 

                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")
##################################################################################################################################        
        elif choice == "22":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                elif ask.lower() == "yes":
                    loop = True
                    names = []
                    while loop:
                        askname = input("What name would you like to add (or type 'stop' to finish): ")
                        if askname.lower() == "stop":
                            print("\nNames entered:", names)
                            print(f"You have entered {len(names)} names!")
                            break
                        else:
                            names.append(askname)
                else:
                    print("Invalid input! Please answer with 'yes' or 'no'.")
###################################################################################################################################################
        elif choice == "23":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)
                    break
                elif ask.lower() == "yes":
                    def factorial (number):
                        """ This function's purpose is to compute/calculate the factorial of any number given """
                        fact = 1
                        for x in range(number, 0, -1):
                            fact *= x

                        return fact

                    print(f"THe factorial of 13 is {factorial(13)}")
#############################################################################################################################################                    
        elif choice == "24":
            os.system("cls")
            while True:
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1)  
                    break
                elif ask.lower() == "yes":
                    def factorial(number):
                        """ This function's purpose is to compute/calculate the factorial of any number given """
                        fact = 1
                        def factorial(number):
                            """ This function's purpose is to compute/calculate the factorial of any number given """
                            fact = 1
                            from activity23_test import factorial

                    print(f"the factorial of 7 is {factorial(7)} ")
                else:
                    print("Invalid choice. Please type 'yes' or 'no'.")
######################################################################################################################################
        elif choice == "25":
            while True:
                os.system("cls")
                ask = input("Do you want to check this code challenge (yes/no): ")
                if ask.lower() == "no":
                    print("Thank you for checking!")
                    input("Press ENTER to return to the menu....")
                    activities(user1) 
                    break
                elif ask.lower() == "yes":
                    fruits = ["apples", "banana", "orange", "star apple", "guyabano"]

                    print(f"Initial fruit list: {fruits}")

                    # INDEXING / INDEX - Address / Location of an item inside a list
                    #            0          1        2          3           4
                    # fruits = ["apples", "banana", "orange", "star apple", "guyabano"]

                    print(f"My favorite childhood fruit is {fruits[3]}")
                    print(f"The last item on the list is {fruits[-1]}")

                    fruits.append("longgan")
                    print(f"After appending 'longgan': {fruits}")
                    fruits.append("chico")
                    print(f"After appending 'chico': {fruits}")

                    fruits.insert(3, "papaya")
                    print(f"After inserting 'papaya' at index 3: {fruits}")

                    fruits.remove("longgan")
                    print(f"After removing 'longgan': {fruits}")

                    while True:
                        fruit = input("Do you wish to add more fruits (Yes/No): ")
                        if fruit.lower() == "no":
                            print(f"Final fruit list: {fruits}")
                            break
                        elif fruit.lower() == "yes":
                            new_fruit = input("Enter the name of the fruit to add: ")
                            fruits.append(new_fruit)
                            print(f"{new_fruit} added to the list!")
                        else:
                            print("Invalid input! Please answer with 'Yes' or 'No'.")
                            continue
                else:
                    print("Invalid choice! Please answer with 'yes' or 'no'.")
#########################################################################################################################       
def lessons(user3):
    os.system("cls")
    """First Menu Option [LESSONS]."""
    print("\nLESSONS MENU")
    print("1. Printing\n\n2.Printing with Variables\n\n3. Printing Using f-Strings for Formatted Output\n\n4. Printing with Mathematical Operations\n\n5. Printing With loops\n\n6. While loops\n\n7. String Concatenation\n\n8. Denomination\n\n9. Function Definition (def) and Return\n\n10. Exit")
    while loop:
        choice = input("Please Enter the number of the topic you want to explore (1/2/3/4/5/6/7/8/9/10): ")
        if choice.lower() == "10":
            os.system("cls")
            menu(user3)
        elif choice.lower() == "1":
            os.system("cls")
            print("Example 1: Simple Text Output")
            print("Input:")
            print("""
            # Simple printing
            print("Hello, world!")
            print("Welcome to Python coding.")
            """)
            print("Output:")
            print("Hello, world!")
            print("Welcome to Python coding.")
            print("\n")
            input("Press ENTER to continue...")
            lessons(user3)
#################################################################################################################################
        elif choice.lower() == "2":
            os.system("cls")
            print("Example 2: Printing Variables")
            print("Input:")
            print("""
            # Variables
            name = "Alice"
            age = 25

            # Printing variables
            print("Name:", name)
            print("Age:", age)
            """)
            print("Output:")
            name = "Alice"
            age = 25
            print("Name:", name)
            print("Age:", age)
            print("\n")
            input("Press ENTER to continue...")
            lessons(user3)
###########################################################################################################################################
        elif choice.lower() == "3":
            os.system("cls")
            print("Example 3: Using f-Strings for Formatted Output")
            print("Input:")
            print("""
            # Variables
            name = "Bob"
            hobby = "cycling"

            # Using f-strings
            print(f"{name} enjoys {hobby}.")
            """)
            print("Output:")
            name = "Bob"
            hobby = "cycling"
            print(f"{name} enjoys {hobby}.")
            print("\n")
            input("Press ENTER to continue...")
            lessons(user3)
############################################################################################################            
        elif choice.lower() == "4":
            os.system("cls")
            print("Example 4: Printing with Mathematical Operations")
            print("Input:")
            print("""
            # Simple math
            x = 10
            y = 5

            print("Addition:", x + y)
            print("Multiplication:", x * y)
            print(f"The result of {x} divided by {y} is {x / y}.")
            """)
            print("Output:")
            x = 10
            y = 5
            print("Addition:", x + y)
            print("Multiplication:", x * y)
            print(f"The result of {x} divided by {y} is {x / y}.")
            print("\n")
            input("Press ENTER to continue...")
            lessons(user3)
#############################################################################################################################
        elif choice.lower() == "5":
            os.system("cls")
            print("Printing with Loops")
            print("Input:")
            print("""
            # Looping through a range
            for i in range(5):
                print(f"Number: {i}")
            """)
            print("Output:")
            for i in range(5):
                print(f"Number: {i}")
            print("\n")
            print(input("Press ENTER to return to menu"))
            lessons(user3)
##############################################################################################################################
        elif choice.lower() == "6":
            os.system("cls")
            print("While Loop")
            print("Input:")
            print("""
            # While loop example
            count = 1
            while count <= 3:
                print(f"Count is: {count}")
                count += 1
            """)
            print("Output:")
            count = 1
            while count <= 3:
                print(f"Count is: {count}")
                count += 1
            print("\n\n\n")

            print("Infinite While Loop (Continuous Printing)")
            print("Input:")
            print("""
            # Infinite while loop to print continuously
            count = 1
            while True:
                print(f"Count: {count}")
                count += 1
            """)
            print("Output:")
            count = 1
            while True:
                print(f"Count: {count}")
                count += 1

                print(input("Press ENTER to return to menu"))
                lessons(user3)
##################################################################################################################################################
        elif choice.lower() == "7":
            os.system("cls")
            print("String Concatenation")
            print("Input:")
            print("""
            # Concatenating strings
            first_name = "James"
            last_name = "Bond"
            full_name = first_name + " " + last_name
            print("Full Name:", full_name)
            """)
            print("Output:")
            first_name = "James"
            last_name = "Bond"
            full_name = first_name + " " + last_name
            print("Full Name:", full_name)
            print("\n")
            print(input("Press ENTER to return to menu"))
            lessons(user3)
##############################################################################################################################################
        elif choice.lower() == "8":
            os.system("cls")
            print("Denomination (Division and Modulo)")
            print("Input:")
            print("""
            # Division and modulo
            amount = 160
            denomination = 25
            result = amount // denomination  # Whole number division (integer division)
            remainder = amount % denomination  # Remainder of division (modulo)
            print(f"{amount} divided by {denomination} gives {result} with a remainder of {remainder}.")
            """)
            print("Output:")
            amount = 160
            denomination = 25
            result = amount // denomination
            remainder = amount % denomination
            print(f"{amount} divided by {denomination} gives {result} with a remainder of {remainder}.")
            print(input("Press ENTER to return to menu"))
            lessons(user3)
##############################################################################################################################
        elif choice.lower() == "9":
            print("Function Definition (def) and Return")
            print("Input:")
            print("""
            # Defining a function with def and return
            def greet(name):
                return f"Hello, {name}!"

            # Calling the function
            greeting_message = greet('Alice')
            """)
            print("Output:")
            def greet(name):
                return f"Hello, {name}!"

            greeting_message = greet('Alice')
            print(greeting_message)  # Output: Hello, Alice!
            print("\n")

            # Function with While Loop and Return
            print("Example 15: Function with While Loop and Return")
            print("Input:")
            print("""
            # Defining a function with a while loop that uses return
            def ask_for_input():
                while True:
                    answer = input("What is the capital of France? ")
                    if answer.lower() == "paris":
                        return "Correct!"
                    else:
                        print("Incorrect, try again.")
            """)
            print("Output:")
            def ask_for_input():
                while True:
                    answer = input("What is the capital of France? ")
                    if answer.lower() == "paris":
                        return "Correct!"
                    else:
                        print("Incorrect, try again.")

            # You would interactively enter an answer when prompted, and if correct, the function will return "Correct!"
            input("Press ENTER to return to menu")  # Wait for user to press ENTER before going back to menu
            lessons(user3)  # Assuming lessons is a function defined elsewhere to go back to the main menu
################################################################################################################################
        elif choice.lower() == "10":
            print("Thankyou for Using my system")
            print(input("Press ENTER to return to menu"))
            lessons(user3)
        else:
            print("Invalid input. Please enter a valid choice.")  
# Main program loop
while loop:
    start = input("\nWould you like to use the system? (yes / no): ")
    if start.lower() == "yes":
        user = input("What's your name: ")
        menu(user)
    elif start.lower() == "no":
        print("Thank you for using the system!")
        break
    else:
        print("Please enter a valid choice.")