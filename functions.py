"""A collection of functions for doing my project."""

def rps(msg_2):
    """Takes the user input between 1 to 4 and translates it to rock, paper, scissors, or exit the program.
    
    Parameters
    ----------
    msg_2 : int
        Translate user input to rock, paper, scissors.
    
    Returns
    ---------
    play : string
        The translated user input.
    """
    
    play=''
    if msg_2 == "1":
        play='rock'
        print("\nYou played Rock!")
    elif msg_2 == "2":
        play='paper'
        print("\nYou played Paper!")
    elif msg_2 == "3":
        play='scissors'
        print("\nYou played Scissors!")
    elif msg_2 == "4":
        print("\nHave a nice day!")
        play = False
    else:
        print("\nOops! Please select from the option!")
    return play

def win_or_lose(play):
    """Determines if the user wins or loses the game of rock, paper, scissors against a robot who chooses randomly from a list.
    
    Parameters
    ----------
    play : string
        Uses the user's input to run program.
    computer_list : list
        A list for robot to randomly choose from.
    
    Returns
    ---------
    counter : int
        Contains the user's total number of wins.
    """
    
    import random
    
    #Declares a global parameter
    global counter
    
    computer_list = ['rock','paper','scissors']
    
    #Robot to randomly choose from computer_list
    computer_choice = random.choice(computer_list)
    
    #Prints the corresponding requirements if conditions are met
    if computer_choice == 'rock' and play == 'rock':
        print("I played Rock!")
        print("Rock and Rock! A draw!")
        counter = counter + 0
        print("Your total points is:",counter)
    elif computer_choice == 'rock' and play == 'paper':
        print("I played Rock!")
        print("Paper beats Rock! You win!")
        counter = counter + 1
        print("Your total points is:",counter)
    elif computer_choice == 'rock' and play == 'scissors':
        print("I played Rock!")
        print("Rock beats Scissors! You lose!")
        counter = counter + 0
        print("Your total points is:",counter)
    elif computer_choice == 'paper' and play == 'rock':
        print("I played Paper!")
        print("Paper beats Rock! You lose!")
        counter = counter + 0
        print("Your total points is:",counter)
    elif computer_choice == 'paper' and play == 'paper':
        print("I played Paper!")
        print("Paper and Paper! A draw!")
        counter = counter + 0
        print("Your total points is:",counter)
    elif computer_choice == 'paper' and play == 'scissors':
        print("I played Paper!")
        print("Scissors beats Paper! You win!")
        counter = counter + 1
        print("Your total points is:",counter)
    elif computer_choice == 'scissors' and play == 'rock':
        print("I played Scissors!")
        print("Rock beats Scissors! You win!")
        counter = counter + 1
        print("Your total points is:",counter)
    elif computer_choice == 'scissors' and play == 'paper':
        print("I played Scissors!")
        print("Scissors beats Paper! You lose")
        counter = counter + 0
        print("Your total points is:",counter)
    elif computer_choice == 'scissors' and play == 'scissors':
        print("I played Scissors!")
        print("Scissors and Scissors! A draw!")
        counter = counter + 0
        print("Your total points is:",counter)
    return counter

def dolphin_facts():
    """Prints a random fact about dolphins from a list.
    
    Parameters
    ----------
    facts : list
        A list for robot to randomly choose from.
    
    Returns
    -------
    random_fact : string
        String containing a randomly chosen option from a list.
    """
    import random
    facts = ["\nMost dolphins live in shallow areas of tropical and temperate oceans!",
             "\nDolphins are well known for their agility and playful behavior!",
            "\nDolphins usually only give birth to one calf!",
            "\nDolphins are carnivores! Preying on things like fish and squid!",
            "\nMales are called bulls, female dolphins are called cows, and young dolphins are called calves!",
            "\nDolphins use their blowholes to breath!"]
    
    #Robot randomly chooses from facts
    random_fact = random.choice(facts)
    return random_fact


counter = 0
def start_game():
    """Starts the program
    
    Parameters
    ----------
    msg : string
        The user's input.
    msg2 : string
        User's input for rps function.
    
    Returns
    -------
    None
    """
       
    import random
    chat = True
    
    #Puts user in while loop until conditional is met
    while chat == True:
        
        #Takes the user input
        msg = input("This program contains a game of Rock, Paper, Scissors! \n1 to Continue! \n2 for a random dolphin fact! \n3 to Exit! \n")
        if msg == "1":
            chat_2 = True
            
            #Puts the user in a second loop until conditional is met
            while chat_2 == True:
                
                #Takes the user input
                msg_2 = input("\n1 for Rock! \n2 for Paper! \n3 for Scissors! \n4 to Quit! \n")
                
                #Uses user's input for the rps function
                play = rps(msg_2)
                
                #Uses user's input for the win_or_lose function
                outcome = win_or_lose(play)
                if play == False:
                    chat_2 = False
                    chat = False
                else:
                    continue
        elif msg == "2":
            random_fact = dolphin_facts()
            print(random_fact)
        elif msg == "3":
            print("Have a nice day!")
            chat = False
        else:
            print("Please select from the options!")
