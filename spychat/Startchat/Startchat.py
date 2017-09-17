from Select_friend import Select_friend
from add_status import add_status
from add_friend import add_friend
from Send_message import send_message
from read_message import read_message
from read_chat_history import read_chat_history

def start_chat(name,age,rating,status):
    from globals import current_status_messages
    error_message = None

    if not(age > 12 and age < 50):
        error_message = "Invalid age! provide valid age"
        print error_message
    else:
        Welcome_message = "Authenticaion complete. \n Welcome"
        print Welcome_message

        show_menu = True
        while show_menu:
            menu_choices = "Select your choice from the following options"
            "1.Add a status update \n" \
            "2.Add a friend \n" \
            "3.Send a secret message \n" \
            "4.read a secret messaage \n " \
            "5.Read chat frm a user \n" \
            "6.Close application \n"
        result = int(input(menu_choices))
        # validating user input
        if (result == 1):
            current_status_messages = add_status(current_status_messages)
        elif (result == 2):
            number_of_friend = add_friend()
            print "You have %d friends" % (number_of_friend)
        elif (result == 3):
            send_message()
        elif (result == 4):
            read_message()
        elif (result == 5):
            read_chat_history()
        elif (result == 6):
            show_menu = False
        else:
            cprint('Wrong choice entered please try again *_* ', 'red', attrs=['bold'])#validating user input
            if (result == 1):
                current_status_messages = add_status(current_status_messages)
            elif (result == 2):
                number_of_friend = add_friend()
                print "You have %d friends" % (number_of_friend)
            elif (result == 3):
                send_message()
            elif (result == 4):
                read_message()
            elif (result == 5):
                read_chat_history()
            elif (result == 6):
                show_menu = False
            else:
                cprint ('Wrong choice entered please try again *_* ','red',attrs=['bold'])


