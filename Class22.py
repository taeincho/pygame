class Hello():
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print(self.name+'안녕하세요')
    def goodbye(self):
        print("한녕하세요")
a = Hello('류지')
a.greeting()