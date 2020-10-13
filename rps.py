while True:
    
    print("Enter choice \n 1. r \n 2. p \n 3. s \n") 
      
    
    choice = int(input("User turn: ")) 
  
    
    while choice > 3 or choice < 1: 
        choice = int(input("enter valid input: ")) 
          
    if choice == 1: 
        userchoice_name = 'r'
    elif choice == 2: 
        userchoice_name = 'p'
    else: 
        userchoice_name = 's'
          
    
    print("user choice is: " + userchoice_name)
    
    print("\nNow its computer turn.......") 
  
    
    comp_choice = range(1, 3) 
      
    
    while comp_choice == choice: 
        comp_choice = range(1, 3) 
  
    
    if comp_choice == 1: 
        comp_choice_name = 'r'
    elif comp_choice == 2: 
        comp_choice_name = 'p'
    else: 
        comp_choice_name = 's'
          
    print("Computer choice is: " + comp_choice_name) 
  
    print(userchoice_name + " V/s " + comp_choice_name)


    if (userchoice_name == 'r') and (comp_choice_name == 'r'):
        print("Match Draw")
    elif (userchoice_name == 'r') and (comp_choice_name == 'p'):
        print("computer won the game")
    elif (userchoice_name == 'r') and (comp_choice_name == 's'):
        print("user won the game")
    elif (userchoice_name == 'p') and (comp_choice_name == 'r'):
        print("user won the game")
    elif (userchoice_name == 'p') and (comp_choice_name == 'p'):
        print("Match Draw")
    elif (userchoice_name == 'p') and (comp_choice_name == 's'):
        print("computer won the game")
    elif (userchoice_name == 's') and (comp_choice_name == 'r'):
        print("computer won the game")
    elif (userchoice_name == 's') and (comp_choice_name == 'p'):
        print("user won the game")
    elif (userchoice_name == 's') and (comp_choice_name == 's'):
        print("Match Draw")
    print("\n")
    continue_input = input("Want to play again? (y/n): ").casefold()
    print("\n")
    if (continue_input == 'y') or (continue_input == 'yes'):
        continue
    else:
        print("See you again. Bye")
        break


