def main():
    usertime = input("What time is it? ")
    hours = convert(usertime)
    if hours >= 7.0 and hours <= 8.0:
        print("breakfast time")
    if hours >= 12.0 and hours <= 13.0:
        print("lunch time")
    if hours >= 18.0 and hours <= 19.0:
        print("dinner time")

def convert(time):
    timeparts = time.split(":")
    hours_string = timeparts[0]
    minutes_string = timeparts[1]
    hours = float(hours_string)
    minutes = float(minutes_string)
    minutesconvert = minutes / 60.0
    totaltime = hours + minutesconvert
    return totaltime

if __name__=="__main__":
    main()
