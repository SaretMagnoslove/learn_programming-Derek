class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return ('{}:{:02d}:{:02d}'.format(self.hours, self.minutes, self.seconds))

    def __add__(self, othertime):
        newtime = Time()
        if (self.seconds + othertime.seconds) >= 60:
            self.minutes += 1
            newtime.seconds = self.seconds + othertime.seconds - 60
        else:
            newtime.seconds = self.seconds + othertime.seconds
        if (self.minutes + othertime.minutes) > 60:
            self.hours += 1
            newtime.minutes = self.minutes + othertime.minutes - 60
        else:
            newtime.minutes = self.minutes + othertime.minutes
        if (self.hours + othertime.hours) > 24:
            newtime.hours = self.hours + othertime.hours - 24
        else:
            newtime.hours = self.hours + othertime.hours
        return newtime
def main():
    time1 = Time(1,20,30)
    print(time1)
    time2 = Time(24,41,30)
    print (time1+time2)

main()


