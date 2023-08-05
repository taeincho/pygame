class Fighter(object):
    def __init__(self, model, missile):
        self.model = model
        self.missile = missile

    def attack(self):
        print(self.model + "출격!")

    def fire(self):
        print(self.missile + "발사!")

gg = Fighter("Minecraft ", "Roblox")
gg.fire()