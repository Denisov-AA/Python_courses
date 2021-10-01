class Hours:
    def __init__(self, seconds, degrees):
        self.degrees = degrees
        self.seconds = seconds

    def seconds_convert(self):
        if self.seconds > 86400:
            print("More than 1 day passed")
        else:
            sec_hours = self.seconds // 3600
            sec_minutes = (self.seconds % 3600) / 60
            print(f"It is {sec_hours} hours {int(sec_minutes)} minutes ")

    def degrees_convert(self):
        if self.degrees > 720:
            print("More than 1 day passed")
        else:
            deg_hours = self.degrees // 30
            deg_minutes = (self.degrees % 30) * 2
            print(f"It is {deg_hours} hours {int(deg_minutes)} minutes")
