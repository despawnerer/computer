from unittest import TestCase

from computer import evaluate, UndefinedVariable, UnsupportedOperation


class BasicMathTestCase(TestCase):
    def test_addition(self):
        self.assertEqual(evaluate('2 + 2'), 4)

    def test_subtraction(self):
        self.assertEqual(evaluate('5 - 2'), 3)

    def test_multiplication(self):
        self.assertEqual(evaluate('3 * 2'), 6)

    def test_division(self):
        self.assertEqual(evaluate('10 / 2'), 5)

    def test_exponentiation(self):
        self.assertEqual(evaluate('5 ** 2'), 25)

    def test_modulo(self):
        self.assertEqual(evaluate('10 % 3'), 1)


class ComparisonsTestCase(TestCase):
    def test_equal(self):
        self.assertTrue(evaluate('5 == 5'))
        self.assertFalse(evaluate('10 == 5'))

    def test_unequal(self):
        self.assertFalse(evaluate('5 != 5'))
        self.assertTrue(evaluate('5 != 10'))

    def test_less_than(self):
        self.assertTrue(evaluate('5 < 10'))
        self.assertFalse(evaluate('10 < 5'))
        self.assertFalse(evaluate('10 < 10'))

    def test_less_than_or_equal(self):
        self.assertTrue(evaluate('5 <= 10'))
        self.assertFalse(evaluate('10 <= 5'))
        self.assertTrue(evaluate('10 <= 10'))

    def test_greater_than(self):
        self.assertTrue(evaluate('10 > 5'))
        self.assertFalse(evaluate('5 > 10'))
        self.assertFalse(evaluate('5 > 5'))

    def test_greater_than_or_equal(self):
        self.assertTrue(evaluate('10 >= 5'))
        self.assertFalse(evaluate('5 >= 10'))
        self.assertTrue(evaluate('5 >= 5'))


class BooleanTestCase(TestCase):
    def test_and(self):
        self.assertTrue(evaluate('10 > 5 and 10 > 6'))
        self.assertFalse(evaluate('10 < 5 and 10 > 6'))
        self.assertFalse(evaluate('10 > 5 and 10 < 6'))
        self.assertFalse(evaluate('10 < 5 and 10 < 6'))

    def test_or(self):
        self.assertTrue(evaluate('10 > 5 or 10 > 6'))
        self.assertTrue(evaluate('10 < 5 or 10 > 6'))
        self.assertTrue(evaluate('10 > 5 or 10 < 6'))
        self.assertFalse(evaluate('10 < 5 or 10 < 6'))


class UnaryTestCase(TestCase):
    def test_not(self):
        self.assertFalse(evaluate('not 10 > 5'))
        self.assertTrue(evaluate('not 5 > 10'))


class VariablesTestCase(TestCase):
    def test_calculating_with_variables(self):
        self.assertEqual(evaluate('a + b', a=2, b=3), 5)

    def test_comparisons_with_variable(self):
        self.assertTrue(evaluate('a < 10', a=5))

    def test_undefined_variables(self):
        with self.assertRaises(UndefinedVariable):
            evaluate('a + b', a=3)


class UnsupportedOperationsTestCase(TestCase):
    def test_strings(self):
        with self.assertRaises(UnsupportedOperation):
            evaluate('"string"')

    def test_attrs(self):
        with self.assertRaises(UnsupportedOperation):
            evaluate('b.attr', b=5)

    def test_items(self):
        with self.assertRaises(UnsupportedOperation):
            evaluate('b[0]', b=5)
