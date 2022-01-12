import random # Random module which is imported from the in-built modules

def intro():
    """This function an intro and ask the user to input the email."""
    print("\nWelcome to Pop Chat\nOne of our operators will be pleased to help you today.\n")
    email = input("Please enter your Poppleton email address: ")
    if email == "":  #If the email is not provided the it exit the program 
        print("No E-mail entered. Nothing to do.\n")
    else:  # If the email is provided it call the Email function by passing two parameters email and domain 
        Email(email,domain="@pop.ac.uk")

def Email(mail,domain):
    """This function receive the mail and domain from the above. It will check the entered email is valid or not."""
    if "@" in mail[:3]:  # It checks if "@" comes before the length 3 the email is invalid
        print("Invalid E-mail!")
    elif domain not in mail:   # It checks email domain.  
        print("E-mail domail doesnot match!")
    else:      # IF all the condition is fulfilled then pass the mail to extract function.
        extract(mail)

def extract(e_mail):
    """This is the function that receive the email and extract the name from the email and pass the name to the chat_bot function."""
    name = e_mail.index("@")
    user=e_mail[:name]
    chat_bot(user)

def chat_bot(user):
    """This function receive the name of the user. """
    rand_name = ["Janice","Hary","Alexander","Juli","Andrew","Miya","Fiona"] 
    rand_num = range(10)
    print("\nHi, {}! Thank you, and Welcome to PopChat!".format(user))
    print("My name is {}, and it will be my pleasure to help you.".format(random.choice(rand_name)))

    if random.choice(rand_num) <= 2: # It check the internet connection if the value <= 2 then there is network error
        print("\n\t*****NETWORK ERROR*****\n")
    else:  # If the value is more or equal to 1 then it execute
        while True:  # This will loop the code
            question = input("----> ")
            if "goodbye" in question or "exit" in question or "bye" in question:  #If the input is bye or exit or goodbye then it break the loop 
                break
            else: #if condition is fulfilled it execute
                answer(question)
    print("Thanks, {}, for using PopChat. See you again soon!\n".format(user))  

def answer(question):
    """This function receive the question and check the condition and provide the answer accordig to questions."""
    my_list = ["library","wifi","deadline","coffee","hungry","fee","college","bored","teacher"]
    # it checks the condition and print the statements 
    if my_list[0] in question:  
        print("The library is closed today.")
    elif my_list[1] in question:  
        print("WiFi is excellent across the campus.")
    elif my_list[2] in question:  
        print("Your deadline has been extended by two working days.")
    elif my_list[3] in question:  
        print("Teekee is open until 9pm this evening.")
    elif my_list[4] in question: 
        print("The campus cafe is open 24 hrs.")
    elif my_list[5] in question:   
        print("You can consult to the administration department.")
    elif my_list[6] in question:   
        print("The college open from 7am to 7pm.")
    elif my_list[7] in question:   
        print("You can listen some music. Or you can go out for walk.")
    elif my_list[8] in question:   
        print("Teachers are professional and friendly.")
    else:     #it check if the question doesnot match it returns randomly
        lol = ["Hmmm","Oh","yes","I see","Tell me more","Like"]
        print(random.choice(lol))

intro()