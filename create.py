# create.py | main program
# author: mairebaap

import os
import time

shortcut = '''
[Desktop Entry]
Encoding=UTF-8
'''

class bcolors: # colors for cli
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# append application type and start up behaviour beforehand
def beforehandAppend():
    type = "Type=application\n"
    startUpNotify = "StartupNotify=false\n"

    concatenateBoth = str(type) + str(startUpNotify)

    with open('shortcuts/progress.txt', 'a') as progress:
        progress.write(concatenateBoth)
        
def stageFour():
    beforehandAppend() # call the appending function
    os.system('clear')
    print(f"{bcolors.HEADER}     PHASE FOUR: Catagories     {bcolors.ENDC}")
    print("___________________________________________________________________")
    print("These are the final touches before succesfully making the shortcut and renaming io a .desktop format.\n")
    print("Press a key 1-9 to choose a catagory.\n")
    print("Note: After choosing, go to terminal and use rename.py to rename the .txt to a .desktop format. Although you can do this in your distro's file manager alone, it's somewhat more convenient than doing all that with your mouse.\nInstructions are in the readme file.")
    choice = input(
        f'''
        {bcolors.WARNING}1{bcolors.ENDC} - Accessories\n
        {bcolors.WARNING}2{bcolors.ENDC} - Games\n
        {bcolors.WARNING}3{bcolors.ENDC} - Graphics\n
        {bcolors.WARNING}4{bcolors.ENDC} - Internet\n
        {bcolors.WARNING}5{bcolors.ENDC} - Office\n
        {bcolors.WARNING}6{bcolors.ENDC} - Programming\n
        {bcolors.WARNING}7{bcolors.ENDC} - Sound and Video\n
        {bcolors.WARNING}8{bcolors.ENDC} - System Tools (very unlikely)\n
        {bcolors.WARNING}9{bcolors.ENDC} - Utilities\n
        '''
    )

    match choice: # yet to be adden functionality
        case '1':
            print("Saved and ready to go.")
            with open('shortcuts/progress.txt', 'a') as progress:
                chose = "Categories=" + str('Accessories')
                progress.write(chose)
            opn = open('shortcuts/progress.txt', 'r')
            print(opn)
        case '2':
            print("Saved and ready to go.")
            with open('shortcuts/progress.txt', 'a') as progress:
                chose = "Catagories=" + str('Games')
                progress.write(chose)
            opn = open('shortcuts/progress.txt', 'r')
            print(opn)
        case '3':
            print("Saved and ready to go.")
            with open('shortcuts/progress.txt', 'a') as progress:
                chose = "Catagories=" + str('Graphics')
                progress.write(chose)
            opn = open('shortcuts/progress.txt', 'r')
            print(opn)
        case '4':
            print("Saved and ready to go.")
            with open('shortcuts/progress.txt', 'a') as progress:
                chose = "Catagories=" + str('Internet')
                progress.write(chose)
            opn = open('shortcuts/progress.txt', 'r')
            print(opn)
        case '5':
            print("Saved and ready to go.")
            with open('shortcuts/progress.txt', 'a') as progress:
                chose = "Catagories=" + str('Office')
                progress.write(chose)
            opn = open('shortcuts/progress.txt', 'r')
            print(opn)
        case '6':
            print("Saved and ready to go.")
            with open('shortcuts/progress.txt', 'a') as progress:
                chose = "Catagories=" + str('Programming')
                progress.write(chose)
            opn = open('shortcuts/progress.txt', 'r')
            print(opn)
        case '7':
            print("Saved and ready to go.")
            with open('shortcuts/progress.txt', 'a') as progress:
                chose = "Catagories=" + str('Sound & Video')
                progress.write(chose)
            opn = open('shortcuts/progress.txt', 'r')
            print(opn)
        case '8':
            print("Saved and ready to go.")
            with open('shortcuts/progress.txt', 'a') as progress:
                chose = "Catagories=" + str('System Tools')
                progress.write(chose)
            opn = open('shortcuts/progress.txt', 'r')
            print(opn)
        case '9':
            print("Saved and ready to go.")
            with open('shortcuts/progress.txt', 'a') as progress:
                chose = "Catagories=" + str('Utilities')
                progress.write(chose)
            opn = open('shortcuts/progress.txt', 'r')
            print(opn)

def stageThree():
    os.system('clear')
    print(f"{bcolors.HEADER}      PHASE THREE: ICONS     {bcolors.ENDC}")
    print("___________________________________________________________________")
    print("Specify the icon for your application. If it's on your /usr/share/icons, then just type the filename. Otherwise, specify the category\n")

    icon = input("Filename or directory of icon: ")

    if icon == None:
        print("Try again")
    elif icon == icon:
        iconDir = "Icon=" + str(icon) + "\n"
        with open('shortcuts/progress.txt', 'a') as progress:
            progress.write(iconDir)
        print("Okay, progress has been saved.")

        showProg = open('shortcuts/progress.txt', "r")
        print(showProg.read())
        
        cToCont = input(f"{bcolors.OKCYAN}Press C to continue.{bcolors.ENDC}\n")
        if cToCont == "C" and "c":
            stageFour()
        else:
            print(f"{bcolors.FAIL}Invalid input. The program will halt.{bcolors.ENDC}")

def optionalAgreed():
    print("What will your comment will be?\n")
    comment = input("Type here: ")
    if comment == " ":
        while True:
            print("bye bye!")
            os.system("bash shutdown -P now")
    elif comment == comment:
        com = "Comment=" + str(comment) + "\n" + "Terminal=false"

        print("Sure. Progress has been saved.")
        with open("shortcuts/progress.txt", "a") as progress:
            progress.write(com)
        showProg = open('shortcuts/progress.txt', "r")
        print(showProg.read())
        cToCont = input(f"{bcolors.OKCYAN}Press C to continue.{bcolors.ENDC}\n")
        if cToCont == "C" and "c":
            stageThree()
        else:
            print(f"{bcolors.FAIL}Invalid input. The program will halt.{bcolors.ENDC}")

def optional():
    print(f"{bcolors.HEADER}     OPTIONAL PHASE     {bcolors.ENDC}")
    print("___________________________________________________________________")
    print("Do you want to write comments? You will see it when you hover the icon on the desktop.\n")
    askForOptional = input("Press Y for yes. Press N for no")
    if askForOptional == "Y" and "y":
        optionalAgreed()
    elif askForOptional == "N" and "n":
        with open('shortcuts/progress.txt', 'a') as progress:
            progress.write("Comment=" + "\n" + "Terminal=false" + "\n")
        stageThree()
    else:
        print(f"{bcolors.FAIL}Invalid input. The program will halt.{bcolors.ENDC}")
        
def stageTwo():
    os.system('clear')
    print((f"{bcolors.HEADER}     PHASE TWO: EXECUTABLE DIRECTORY\n     {bcolors.ENDC}").center(33))
    print("___________________________________________________________________")
    askForDir = input("Where is the directory of the application? If the application is in your PATH then you just need to write the name of the application in lowercase. Otherwise, enter the directory.\n")
    if askForDir == " ":
        print(f"{bcolors.FAIL}Invalid input. The program will halt.{bcolors.ENDC}")
    elif askForDir == askForDir:
        dir = "Exec=" + str(askForDir) + "\n"
        print("Certainly! Progress has been saved.\n")
        with open('shortcuts/progress.txt', 'a') as progress:
            progress.write(dir)

        showprog = open('shortcuts/progress.txt', 'r')
        print(showprog.read())
        cToCont = input(f"{bcolors.OKCYAN}Press C to continue.{bcolors.ENDC}\n")
        if cToCont == "C" and "c":
            optional()
        else:
            print(f"{bcolors.FAIL}Invalid input. The program will halt.{bcolors.ENDC}")

def stageOne():
    # clean up the console first
    os.system('clear')
    print(f"{bcolors.HEADER}     PHASE ONE: Name\n     {bcolors.ENDC}")
    print("___________________________") # line to separate element
    askForName = input("What is the name of your shortcut? Typically, it's the name of the application itself though you can set it as how you wish.\n")
    if askForName == " ":
        print("Try again.")
    elif askForName == askForName:
        os.system('clear')
        # append name to shortcut variable
        newln = "Name=" + str(askForName) + "\n"
        concatenate = shortcut + newln
        print("Gladly! Here is what the shortcut file looks like right now. Progress is saved in progress.txt.\n")
        try:
            with open("shortcuts/progress.txt", "w") as progress:
                progress.write(concatenate)
        except:
            while True:
                print(f"{bcolors.FAIL}AN ERROR HAS OCCURED AND THE APPLICATION MUST BE HALTED.{bcolors.ENDC}")
                time.sleep(5)
                break
        showProg = open('shortcuts/progress.txt', "r")
        print(showProg.read())

        cToCont = input(f"{bcolors.OKCYAN}Press C to continue.{bcolors.ENDC}\n")
        if cToCont == "C" and "c":
            stageTwo()
        else:
            print(f"{bcolors.FAIL}Invalid input. The program will halt.{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}Invalid input. The program will halt.{bcolors.ENDC}")

def startingPhase():
    os.system('clear')
    print(f"{bcolors.HEADER}Welcome to the GNOME Command Line desktop icon adder! A GUI version of it shall be developed soon and the whole thing shall be wrotten from scratch for better readibility.\n{bcolors.ENDC}")  
    print("It is much recommended to run this on fullscreen for a better experience.")
    print(f"{bcolors.WARNING}WARNING: IF YOU MESS SOMETHING UP, YOU HAVE TO START OVER AGAIN\nKEEP IN MIND THAT THERE ARE SOME BUGS THAT SRE OUGHT TO BE FIXED  .{bcolors.ENDC}")
    print(f"{bcolors.FAIL}EVERY SINGLE INPUT MUST BE CASE SENSITIVE OTHERWISE YOU WILL LOSE ALL YOUR PROGRESS.{bcolors.ENDC}")
    askForInput = input("Press Y to proceed or Q to quit\n")

    # check for 
    if askForInput == "Y" and "y":
        os.system('mkdir shortcuts')
        stageOne()  
    elif askForInput == "Q" and "q":
        os.system('exit')
    else:
        print(f"{bcolors.FAIL}Invalid input. The program will halt.{bcolors.ENDC}")
        os.system('exit')
    
startingPhase()
