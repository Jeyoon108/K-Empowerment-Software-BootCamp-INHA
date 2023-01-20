#

class PrettyMixin():
    def time_print(self):
        import datetime
        print(datetime.date.today())


    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.gender = "male"
t.dump()

t.time_print()
