class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name="Musa", age=20, track=["Mechanical Engineering", "Full Stack Development"], score=98.6):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = int(age)

    def get_score(self, score):
        self.score = float(score)

    def add_track(self, track=[]):
        self.track = track


Bob = Student(name="Bob", age=26, track=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(78.22)
print(Bob.age)  # 34
print(Bob.name)  # Peter
print(Bob.track)  # 'UI/UX'
print(Bob.score)  # 78.22
