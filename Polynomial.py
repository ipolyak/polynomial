import operator

class Polynomial:
    def __init__(self, coeffsList):
        if not coeffsList:
            self.coeffs = [0]
            self.degree = 0
            return
        self.checkObjectsTypeCorrectness(coeffsList)
        self.coeffs = []
        self.coeffs[0:len(coeffsList)] = coeffsList[:]
        self.prepocessingOfCoeffsList(self.coeffs)
        self.degree = len(self.coeffs) - 1

    def __add__(self, rhValue):
        if isinstance(rhValue, Polynomial):
            if (self.degree == rhValue.degree):
                result = Polynomial(list(map(operator.add, self.coeffs, rhValue.coeffs)))
                result.prepocessingOfCoeffsList(result.coeffs)
                return result
            elif (self.degree > rhValue.degree):
                rhPolynomialCoeffs = [0] * (self.degree - rhValue.degree) + rhValue.coeffs
                result = Polynomial(list(map(operator.add, self.coeffs, rhPolynomialCoeffs)))
                result.prepocessingOfCoeffsList(result.coeffs)
                return result
            else:
                lhPolynomialCoeffs = [0] * (rhValue.degree - self.degree) + self.coeffs
                result = Polynomial(list(map(operator.add, lhPolynomialCoeffs, rhValue.coeffs)))
                result.prepocessingOfCoeffsList(result.coeffs)
                return result
        else:
            if not isinstance(coeff, (int, float)):
                raise Exception("Incorrect type of value. 'int' or 'float' type is expected.")
            result = Polynomial(self.coeffs)
            result.coeffs[len(result.coeffs) - 1] += rhValue
            return result

    def __mul__(self, rhValue):
        if isinstance(rhPolynomial, Polynomial):
            result = [0] * (self.degree + rhValue.degree + 1)
            for i, lhCoeff in enumerate(self.coeffs):
                for j, rhCoeff in enumerate(rhValue.coeffs):
                    res[i + j] += lhCoeff * rhCoeff
        else:
            if not isinstance(coeff, (int, float)):
                raise Exception("Incorrect type of value. 'int' or 'float' type is expected.")
            result = Polynomial([coef * rhValue for coef in self.coeffs])
            return result

    def __eq__(self, rhPolynomial):
        if not isinstance(rhPolynomial, Polynomial):
            raise Exception("Incorrect type of input data. Polynomial is expected.")
        return self.coeffs == rhPolynomial.coeffs

    def __str__(self):
        polynomialStr = ""
        coeffsCount = len(self.coeffs)
        if (coeffsCount == 1):
            polynomialStr += self.coeffs[0]
            return polynomialStr
        for i, coeff in enumerate(self.coeffs):
            if (((coeffsCount - 1) - i) == self.degree):
                polynomialStr += coeff + 'x' + (self.degree)
            elif (((coeffsCount - 1) - i) == 0):
                if (coeff > 0):
                    polynomialStr += '+' + coeff
                else:
                    polynomialStr += coeff
                return polynomialStr
            else:
                if (coeff != 0):
                    if (coeff > 0):
                        polynomialStr += '+' + coeff + 'x' + (degree - i)
                    else:
                        polynomialStr += coeff + 'x' + (degree - i)

    def checkObjectsTypeCorrectness(self, coeffsList):
        for i, coeff in enumerate(coeffsList):
            if not isinstance(coeff, (int, float)):
                raise Exception("The polynomial coefficients must have 'int' or 'float' type.")

    def prepocessingOfCoeffsList(self, coeffs):
        i = 0
        while ((i < len(coeffs)) and (coeffs[i] == 0)):
            coeffs.pop(0)
        if not coeffs:
            coeffs.insert(0, 0)