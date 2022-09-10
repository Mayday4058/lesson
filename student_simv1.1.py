import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.bux = 20
    def to_study(self):
        print("another day in university\nWELCOME TO THE RICE FIEl... adult life, son")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("ok ill go to bed")
        self.gladness += 3
    def to_chill(self):
        print("time to play fortnite! \nand regress")
        self.gladness += 5
        self.progress -= 0.1
    def earn_bux(self):
        print("time to earn some bux!")
        self.gladness -= 3
        self.progress -= 0.2
        self.bux += 20

    def is_alive(self):
        if self.progress < -0.5:
            print("kicked from the university\ngo to mcdonalds them")
            self.alive = False
        elif self.gladness <= 0:
            print("you`ve commited suicide \n:/")
            self.alive = False
        elif self.progress > 5:
            print("you should`ve learnt more, dumbo\n(c)warden")
            self.alive = False
        elif self.bux >= 0:
            print("you`re a hobo now! woohoo!\nhmmm. why not make a hobo simulator next time?")
            self.alive(False)

    def end_of_day(self):
        print(f"non-suicide points = {self.gladness}")
        print(f"progress to BETTER LIFE = {round(self.progress, 2)}")
        print(f"ur bux = {self.bux}")
        print("glory to arstotzka\nGET IT? GET IT? nah")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive ()
        elif live_cube == 4:
            self.earn_bux()
            self.end_of_day()
            self.is_alive()
nick = Student(name="east grestin inspector")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)