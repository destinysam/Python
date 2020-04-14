# coded by sam@sameer
# email:sams44802@gmail.com
# date:29/02/2020
# project: car start/stop

started = False
stopped = False
print("TYPE YOUR OPTION start,stop or help")
while(True):
    option = input("")
    if option.upper() == 'START':
        if started:
            print("CAR IS ALREADY STARTED")
        else:
            started = True
            print("CAR STARTED...")
    elif option.upper() == 'STOP':
        if stopped:
            print("CAR IS ALREADY STOPPED")
        else:
            stopped = True
            print("CAR IS STOPPED")
    elif option.upper() == 'HELP':
        print("start- to start car")
        print("stop- to stop car")
        print("exit-to exit")
    elif option.upper() == 'EXIT':
        print("program closed")
        break
    else:
        print("NOT UNDERSTANDING YOUR OPTION")