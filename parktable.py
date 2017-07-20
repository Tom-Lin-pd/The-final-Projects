#WARNING: Changing anything in the script will result making the program look ugly :P

#This is a following programm that has example about you are going to learn

import time
#This will import time to your programm so you can make your programm run at the correct second

money1 = "$5/$7" #This contains the amount of money you will pay 
money2 = "$9/$12"
money3 = "$15/$17"
money4 = "$18/$20"
money5 = "$20/$23"
list1 = "Creek Side", "Val Vista", "Fairlands" #This contains the parks in Pleasanton
list2 = "Emerald Glen", "Bray Commons", "Shannon" #This contains parks in Dublin
list3 = "Joaquin Miller", "Cleveland Cascade", "Grove Shafter" #This contains parks in Oakland
list4 = "Golden Gate", "Mission Dolares", "Buena Vista" #This contains parks in San Fransisco
emailid = "Please type in your email so we can give you your payment instructions" #This contains the email instructions

print("Hello there!")
print("")
time.sleep(1) 
print(" __      __         .__")
print("/  \    /  \  ____  |  |    ____    ____    _____    ____  ")
print("\   \/\/   /_/ __ \ |  |  _/ ___\  /  _ \  /     \ _/ __ \ ")
print(" \        / \  ___/ |  |__\  \___ (  <_> )|  Y Y  \ \  ___/ ")
print("  \__/\  /   \___  >|____/ \___  > \____/ |__|_|  / \___  >")
print("       \/        \/            \/               \/      \/ ")
print('')
print("To Upolies Tables")
time.sleep(1)
print('Book a table')
print('')
time.sleep(1)
print("Do you want to book a table in Pleasanton parks? (yes or no)")
if input() == "yes":
    time.sleep(1)
    print('Loading...')
    time.sleep(4)
    print("This the list of parks in Pleasanton: ", list1)
    print('Pick a park')
    park = input()
    print("We are booking your table at " +park+ " park")
    time.sleep(1)
    print("How many # of table? (one, two, or three)")
    if input() == "one":
        print("The price is: ", money1)
    else:
        print("The price is: ", money2)
    print(emailid)
    email = input()
    time.sleep(1)
    print("We have sent instructions to your email at: " +email+ "")
    print('')
    time.sleep(0.5)
    print("Thank you")
else: 
    time.sleep(1)
    print("Loading more places...")
    print("Do you want to book a table in Dublin? (yes or no)")
    if input() == "yes":
        time.sleep(1)
        print("Loading...")
        time.sleep(4)
        print("This is the list of parks in Dublin: ", list2)
        print('Pick a Park')
        park2 = input()
        time.sleep(1)
        print("Okay we are booking your table at: " +park2+ " park")
        time.sleep(1)
        print("How many # of table? (one, two, or three)")
        if input() == "one":
            print("The price is: ", money1)
        else:
            print("The price is: ", money3)
        print(emailid)
        email2 = input()
        time.sleep(1)
        print("We have sent instructions to your email at: " +email2+ "")
        print('')
        time.sleep(0.5)
        print("Thank you")
    else:
        print("Loading More Places...")
        time.sleep(4)
        print("Do you want to book a table in Oakland's park? (yes or no)")
        if input() == "yes":
            time.sleep(0.5)
            print("Loading...")
            time.sleep(3)
            print("This is a list of parks in Oakland: ", list3)
            print("Pick a park")
            park3 = input()
            print("We are booking you a table at " +park3+ " park")
            time.sleep(1)
            print("How many # of table? (one, two, or three)")
            if input() == "one":
                print("The price is: ", money2)
            else:
                print("The price is: ", money4)
            print(emailid)
            email2 = input()
            time.sleep(1)
            print("We have sent instructions to your email at: " +email2+ "")
            print('')
            time.sleep(0.5)
            print("Thank you")
        else:
            print("There are no more cities or parks near your location.")
            time.sleep(1)
            print("Do you want to see more cities 1 hour away from your location? (yes or no)")
            if input() == "yes":
                time.sleep(1)
                print("Loading...")
                time.sleep(4)
                print("Do you want to book a table in San Fransico's Parks? (yes or no)")
                if input() == "yes":
                    time.sleep(1)
                    print("Loading...")
                    time.sleep(3)
                    print("This is a list of parks in San Fransico: ", list4)
                    print("Pick a Park")
                    park4 = input()
                    print("We are booking a park at " +park4+ " park")
                    time.sleep(1)
                    print("How many # of table? (one, two, or three)")
                    if input() == "one":
                        print("The price is: ", money3)
                    else:
                        print("The price is: ", money5)
                    print(emailid)
                    email2 = input()
                    time.sleep(1)
                    print("We have sent instructions to your email at: " +email2+ "")
                    print('')
                    time.sleep(0.5)
                    print("Thank you")
                else:
                    print("  _________                                ")
                    print(" /   _____/  ____  _______ _______  ___.__.")
                    print(" \_____  \  /  _ \ \_  __ \\_  __ \<    |  |")
                    print(" /        \(  <_> ) |  | \/ |  | \/ \___  |")
                    print("/_______  / \____/  |__|    |__|    / ____|")
                    print("        \/                          \/     ")
                    time.sleep(1)
                    print("We have no more places")
                    time.sleep(0.5)
                    print("Try Again Later")
            else:
                print("  _________                                ")
                print(" /   _____/  ____  _______ _______  ___.__.")
                print(" \_____  \  /  _ \ \_  __ \\_  __ \<    |  |")
                print(" /        \(  <_> ) |  | \/ |  | \/ \___  |")
                print("/_______  / \____/  |__|    |__|    / ____|")
                print("        \/                          \/     ")
                time.sleep(1)
                print("We have no more places")
                time.sleep(0.5)
                print("Try Again Later")
