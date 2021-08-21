import time

lastHour = time.time()/(60*24)

def clock():
    currentTime = time.time()/60
    print("Current time since eposh in minutes is ",round(currentTime))

def main():
    while(True):
        hour = int((time.time()/(60*24))-lastHour)
        print(hour)
        min = int((time.time()/60)-(lastHour*60))
        print(min)
        if(min == min+1):
            clock()
        if(hour == hour+1):
            print(hour," hour as passed since you've actived program")

main()