import unittest
def area(a):
    '''
        Функция для вычисления площади квадрата
        Параметры:
            a: длина стороны квадрата
        Возвращаемое значение:
            площадь квадрата
        Пример:
            Входной параметр: 3
            Возвращаемое значение: 3 * 3 = 9
        '''
    if (a < 0):
        raise ValueError("a < 0")
    return a * a


def perimeter(a):
    '''
         Функция для вычисления периметра квадрата
         Параметры:
            a: длина стороны квадрата
         Возвращаемое значение:
            периметр квадрата
         Пример:
            Входной параметр: 3.2
            Возвращаемое значение: 4 * 3.2 = 12.8
    '''
    if (a < 0):
        raise ValueError("a < 0")
    return 4 * a

class SquareTestCase(unittest.TestCase):
    '''
         Класс тестов для проверки корректности работы функций
         Тесты:
            test_negative: производит проверку вывода ошибки при передаче отрицательных чисел в функции
            test_area: производит проверку функции area для положительного параметра и нуля
            test_perimeter: производит проверку функции perimeter для положительного параметра и нуля
    '''
    def test_negative(self):
        with self.assertRaises(ValueError): area(-3)
        with self.assertRaises(ValueError): perimeter(-3)

    def test_area(self):
        self.assertAlmostEqual(area(5), 25)
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3.2), 12.8)
        self.assertEqual(perimeter(0), 0)