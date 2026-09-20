class teacher :
    name = "anonymous"
    def __init__(self, name):
        self.name = name
    @staticmethod
    def fight(st1, st2):
        print(f"{st1.name} is fighting with {st2.name}")
        print("suspended both of them")
    @staticmethod
    def breaktime():
        print("break time is over")
st1 = teacher("john")
st2 = teacher("jane")
s4 = teacher("ali")
s3 = teacher.fight(s4, st2)
print(st1.name)
print(st2.name)
# print(s3)