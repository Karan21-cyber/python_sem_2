try: #Try is used to check the program runs or not. If runs it executed else return except.
    print("\nStop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.\n")
    pass_name = ["Arthur","Grail"]
    name = input("What is your name? ") 
    
    if pass_name[0].lower() in name or pass_name[0] in name: #It checks that given name is in the list[0] or not. 
        print("My liege! You may pass!\n")
    
    else: # It execute if 1st condition doesnot match
        quest = input("What is your quest? ") 

        if pass_name[1].lower() not in quest and pass_name[1] not in quest: # IT checks that "grail" is in the quest or not. 
            print("\nOnly those who seek the Grail may pass.\n")
            
        else: # It execute if the 2nd conditon match.
            color = input("What is your favourite color? ")
            if color[0].capitalize() == name[0].capitalize():  # It checks the First character of the color and name and match.
                print("You may pass!\n")
            
            else: # This is execute if the 3rd condition is not match.
                print("Incorrect! You must now face the Gorge of Eternal Peril.\n")

except: # This is execute if the code has an error
    print("There is some error in your input")
