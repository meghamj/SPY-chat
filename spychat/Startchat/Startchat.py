from Select_friend import Select_friend
from add_status import add_status

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
    if (result == 1):
         current_status_messages= add_status(current_status_messages)
    elif (result == 6):
        show_menu = False
    else:
        print "error"



