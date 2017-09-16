from globals import friends

def Select_friend():
    counter = 1
    print str(counter) + " " + friends['salutation'] + " " + friends['name']
    counter += 1
    user_input = int(raw_input("choose the friend from the list : "))
    if user_input <= counter:
        return user_input -1
    else:
        print"Invalid choice. Try again"
        exit(-1)

