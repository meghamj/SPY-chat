from globals import Status_messages

updated_status_message = None

def add_status(current_status_message):
    if current_status_message != None:
        print "Your Current Status is: " + current_status_message + "\n"
    else:
        print "No Current Status Found \n"
    default = raw_input("Do you want to continue with the current status?  y/n")
    if default.upper() == "N":
        new_status_message = raw_input("Write the status you want:")

        if len(new_status_message)>0:
            updated_status_message = new_status_message
            Status_messages.append(updated_status_message)
            print "Your updaed message is: %s"%(updated_status_message)
            print "you have not given any message"
    elif default.upper() == "Y":
        item_position = 1
        for message in Status_messages:
            print str(item_position) + "." + message
            item_position += 1
        message_selection = int(input("\n Choose from the "))
        if len(Status_messages)>=message_selection:
            updated_status_message = Status_messages(message_selection)
            print "Your updated status message is: %s"% ()
        else:
            print "Invalid Input "
    else:
        print "You have entered a wrong choice"
    return updated_status_message
