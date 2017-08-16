print "Let's get started"
spy_name = raw_input("What is your name?")
spy_salutation = raw_input("What you want to be called like mr. or mrs. or dr.")
spy_name = spy_salutation + "" + spy_name
if len(spy_name)>0:
    print "Welcome " + spy_name +  " glad to have you with us."
else:
    print "Invalid name, Please try again "
spy_age = 0
spy_rating = 0.0
