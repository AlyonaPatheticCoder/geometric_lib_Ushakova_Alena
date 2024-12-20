import math
import re
import unittest


def area(r):
    '''
    Функция для вычисления площади круга
    Параметры:
        r: радиус
    Возвращаемое значение:
        (float)
    Пример:
        Входной параметр: 2
        Возвращаемое значение: math.pi * 2 * 2 = 12.566370614359172
    '''

    if (r < 0):
        raise ValueError("r < 0")
    return math.pi * r * r


def perimeter(r):
    '''
        Функция для вычисления периметра круга
        Параметры:
            r: радиус
        Возвращаемое значение:
            (float)
        Пример:
            Входной параметр: 4
            Возвращаемое значение: 2 * math.pi * 4 = 25.132741228718345
        '''

    if (r < 0):
        raise ValueError("r < 0")

    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
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
        self.assertAlmostEqual(area(2), 12.566370614359172)
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(4), 25.132741228718345)
        self.assertEqual(perimeter(0), 0)
