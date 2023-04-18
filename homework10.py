
class Dragon:
    def __init__(self, height, danger, color):
        self.height = height #высота
        self.danger = danger #уровень опасности
        self.color = color #цвет
    
    def __lt__(self, other):
        if self.height != other.height:
            return self.height < other.height
        elif self.danger != other.danger:
            return self.danger < other.danger
        else:
            return self.color < other.color
    
    def __eq__(self, other):
        return self.height == other.height and self.danger == other.danger and self.color == other.color
    
    def __add__(self, other):
        height = (self.height + other.height) // 2 # средняя высота
        danger = max(self.danger, other.danger) # максимальный уровень опасности
        color = min(self.color, other.color) # минимальный цвет
        return Dragon(height, danger, color)
    
    def __sub__(self, num):
        self.height -= self.height // num
        self.danger += self.danger % num
        return self
    
    def __call__(self, string):
        return string * self.danger # повторение строки string danger раз
    
    def change_color(self, new_color):
        self.color = new_color # изменение цвета
    
    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.danger} and color {self.color}." # строковое представление дракона
    
    def __repr__(self):
        return f"Dragon({self.height}, {self.danger}, {self.color})" # строковое представление для измененного дракона
    
    def __le__(self, other):
        if self.height != other.height:
            return self.height <= other.height
        elif self.danger != other.danger:
            return self.danger <= other.danger
        else:
            return self.color <= other.color


dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")
print(dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")
print()

dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr + dr1
print(dr, dr1, dr2, sep="\n")

print(dr("Welcome "))

