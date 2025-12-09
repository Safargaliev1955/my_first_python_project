'''Класс фигура (пустой)
Класс Прямоугольник унаследован от фигуры:
Конструктор по 2 сторонам
Метод вычисления площади
Метод вычисления периметра

Класс Квадрат унаследован от прямоугольника
Конструктор по 1 стороне
Метод вычисления Площади (другой формулой)
Метод вычисления периметра (другой формулой)

Класс треугольник унаследован от фигуры
Конструктор по 3 сторонам
Метод вычисления площади (с проверкой возможности треугольника)
Метод вычисления периметра (с проверкой возможности треугольника)'''


class Shape:
    @property
    def area():
        pass

    @property
    def perimeter():
        pass

class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    
    @property
    def perimeter(self):
        return self.side1 * 2 + self.side2 * 2
    
    @property
    def area(self):
        return self.side1 * self.side2

    def __str__(self):
        return f"Прямоугольник с периметром {self.perimeter} и площадью {self.area}"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __str__(self):
        return f"Треугольник с периметром {self.perimeter} и площадью {self.area}" if self.is_exists else "Треугольника с такими сторонами не существует"

    @property
    def is_exists(self):
        return (
            self.side1 < self.side2 + self.side3
            and
            self.side2 < self.side1 + self.side3
            and
            self.side3 < self.side2 + self.side1
            )
    @property
    def perimeter(self):
        if self.is_exists:
            return self.side1 + self.side2 + self.side3
        else:
            print("Треугольника с такими сторонами не существует")
            return None

    @property
    def area(self):
        if self.is_exists:
            p = self.perimeter/2
            return (p * (p-self.side1) * (p-self.side2) * (p-self.side3)) ** 0.5
        else:
            print("Треугольника с такими сторонами не существует")
            return None

if __name__ == "__main__":
    square = Square(10)
    triangle = Triangle(3,4,5)
    triangle1 = Triangle(1,2,50)
    rectangle = Rectangle(10,20)
    print(square)
    print(triangle)
    print(triangle1)
    print(rectangle)
