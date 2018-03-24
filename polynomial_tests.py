import unittest

from polynomial import Polynomial

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

        rhp_9 = Polynomial([4, 3])
        result_9 = result_8 + rhp_9
        self.assertEqual(result_9.coeffs, [4, 5, 8, 7])

        lhp_10 = Polynomial([4, 5, 4, 4])
        rhp_10 = 5
        result_10 = lhp_10 + rhp_10
        self.assertEqual(result_10.coeffs, [4, 5, 4, 9])

        lhp_11 = Polynomial([4.1, 5.2, 4.3, 4.4])
        rhp_11 = Polynomial([4.1, 5.3, 4.8, 4.1])
        result_11 = lhp_11 + rhp_11
        self.assertEqual(result_11.coeffs, [8.2, 10.5, 9.1, 8.5])

        lhp_12 = Polynomial([4.1, 5.2, 4.3, 4.4])
        rhp_12 = 5.5
        result_12 = lhp_12 + rhp_12
        self.assertEqual(result_12.coeffs, [4.1, 5.2, 4.3, 9.9])

    def test_multiply_of_polynomials_is_correct(self):
        lhp_1 = Polynomial([5, 4, 4])
        rhp_1 = Polynomial([-3, 1])
        result_1 = lhp_1 * rhp_1
        self.assertEqual(result_1.coeffs, [-15, -7, -8, 4])

        lhp_2 = Polynomial([5, 4, 4])
        rhp_2 = Polynomial([0])
        result_2 = lhp_2 * rhp_2
        self.assertEqual(result_2.coeffs, [0])

        lhp_3 = Polynomial([5, 4, 4])
        rhp_3 = Polynomial([])
        result_3 = lhp_3 * rhp_3
        self.assertEqual(result_3.coeffs, [0])

        lhp_4 = Polynomial([5, 0, 4])
        rhp_4 = Polynomial([-3, 1])
        result_4 = lhp_4 * rhp_4
        self.assertEqual(result_4.coeffs, [-15, 5, -12, 4])

        result_5 = result_4 * rhp_4
        self.assertEqual(result_5.coeffs, [45, -30, 41, -24, 4])

        lhp_5 = Polynomial([5, 0, 4])
        rhp_5 = 2
        result_6 = lhp_5 * rhp_5
        self.assertEqual(result_6.coeffs, [10, 0, 8])

        lhp_6 = Polynomial([5.1, 0, 4.5])
        rhp_6 = 2
        result_7 = lhp_6 * rhp_6
        self.assertEqual(result_7.coeffs, [10.2, 0, 9])

    def test_operator_equality_for_polynomials_is_correct(self):
        lhp_1 = Polynomial([5, 0, 4])
        rhp_1 = Polynomial([5, 0, 4])
        self.assertTrue(lhp_1 == rhp_1)

        lhp_2 = Polynomial([5, 0, 4])
        rhp_2 = Polynomial([5, 0, 5])
        self.assertFalse(lhp_2 == rhp_2)

        lhp_3 = Polynomial([0, 5, 0, 5])
        rhp_3 = Polynomial([5, 0, 5])
        self.assertTrue(lhp_3 == rhp_3)

        lhp_4 = Polynomial([0, 5.4, 0.0, 5.8])
        rhp_4 = Polynomial([5.4, 0, 5.8])
        self.assertTrue(lhp_4 == rhp_4)

        lhp_5 = Polynomial([2])
        rhp_5 = 2
        self.assertTrue(lhp_5 == rhp_5)

        lhp_6 = Polynomial([2, 1])
        rhp_6 = 2
        self.assertFalse(lhp_6 == rhp_6)

        lhp_7 = Polynomial([2])
        rhp_7 = 3
        self.assertFalse(lhp_7 == rhp_7)

    def test_operator_non_equality_for_polynomials_is_correct(self):
        lhp_1 = Polynomial([5, 0, 4])
        rhp_1 = Polynomial([5, 0, 4])
        self.assertFalse(lhp_1 != rhp_1)

        lhp_2 = Polynomial([5, 0, 4])
        rhp_2 = Polynomial([5, 0, 5])
        self.assertTrue(lhp_2 != rhp_2)

        lhp_3 = Polynomial([0, 5, 0, 5])
        rhp_3 = Polynomial([5, 0, 5])
        self.assertFalse(lhp_3 != rhp_3)

        lhp_4 = Polynomial([0, 5.4, 0.0, 5.8])
        rhp_4 = Polynomial([5.4, 0, 5.8])
        self.assertFalse(lhp_4 != rhp_4)

        lhp_5 = Polynomial([2])
        rhp_5 = 3
        self.assertTrue(lhp_5 != rhp_5)

        lhp_6 = Polynomial([2, 1])
        rhp_6 = 2
        self.assertTrue(lhp_6 != rhp_6)

        lhp_7 = Polynomial([2])
        rhp_7 = 2
        self.assertFalse(lhp_7 != rhp_7)

    def test_converting_polynomial_to_string_is_correct(self):
        p_1 = Polynomial([5, 1, 4])
        result_1 = str(p_1)
        self.assertEqual(result_1, '5x2+x+4')

        p_2 = Polynomial([-5, -1, -4])
        result_2 = str(p_2)
        self.assertEqual(result_2, '-5x2-x-4')

        p_3 = Polynomial([-1, -1, -1])
        result_3 = str(p_3)
        self.assertEqual(result_3, '-x2-x-1')

        p_4 = Polynomial([-1, -1, 0])
        result_4 = str(p_4)
        self.assertEqual(result_4, '-x2-x')

        p_5 = Polynomial([0, 0])
        result_5 = str(p_5)
        self.assertEqual(result_5, '0')

        p_6 = Polynomial([1])
        result_6 = str(p_6)
        self.assertEqual(result_6, '1')

        p_7 = Polynomial([-1])
        result_7 = str(p_7)
        self.assertEqual(result_7, '-1')

        p_8 = Polynomial([2, -1])
        result_8 = str(p_8)
        self.assertEqual(result_8, '2x-1')

        p_9 = Polynomial([2.3, -1.4])
        result_9 = str(p_9)
        self.assertEqual(result_9, '2.3x-1.4')

        p_10 = Polynomial([])
        result_10 = str(p_10)
        self.assertEqual(result_10, '0')

        p_11 = Polynomial([1, 1])
        result_11 = str(p_11)
        self.assertEqual(result_11, 'x+1')

        p_12 = Polynomial([1, 2, 2, 1])
        result_12 = str(p_12)
        self.assertEqual(result_12, 'x3+2x2+2x+1')

    def test_coeffs_is_not_list_is_incorrect(self):
        self.assertRaises(TypeError, Polynomial, 1)

    def test_incorrect_type_of_coeffs_is_incorrect(self):
        self.assertRaises(TypeError, Polynomial, ["aaa", "bb"])

    def test_incorrect_type_of_rh_value_in_equal_operation_is_incorrect(self):
        p_1 = Polynomial([1, 0])
        self.assertRaises(TypeError, p_1.__eq__, "aaa")

    def test_incorrect_type_of_rh_value_in_non_equal_operation_is_incorrect(self):
        p_1 = Polynomial([1, 0])
        self.assertRaises(TypeError, p_1.__ne__, "aaa")

    def test_incorrect_type_of_rh_value_in_add_operation_is_incorrect(self):
        p_1 = Polynomial([1, 0])
        self.assertRaises(TypeError, p_1.__add__, "aaa")

    def test_incorrect_type_of_rh_value_in_mul_operation_is_incorrect(self):
        p_1 = Polynomial([1, 0])
        self.assertRaises(TypeError, p_1.__mul__, "aaa")


if __name__ == '__main__':
    unittest.main()