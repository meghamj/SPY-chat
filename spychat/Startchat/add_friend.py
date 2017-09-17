from globals import friends


def add_friend():
    friend_name = {"salutation": "", "name": "", "age": 0, "rating": 0.0, "is online": False,
                   'salutation': raw_input('Mr.\ Mrs.\ Ms.'), 'name': raw_input("Enter your fried's name")}
    friend_name= friend_name['salutation']+ " " + friend_name['name']
    friend_name['age'] = int(raw_input('Your age is: '))
    friend_name['rating'] = int(raw_input('Your rating is: '))

    if len(friend_name['name'])>0 and friend_name['age']>12 and friend_name['age']<55:
        friend_name['is online']= True
        friends.append(friend_name)
        print "A new friend is addedd"
    else:
        print "Invalid input"
    return len(friends)


