class Watch:
    def set_time(self):
        now = input("시간을 입력하세요")
        hms = now.split(":")
        self.hour = int(hms[0])
        self.minute = int(hms[1])
        self.second = int(hms[2])

    def add_hour(self, hour):
        if hour <= 0:
            return
        self.hour += hour
        self.hour %= 24
        
    def add_minute(self, minute):
        if minute <= 0:
            return
        self.minute += minute
        self.add_hour(self.minute // 60)
        self.minute %= 60
        
    def add_second(self, second):
        if second <= 0:
            return
        self.second += second
        self.add_minute(self.second // 60)
        self.second %= 60
        
    def see(self):
        print("계산된 시간은 ", end='')
        print("{}시 {}분 {}초 입니다.".format(self.hour, self.minute, self.second))
        
w = Watch()
w.set_time()
w.add_hour(10)
w.add_minute(70)
w.see()
