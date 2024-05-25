# база 1
class First:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def write_num(self):
        print(f'Первое число: {self.num1}, второе число: {self.num2}')
    def redact(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def Summa(self):
        return self.num1 + self.num2
    def MaxNumber(self):
        if self.num1 == self.num2:
            return '='
        elif self.num1 > self.num2:
            return '>'
        else:
            return '<'

Object = First(int(input('Введите первое число: ')), int(input('Введите второе число: ')))
Object.write_num()
print(f'{Object.num1} + {Object.num2} = {Object.Summa()}')
print(f'{Object.num1} {Object.MaxNumber()} {Object.num2}')
Operation = input('Вы хотите изменить числа? (Yes/No): ')

while Operation == 'Yes':
    Object.redact(int(input('Введите первое изменённое число: ')), int(input('Введите второе изменённое число: ')))
    Object.write_num()
    print(f'{Object.num1} + {Object.num2} = {Object.Summa()}')
    print(f'{Object.num1} {Object.MaxNumber()} {Object.num2}')
    Operation = input('Вы хотите изменить числа? (Yes/No): ')

# база 2
class Polynomial:
    def __init__(self, *terms: int):
        self._terms = tuple(terms)

    def __str__(self):
        out = str(self._terms[0]) if self._terms and self._terms[0] else ""
        for p, term in enumerate(self._terms[1:], 1):
            if term == 0:
                continue
            if out:
                out += " + " if term > 0 else " - "
            if abs(term) != 1:
                out += str(abs(term))
            out += "x"
            if p > 1:
                out += f"^{p}"
        return out

    def __mul__(self, other: 'Polynomial'):
        result_terms = [0] * (len(self._terms) + len(other._terms) - 1)
        for i, term1 in enumerate(self._terms):
            for j, term2 in enumerate(other._terms):
                result_terms[i + j] += term1 * term2
        return Polynomial(*result_terms)


print(f'({Polynomial(1, 2, 3)}) * ({Polynomial(4, 5, 6)}) = {Polynomial(1, 2, 3) * Polynomial(4, 5, 6)}')

# база 3
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str((self.x, self.y, self.z))

    def __add__(self, b):
        xx = self.x + b.x
        yy = self.x + b.y
        zz = self.x + b.z
        return Vector3D(xx, yy, zz)

    def __sub__(self, b):
        xx = self.x - b.x
        yy = self.x - b.y
        zz = self.x - b.z
        return Vector3D(xx, yy, zz)

    def __mul__(self, b):
        if type(b) is Vector3D:
            ss = self.x * b.x + self.y * b.y + self.z * b.z
            return ss
        else:
            return Vector3D(self.x * b, self.y * b, self.z * b)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def cos_angle(self, b):
        return (self * b) / (abs(self) * abs(b))


v1 = Vector3D(1, 1, 1)
v2 = Vector3D(1, 3, -2)
v = v1 + v2
print(v)
cf = v1 * v2
print(cf)
co = v1.cos_angle(v2)
print(co)
v3 = v1 * 10
print(v3)

# база 4
class train:
    def __init__(self, departure, purpose, departure_time, purpose_time):
        self.departure = departure
        self.purpose = purpose 
        self.departure_time = departure_time 
        self.purpose_time = purpose_time 
    def __add__(self, other):
        if self.purpose == other.departure and self.purpose_time < other.departure_time:
            new_departure = self.departure
            new_purpose = other.purpose
            new_departure_time = self.departure_time
            new_purpose_time = other.purpose_time
            return train(new_departure, new_purpose, new_departure_time, new_purpose_time)
        else:
            return None
train1 = train("Москва", "Санкт-Петербург", "10:00", "14:00")
train2 = train("Санкт-Петербург", "Москва", "15:00", "19:00")

combined_train = train1 + train2
if combined_train:
    print(f'Поезда ({train1.departure} - {train1.purpose}) могут быть объеденены')
else:
    print("Поезда не могут быть объединены.")

# доп 1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def find_books_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def sort_books_by_title(self):
        return sorted(self.books, key=self.sort_by_title)

    def sort_books_by_author(self):
        return sorted(self.books, key=self.sort_by_author)

    def sort_books_by_year(self):
        return sorted(self.books, key=self.book.year)

    def sort_by_title(self, book):
        return book.title

    def sort_by_author(self, book):
        return book.author

    def sort_by_year(self, book):
        return book.year

library = Library()

library.add_book(Book("Война и мир", "Лев Толстой", 1869))
library.add_book(Book("Преступление и наказание", "Федор Достоевский", 1866))
library.add_book(Book("Мастер и Маргарита", "Михаил Булгаков", 1928))

books_by_author = library.find_books_by_author("Лев Толстой")
print("Книги Льва Толстого:")
for book in books_by_author:
    print(book)

sorted_books_by_year = library.sort_books_by_year()
print("\nКниги, отсортированные по году издания:")
for book in sorted_books_by_year:
    print(book)

# доп 2
import math
class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b}i"

    def __add__(self, other):
        return Number(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Number(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Number(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        denominator = other.a**2 + other.b**2
        return Number((self.a * other.a + self.b * other.b) / denominator, (self.b * other.a - self.a * other.b) / denominator)

class Complex(Number):
    def __init__(self, a, b):
        super().__init__(a, b)

    def __pow__(self, power):
        r = (self.a**2 + self.b**2)**(power/2)
        theta = math.atan2(self.b, self.a)
        return Complex(r**power * math.cos(power * theta), r**power * math.sin(power * theta))

class Double(Number):
    def __init__(self, a, b):
        super().__init__(a, b)

    def __pow__(self, power):
        # Для двойных чисел возведение в степень может быть определено по-разному
        # В этом примере используется простое возведение в степень для вещественных чисел
        return Double(self.a**power, self.b**power)

class Dual(Number):
    def __init__(self, a, b):
        super().__init__(a, b)

    def __pow__(self, power):
        # Для дуальных чисел возведение в степень также может быть определено по-разному
        # В этом примере используется простое возведение в степень для вещественных чисел
        return Dual(self.a**power, self.b**power)

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)  # Сложение
print(c1 - c2)  # Вычитание
print(c1 * c2)  # Умножение
print(c1 / c2)  # Деление
print(c1 ** 2)  # Возведение в квадрат

d1 = Double(1, 2)
d2 = Double(3, 4)
print(d1 + d2)  # Сложение
print(d1 - d2)  # Вычитание
print(d1 * d2)  # Умножение
print(d1 / d2)  # Деление
print(d1 ** 2)  # Возведение в квадрат

du1 = Dual(1, 2)
du2 = Dual(3, 4)
print(du1 + du2)  # Сложение
print(du1 - du2)  # Вычитание
print(du1 * du2)  # Умножение
print(du1 / du2)  # Деление
print(du1 ** 2)  # Возведение в квадрат
