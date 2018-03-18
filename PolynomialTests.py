import unittest

from Polynomial import Polynomial

class PolynomialTests(unittest.TestCase):
    def test_init_with_correct_int_coeffs_is_correct(self):
        p = Polynomial([1, 2, 3])

        self.assertEqual(p.coeffs, [1, 2, 3])

    def test_init_with_correct_float_coeffs_is_correct(self):
        p = Polynomial([1.1, 2.2, 3.3])

        self.assertEqual(p.coeffs, [1.1, 2.2, 3.3])

    def test_init_polynomial_with_zero_degree_is_correct(self):
        p = Polynomial([1])

        self.assertEqual(p.coeffs, [1])

    def test_init_polynomial_with_zero_degree_and_redundancy_zero_coeffs_is_correct(self):
        p = Polynomial([0, 0, 1])

        self.assertEqual(p.coeffs, [1])

    def test_init_polynomial_with_one_monom_is_correct(self):
        p = Polynomial([1, 0])

        self.assertEqual(p.coeffs, [1, 0])

    def test_init_empty_polynomialis_correct(self):
        p = Polynomial([])

        self.assertEqual(p.coeffs, [0])

    def test_addition_of_polynomials_with_equal_degree_is_correct(self):
        lhp_1 = Polynomial([5, 4, 4])
        rhp_1 = Polynomial([-3, -3, 1])
        result_1 = lhp_1 + rhp_1
        self.assertEqual(result_1.coeffs, [2, 1, 5])

        lhp_2 = Polynomial([5, 4, 4])
        rhp_2 = Polynomial([-5, -3, 0])
        result_2 = lhp_2 + rhp_2
        self.assertEqual(result_2.coeffs, [1, 4])

        lhp_3 = Polynomial([5, 4, 4])
        rhp_3 = Polynomial([-5, -4, -4])
        result_3 = lhp_3 + rhp_3
        self.assertEqual(result_3.coeffs, [0])

        lhp_4 = Polynomial([5, 4, 4])
        rhp_4 = Polynomial([-4, -4, -3])
        result_4 = lhp_4 + rhp_4
        self.assertEqual(result_4.coeffs, [1, 0, 1])

        lhp_5 = Polynomial([])
        rhp_5 = Polynomial([])
        result_5 = lhp_5 + rhp_5
        self.assertEqual(result_5.coeffs, [0])

        lhp_6 = Polynomial([1])
        rhp_6 = Polynomial([5])
        result_6 = lhp_6 + rhp_6
        self.assertEqual(result_6.coeffs, [6])

        lhp_7 = Polynomial([1])
        rhp_7 = Polynomial([-1])
        result_7 = lhp_7 + rhp_7
        self.assertEqual(result_7.coeffs, [0])

    def test_addition_of_polynomials_with_not_equal_degree_is_correct(self):
        lhp_1 = Polynomial([5, 4, 4])
        rhp_1 = Polynomial([4, -3, -3, 1])
        result_1 = lhp_1 + rhp_1
        self.assertEqual(result_1.coeffs, [4, 2, 1, 5])

        lhp_2 = Polynomial([5, 4, 4])
        rhp_2 = Polynomial([4, -5, -4, -4])
        result_2 = lhp_2 + rhp_2
        self.assertEqual(result_2.coeffs, [4, 0, 0, 0])

        lhp_3 = Polynomial([4, 5, 4, 4])
        rhp_3 = Polynomial([-3, -3, 1])
        result_3 = lhp_3 + rhp_3
        self.assertEqual(result_3.coeffs, [4, 2, 1, 5])

        lhp_4 = Polynomial([4, 5, 4, 4])
        rhp_4 = Polynomial([-5, -4, -4])
        result_4 = lhp_4 + rhp_4
        self.assertEqual(result_4.coeffs, [4, 0, 0, 0])

        lhp_5 = Polynomial([4, 5, 4, 4])
        rhp_5 = Polynomial([1])
        result_5 = lhp_5 + rhp_5
        self.assertEqual(result_5.coeffs, [4, 5, 4, 5])

        lhp_6 = Polynomial([1])
        rhp_6 = Polynomial([4, 5, 4, 4])
        result_6 = lhp_6 + rhp_6
        self.assertEqual(result_6.coeffs, [4, 5, 4, 5])

        lhp_7 = Polynomial([0])
        rhp_7 = Polynomial([4, 5, 4, 4])
        result_7 = lhp_7 + rhp_7
        self.assertEqual(result_7.coeffs, [4, 5, 4, 4])

        lhp_8 = Polynomial([])
        rhp_8 = Polynomial([4, 5, 4, 4])
        result_8 = lhp_8 + rhp_8
        self.assertEqual(result_8.coeffs, [4, 5, 4, 4])

if __name__ == '__main__':
    unittest.main()