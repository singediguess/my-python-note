import datetime

def showtime():
    today = datetime.date.today()
    print ('today is '+ str(today.month) + '/' + str(today.day))
    return;
