#from spy_details import spy_name, spy_salutation, spy_rating, spy_is_online, spy_age
from Startchat import start_chat
from spy_details import spy

print "Lets get started!"
print "Do you want to continue as " + spy['salutation']+ " " + spy['name']
existing_user = raw_input('enter y/n')
if(existing_user.upper()=="Y"):
    print 'Welcome back' +spy['salutation']+ " " +spy['name']
    print 'good to see you again'
    print '%s is your rating'%(spy['spy_rating'])
    print 'and Your age is %s'%(spy['age'])
    start_chat(spy['name'],spy['age'],spy['spy_rating'],spy['spy_is_online'])

elif(existing_user.upper() == "N"):
    spy_name = raw_input('Welcome to Spychat please provide your name: ')
    if len(spy_name)>0:
        spy['salutation'] = raw_input("what you want to be called mr. or ms. ? ")
        spy['age'] = raw_input("enter your age: ")
        spy['age'] = int(spy['age'])
        spy['spy_rating'] = raw_input("what is your rating?: ")
        spy_rating = float(spy['spy_rating'])
        spy_is_online = True
        print 'Your Authentication is completed %s %s\n You seems to be a young spy with the age %s and rating of %s \n'%(spy['salutation'],spy['name'],spy['age'],spy['spy_rating'])
        start_chat(spy['name'], spy['age'], spy['spy_rating'], spy['spy_is_online'])

else:
    print "You have provided a wrong input!"
