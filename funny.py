import time
import random as rnd
import os

def hc():
    hc = input("[H]ub/[C]lose (CAPS ONLY)") # hc stands for hub/close
    print("The script is over! Exit to hub or close the file?")
    hc
    if hc == "H":
        hub_morethanfirst()
    if hc == "C":
        exit()
def dumbasscalc():
    # When the calc is a dumbass
    os.system("cls")
    x = rnd.randint(1, 10)
    a = input("Enter a number: ")
    b = input("Enter a second number: ")
    print("Loading sum...")
    time.sleep(x)
    print(rnd.randint(0, 1000))
    time.sleep(3)
    print("Fun Fact: You have wasted exactly " + str(x) + " seconds! How do you like that fact?")
    rating = input("Rate the fact 1-5!: ")
    rating
    if rating == "1":
        print("Hey! No need to be so rude! :C")
    if rating == "2":
        print("I shouldn't've made such a bad calculator, should've I? :(")
    if rating == "3":
        print("Sorry for admitting to wasting your time, I guess. :/")
    if rating == "4":
        print("I'm happy that you liked it! :)")
    if rating == "5":
        print("Thanks!!! :D")
    if rating == "6":
        print("Huh? I don't think that's what I told you the rating standards were... wait did you actually like it that much")
    answer = input("Did you ACTUALLY like it that much? (Y/N): ").upper()
    if answer == "Y":
        print("Aww! Thanks! But you shouldn't've broke my standards like that...")
    if answer == "N":
        print("I knew that you were just finding easter eggs. Hmph.")
    time.sleep(5)
    print("Did you know? I'm not actually a 'Dumbass', as my creator states, but in actuality just a prankster. LOL!")
    time.sleep(3)
    hc()
def waitdnd():
    ## Wait for X where X = Roll a 100 Sided Dice
    os.system("cls")
    x = rnd.randint(1, 100)
    time.sleep(x)
    print("You have waited for " + str(x) + " seconds!")
    time.sleep(5)
    hc()
def choice():
    print(r"""
    Type the numbers (with lowercase letters) to play a script:
    One. Dumbass Calculator
    Two. time.sleep in a D100 D&D match
    """
    )
    choice_sub = input("Which script would you like to play? (exit to close): ").lower()
    if choice_sub == "one":
        dumbasscalc()
    elif choice_sub == "two":
        waitdnd()
    elif choice_sub == "exit":
        print("Well, okay. Bye-bye!")
        time.sleep(1)
        exit()
def hub_morethanfirst():
    os.system("cls")
    print(r"""
                _                    _             _     _         _   _        
    __ __ _____| |__ ___ _ __  ___  | |__  __ _ __| |__ | |_ ___  | |_| |_  ___ 
    \ V  V / -_) / _/ _ \ '  \/ -_) | '_ \/ _` / _| / / |  _/ _ \ |  _| ' \/ -_)
     \_/\_/\___|_\__\___/_|_|_\___| |_.__/\__,_\__|_\_\  \__\___/  \__|_||_\___|
     _    _ _    _ ____
    | |  | | |  | |  _ \ 
    | |__| | |  | | |_) |
    |  __  | |  | |  _ < 
    | |  | | |__| | |_) |
    |_|  |_|\____/|____/                  
                      """
    )
    time.sleep(1)
    choice_hmtf = input("Another one? [Y]es/[N]o (CAPS ONLY): ")
    if choice_hmtf == "Y":
        choice()
    if choice_hmtf == "N":
        print(r"""                                                                                                                                                                                                                                          
                                                                                                       
                                                                                               
██     ██ ▄▄ ▄▄  ▄▄▄    ▄▄▄▄▄▄ ▄▄▄  ▄▄    ▄▄▄▄    ▄▄ ▄▄  ▄▄▄  ▄▄ ▄▄   ▄▄▄▄▄▄ ▄▄ ▄▄  ▄▄▄ ▄▄▄▄▄▄ 
██ ▄█▄ ██ ██▄██ ██▀██     ██  ██▀██ ██    ██▀██   ▀███▀ ██▀██ ██ ██     ██   ██▄██ ██▀██  ██   
 ▀██▀██▀  ██ ██ ▀███▀     ██  ▀███▀ ██▄▄▄ ████▀     █   ▀███▀ ▀███▀     ██   ██ ██ ██▀██  ██   
                                                                                               
                                                                                               
                                                                                               
██  ██ ▄████▄ ██  ██ █████▄     ▄▄▄▄ ▄▄ ▄▄  ▄▄▄  ▄▄  ▄▄▄▄ ▄▄▄▄▄  ▄▄▄▄                          
 ▀██▀  ██  ██ ██  ██ ██▄▄██▄   ██▀▀▀ ██▄██ ██▀██ ██ ██▀▀▀ ██▄▄  ███▄▄                          
  ██   ▀████▀ ▀████▀ ██   ██   ▀████ ██ ██ ▀███▀ ██ ▀████ ██▄▄▄ ▄▄██▀                          
                                                                                               
                                                                                               
                                                                              ▄▄▄▄             
▄▄   ▄▄  ▄▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄    ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄ █▀▀▀██            
██▀▄▀██ ██▀██  ██     ██   ██▄▄  ██▄█▄ ██▄▄  ██▀██   ██▄██ ██▄▄  ██▄█▄ ██▄▄    ▄█▀             
██   ██ ██▀██  ██     ██   ██▄▄▄ ██ ██ ██▄▄▄ ████▀   ██ ██ ██▄▄▄ ██ ██ ██▄▄▄   ▄▄              
                                                                                            
        """
        )
        choice()
def hub_first():
    print("I'd recommend using fullscreen or a slightly bigger window!")
    time.sleep(1)
    print("Also, as far as I know the os.system('cls') works only on Windows. Sorry, Mac users and Linux nerds!")
    time.sleep(3)
    os.system("cls")
    print(r"""
     _    _      _ _         __          __        _     _ _ 
    | |  | |    | | |        \ \        / /       | |   | | |
    | |__| | ___| | | ___     \ \  /\  / /__  _ __| | __| | |
    |  __  |/ _ \ | |/ _ \     \ \/  \/ / _ \| '__| |/ _` | |
    | |  | |  __/ | | (_) |     \  /\  / (_) | |  | | (_| |_|
    |_|  |_|\___|_|_|\___( )     \/  \/ \___/|_|  |_|\__,_(_)
                         |/ 
      _    _ _    _ ____  
    | |  | | |  | |  _ \ 
    | |__| | |  | | |_) |
    |  __  | |  | |  _ < 
    | |  | | |__| | |_) |
    |_|  |_|\____/|____/ 
                      
    """
    )
    print(r"""
    Hello, World!
    This small pack of scripts was made by Axxy, also sometimes known as qwuikky.
    The pack consists of a few useless but somewhat funny scripts.
    """)
    time.sleep(2)
    choice()

hub_first()
# A comment to change the commit's name.
