from globals import friends
def addFriend():
    Friend_name = {
        "salutation": "",
        "name":"",
        "age": 0,
        "rating": 0.0,
        "is online": False
    }
    Friend_name['salutation'] = raw_input('Mr.\ Mrs.\ Ms.')
    Friend_name['name'] = raw_input("Enter your fried's name")

