class God():
    def __init__(self, name, age, country, height):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
    def introduce(self):
        print(f"저의 이름은 {self.name}이고, 나이는 {self.age}세, 국적은 {self.country}, 신장은 {self.height}cm 입니다.")
    
a = God("김박사", 20, "김밥천국", 100)
b = God("페트병", 20, "라면사랑", 200)
c = God("Olymp Trade", 2014, "Olymp Trade", 2014)
a.introduce()