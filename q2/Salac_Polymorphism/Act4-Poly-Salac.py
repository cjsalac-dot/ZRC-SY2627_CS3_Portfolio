class HealthPotion:
    def use(self):
        print("You regain 50 HP!")

class ManaPotion:
    def use(self):
        print("You regain 30 MP!")

class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")

def apply_item(item):
    item.use()

hp = HealthPotion()
mp = ManaPotion()
sb = SpeedBoost()

items = [hp, mp, sb]
for i in items:
    apply_item(i)