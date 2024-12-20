import unittest
def area(a, b):
    '''
        Функция для вычисления площади прямоугольника
        Параметры:
            a: длина стороны прямоугольника
            b: длина стороны прямоугольника
        Возвращаемое значение:
            площадь прямоугольника
        Пример:
            Входной параметр: 3, 4
            Возвращаемое значение: 3 * 4 = 12
        '''
    if (a < 0):
        raise ValueError("a < 0")
    if (b < 0):
        raise ValueError("b < 0")
    return a * b


def perimeter(a, b):
    '''
         Функция для вычисления периметра прямоугольника
         Параметры:
            a: длина стороны прямоугольника
         Возвращаемое значение:
            периметр прямоугольника
         Пример:
            Входной параметр: 3, 4
            Возвращаемое значение: 14
    '''
    if (a < 0):
        raise ValueError("a < 0")
    if (b < 0):
        raise ValueError("b < 0")
    if (a == 0):
        return 0
    if (b == 0):
        return 0
    return 2 * a + 2 * b

class RectangleTestCase(unittest.TestCase):
    '''
         Класс тестов для проверки корректности работы функций
         Тесты:
            test_negative_a: производит проверку вывода ошибки при передаче отрицательных чисел в функции
            для параметра a
            test_negative_b: производит проверку вывода ошибки при передаче отрицательных чисел в функции
            для параметра b
            test_area: производит проверку функции area для положительного параметра и нуля
            в параметре a и b
            test_perimeter: производит проверку функции perimeter для положительного параметра и нуля
            в параметре a и b
    '''
    def test_negative_a(self):
        with self.assertRaises(ValueError): area(-3, 1)
        with self.assertRaises(ValueError): perimeter(-3, 1)
    def test_negative_b(self):
        with self.assertRaises(ValueError): area(3, -1)
        with self.assertRaises(ValueError): perimeter(3, -1)

    def test_area(self):
        self.assertAlmostEqual(area(3, 4), 12)
        self.assertEqual(area(0, 1), 0)
        self.assertEqual(area(2, 0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(4, 5), 18)
        self.assertEqual(perimeter(0, 3), 0)

